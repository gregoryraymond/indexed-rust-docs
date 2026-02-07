#!/usr/bin/env bash
set -euo pipefail

# Rust Documentation Indexer
# Rebuilds CLAUDE.md from rust-docs/ structure

RUST_DOCS_DIR="./rust-docs"
RUST_SKILLS_DIR="$RUST_DOCS_DIR/rust-skills"
CLAUDE_MD="./CLAUDE.md"

echo "🔍 Scanning Rust documentation structure..."

# Extract skill metadata from SKILL.md frontmatter
extract_skill_metadata() {
    local skill_file="$1"
    local field="$2"

    # Extract YAML frontmatter between --- markers
    awk '/^---$/{flag=!flag; next} flag && /^'"$field"':/ {
        sub(/^'"$field"': *"?/, "");
        sub(/"? *$/, "");
        print;
        exit
    }' "$skill_file"
}

# Extract error codes from skill description
extract_error_codes() {
    local description="$1"
    echo "$description" | grep -oE 'E[0-9]{4}' | sort -u || true
}

# Get skill directory name
get_skill_name() {
    basename "$(dirname "$1")"
}

# Build skills index
build_skills_index() {
    echo "## Skills Directory Structure"
    echo ""
    echo '```'
    echo "./rust-docs/rust-skills/"

    # Find all SKILL.md files and process them
    find "$RUST_SKILLS_DIR" -maxdepth 2 -name "SKILL.md" | sort | while read -r skill_file; do
        skill_name=$(get_skill_name "$skill_file")
        description=$(extract_skill_metadata "$skill_file" "description")

        # Extract short description (before "Triggers:")
        short_desc=$(echo "$description" | sed 's/\. Triggers:.*//' | sed 's/CRITICAL: Use for //' | sed 's/Use when //' | head -c 60)

        echo "├── $skill_name/" | sed 's/^/│   /'
    done

    echo '```'
    echo ""
}

# Build error code routing
build_error_routing() {
    echo "## Quick Error Code → Skill Routing"
    echo ""
    echo "When encountering compiler errors, consult the corresponding skill:"
    echo ""
    echo '```'

    # Collect error codes and their associated skills
    declare -A error_map

    find "$RUST_SKILLS_DIR" -maxdepth 2 -name "SKILL.md" | while read -r skill_file; do
        skill_name=$(get_skill_name "$skill_file")
        description=$(extract_skill_metadata "$skill_file" "description")
        error_codes=$(extract_error_codes "$description")

        if [ -n "$error_codes" ]; then
            echo "$error_codes" | while read -r code; do
                echo "$code → ./rust-docs/rust-skills/$skill_name/SKILL.md"
            done
        fi
    done | sort -u

    echo '```'
    echo ""
}

# Build documentation index
build_docs_index() {
    echo "## Documentation Index"
    echo ""
    echo '```'
    echo "./rust-docs/"

    find "$RUST_DOCS_DIR" -maxdepth 2 -name "index.md" -o -type d | grep -v rust-skills | while read -r doc_path; do
        if [ -f "$doc_path" ]; then
            doc_dir=$(basename "$(dirname "$doc_path")")
            # Extract title from index.md first H1
            title=$(grep -m 1 "^# " "$doc_path" | sed 's/^# //' || echo "$doc_dir")
            echo "├── $doc_dir/index.md        | $title"
        fi
    done | grep -v "^\./rust-docs/index.md" | sort

    echo '```'
    echo ""
}

# Generate CLAUDE.md
generate_claude_md() {
    cat > "$CLAUDE_MD" << 'HEADER'
# Rust Development - Documentation Index

**Instruction**: When working on Rust tasks, consult the skill files in `./rust-docs/rust-skills/` and documentation indexes in `./rust-docs/` for guidance. These files contain patterns, best practices, and decision frameworks.

---

HEADER

    build_skills_index >> "$CLAUDE_MD"
    echo "---" >> "$CLAUDE_MD"
    echo "" >> "$CLAUDE_MD"
    build_error_routing >> "$CLAUDE_MD"
    echo "---" >> "$CLAUDE_MD"
    echo "" >> "$CLAUDE_MD"
    build_docs_index >> "$CLAUDE_MD"

    cat >> "$CLAUDE_MD" << 'FOOTER'
---

## How to Use This Index

1. **On compiler error**: Check error code routing → Read skill file
2. **On design question**: Browse skills by description → Read relevant skill
3. **On library/framework question**: Check docs index → Read doc index, follow URLs
4. **Multi-skill needed**: Read multiple skill files and synthesize
5. **Deep dive**: Use Grep to search within skill/doc files

**Example workflows:**
```
# Compiler error
Error E0382 → Read ./rust-docs/rust-skills/m01-ownership/SKILL.md

# Design question
"How to share state across threads?" → Browse skills → Read m07-concurrency

# Framework question
"How to spawn tokio tasks?" → Read ./rust-docs/tokio/index.md → Follow tutorial URL
```

---

*This index is auto-generated. Run `./reindex-docs.sh` or invoke `/reindex-docs` to rebuild.*
FOOTER
}

# Main execution
main() {
    if [ ! -d "$RUST_DOCS_DIR" ]; then
        echo "❌ Error: $RUST_DOCS_DIR not found"
        exit 1
    fi

    echo "📝 Generating CLAUDE.md index..."
    generate_claude_md

    echo "✅ Index rebuilt successfully!"
    echo "📄 Updated: $CLAUDE_MD"

    # Show summary
    skill_count=$(find "$RUST_SKILLS_DIR" -maxdepth 2 -name "SKILL.md" | wc -l)
    doc_count=$(find "$RUST_DOCS_DIR" -maxdepth 2 -name "index.md" | grep -v rust-skills | wc -l)

    echo ""
    echo "📊 Summary:"
    echo "   - Skills indexed: $skill_count"
    echo "   - Docs indexed: $doc_count"
}

main "$@"
