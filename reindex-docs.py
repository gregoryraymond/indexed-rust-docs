#!/usr/bin/env python3
"""
Rust Documentation Indexer
Rebuilds CLAUDE.md from rust-docs/ structure with enhanced metadata extraction
"""

import re
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Optional

RUST_DOCS_DIR = Path("./rust-docs")
RUST_SKILLS_DIR = RUST_DOCS_DIR / "rust-skills"
CLAUDE_MD = Path("./CLAUDE.md")

class SkillMeta:
    """Metadata extracted from a skill's SKILL.md file"""
    def __init__(self, path: Path):
        self.path = path
        self.dir_name = path.parent.name
        self.name = ""
        self.description = ""
        self.user_invocable = False
        self.error_codes = []
        self.triggers = []
        self.short_desc = ""
        self._parse()

    def _parse(self):
        """Parse YAML frontmatter from SKILL.md"""
        content = self.path.read_text(encoding='utf-8')

        # Extract YAML frontmatter
        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if match:
            try:
                meta = yaml.safe_load(match.group(1))
                self.name = meta.get('name', self.dir_name)
                self.description = meta.get('description', '')
                self.user_invocable = meta.get('user-invocable', False)

                # Extract error codes
                self.error_codes = re.findall(r'E\d{4}', self.description)

                # Extract short description (before "Triggers:")
                if 'Triggers:' in self.description:
                    desc_part = self.description.split('Triggers:')[0]
                else:
                    desc_part = self.description

                # Clean up description
                desc_part = re.sub(r'CRITICAL:\s*', '', desc_part)
                desc_part = re.sub(r'Use (for|when)\s+', '', desc_part)
                self.short_desc = desc_part.strip().rstrip('.').split('.')[0]

                # Extract trigger keywords
                if 'Triggers:' in self.description:
                    triggers_text = self.description.split('Triggers:')[1]
                    self.triggers = [t.strip() for t in triggers_text.split(',')]

            except yaml.YAMLError as e:
                print(f"⚠️  Warning: Could not parse YAML in {self.path}: {e}")

class DocMeta:
    """Metadata extracted from a documentation index.md file"""
    def __init__(self, path: Path):
        self.path = path
        self.dir_name = path.parent.name
        self.title = ""
        self.quick_ref = ""
        self.source = ""
        self._parse()

    def _parse(self):
        """Parse markdown index file"""
        content = self.path.read_text(encoding='utf-8')
        lines = content.split('\n')

        # Extract title (first H1)
        for line in lines:
            if line.startswith('# '):
                self.title = line.lstrip('# ').strip()
                break

        # Extract source URL
        source_match = re.search(r'>\s*Sources?:\s*([^\n]+)', content)
        if source_match:
            self.source = source_match.group(1).split('|')[0].strip()

        # Extract quick reference
        quick_ref_match = re.search(r'## Quick Reference\n\n([^\n]+)', content)
        if quick_ref_match:
            self.quick_ref = quick_ref_match.group(1)[:100]

def scan_skills() -> List[SkillMeta]:
    """Scan all skills in rust-docs/rust-skills/"""
    skills = []
    for skill_file in sorted(RUST_SKILLS_DIR.glob("*/SKILL.md")):
        skills.append(SkillMeta(skill_file))
    return skills

def scan_docs() -> List[DocMeta]:
    """Scan all documentation indexes in rust-docs/"""
    docs = []
    for doc_file in sorted(RUST_DOCS_DIR.glob("*/index.md")):
        # Skip rust-skills directory
        if "rust-skills" not in str(doc_file):
            docs.append(DocMeta(doc_file))
    return docs

def categorize_skills(skills: List[SkillMeta]) -> Dict[str, List[SkillMeta]]:
    """Categorize skills by common patterns"""
    categories = {
        "Ownership & Borrowing": [],
        "Smart Pointers & Resources": [],
        "Mutability": [],
        "Generics & Traits": [],
        "Type Safety": [],
        "Error Handling": [],
        "Concurrency & Async": [],
        "Domain Modeling": [],
        "Performance": [],
        "Ecosystem & Crates": [],
        "Resource Lifecycle": [],
        "Code Quality": [],
        "Web Development": [],
        "Unsafe & FFI": [],
        "Tooling & LSP": [],
        "Meta & Utilities": []
    }

    patterns = {
        "Ownership & Borrowing": r'ownership|borrow|lifetime',
        "Smart Pointers & Resources": r'Box|Rc|Arc|RefCell|smart pointer',
        "Mutability": r'mutability|Cell|Mutex',
        "Generics & Traits": r'generic|trait|zero-cost',
        "Type Safety": r'type.*driven|newtype|PhantomData',
        "Error Handling": r'error.*handling|Result|Option',
        "Concurrency & Async": r'concurrency|async|thread|tokio',
        "Domain Modeling": r'domain|DDD|aggregate',
        "Performance": r'performance|benchmark|optim',
        "Ecosystem & Crates": r'ecosystem|crate|dependency',
        "Resource Lifecycle": r'lifecycle|RAII|Drop|pool',
        "Code Quality": r'anti-pattern|guideline|style|review',
        "Web Development": r'web|axum|actix|HTTP',
        "Unsafe & FFI": r'unsafe|FFI|raw pointer',
        "Tooling & LSP": r'LSP|call.*graph|navigator|refactor|symbol',
        "Meta & Utilities": r'meta|router|learner|visualiz|creator|daily'
    }

    for skill in skills:
        categorized = False
        for category, pattern in patterns.items():
            if re.search(pattern, skill.description, re.IGNORECASE):
                categories[category].append(skill)
                categorized = True
                break

        if not categorized:
            categories["Meta & Utilities"].append(skill)

    # Remove empty categories
    return {k: v for k, v in categories.items() if v}

def build_skills_index(skills: List[SkillMeta]) -> str:
    """Build skills directory structure section"""
    out = []
    out.append("## Skills Directory Structure\n")
    out.append("```")
    out.append("./rust-docs/rust-skills/")

    for skill in sorted(skills, key=lambda s: s.dir_name):
        desc = skill.short_desc[:60] if len(skill.short_desc) > 60 else skill.short_desc
        out.append(f"├── {skill.dir_name}/".ljust(30) + f" | {desc}")

    out.append("```\n")
    return "\n".join(out)

def build_error_routing(skills: List[SkillMeta]) -> str:
    """Build error code routing table"""
    out = []
    out.append("## Quick Error Code → Skill Routing\n")
    out.append("When encountering compiler errors, consult the corresponding skill:\n")
    out.append("```")

    error_map = defaultdict(list)
    for skill in skills:
        for code in skill.error_codes:
            error_map[code].append(skill.dir_name)

    for code in sorted(error_map.keys()):
        skills_list = ", ".join(error_map[code])
        out.append(f"{code}".ljust(20) + f"→ ./rust-docs/rust-skills/{skills_list}/")

    out.append("```\n")
    return "\n".join(out)

def build_task_categories(skills: List[SkillMeta]) -> str:
    """Build task-based skill selection guide"""
    out = []
    out.append("## Skill Selection by Task Type\n")

    categories = categorize_skills(skills)

    for category, skill_list in categories.items():
        if not skill_list:
            continue

        out.append(f"**{category}**")
        for skill in skill_list:
            out.append(f"- `./rust-docs/rust-skills/{skill.dir_name}/` - {skill.short_desc}")
        out.append("")

    return "\n".join(out)

def build_docs_index(docs: List[DocMeta]) -> str:
    """Build documentation index section"""
    out = []
    out.append("## Documentation Index\n")
    out.append("```")
    out.append("./rust-docs/")

    for doc in sorted(docs, key=lambda d: d.dir_name):
        title = doc.title[:50] if len(doc.title) > 50 else doc.title
        out.append(f"├── {doc.dir_name}/index.md".ljust(30) + f" | {title}")

    out.append("```\n")

    out.append("### Documentation by Topic\n")
    for doc in sorted(docs, key=lambda d: d.dir_name):
        if doc.quick_ref:
            out.append(f"**{doc.title}** → `./rust-docs/{doc.dir_name}/index.md`")
            out.append(f"- {doc.quick_ref}")
            if doc.source:
                out.append(f"- Source: {doc.source}")
            out.append("")

    return "\n".join(out)

def generate_claude_md(skills: List[SkillMeta], docs: List[DocMeta]):
    """Generate complete CLAUDE.md file"""
    sections = []

    # Header
    sections.append("# Rust Development - Documentation Index\n")
    sections.append("**Instruction**: When working on Rust tasks, consult the skill files in `./rust-docs/rust-skills/` and documentation indexes in `./rust-docs/` for guidance. These files contain patterns, best practices, and decision frameworks.\n")
    sections.append("---\n")

    # Skills index
    sections.append(build_skills_index(skills))
    sections.append("---\n")

    # Error routing
    sections.append(build_error_routing(skills))
    sections.append("---\n")

    # Task categories
    sections.append(build_task_categories(skills))
    sections.append("---\n")

    # Docs index
    sections.append(build_docs_index(docs))
    sections.append("---\n")

    # Usage instructions
    sections.append("""## How to Use This Index

1. **On compiler error**: Check error code routing → Read skill file
2. **On design question**: Browse skills by category → Read relevant skill
3. **On library/framework question**: Check docs index → Read doc index, follow URLs
4. **Multi-skill needed**: Read multiple skill files and synthesize
5. **Deep dive**: Use Grep to search within skill/doc files

**Example workflows:**
```
# Compiler error
Error E0382 → Read ./rust-docs/rust-skills/m01-ownership/SKILL.md

# Design question
"How to share state across threads?" → Browse Concurrency & Async → Read m07-concurrency

# Framework question
"How to spawn tokio tasks?" → Read ./rust-docs/tokio/index.md → Follow tutorial URL
```

---

*This index is auto-generated. Run `./reindex-docs.py` or `./reindex-docs.sh` or invoke `/reindex-docs` skill to rebuild.*
""")

    # Write to file
    CLAUDE_MD.write_text("\n".join(sections), encoding='utf-8')

def main():
    """Main execution"""
    print("🔍 Scanning Rust documentation structure...")

    if not RUST_DOCS_DIR.exists():
        print(f"❌ Error: {RUST_DOCS_DIR} not found")
        return 1

    # Scan structure
    skills = scan_skills()
    docs = scan_docs()

    print(f"📝 Found {len(skills)} skills and {len(docs)} documentation indexes")
    print(f"📄 Generating {CLAUDE_MD}...")

    # Generate index
    generate_claude_md(skills, docs)

    print("✅ Index rebuilt successfully!")
    print(f"📊 Summary:")
    print(f"   - Skills indexed: {len(skills)}")
    print(f"   - Docs indexed: {len(docs)}")

    # Show categorization
    categories = categorize_skills(skills)
    print(f"   - Skill categories: {len(categories)}")
    for cat, skill_list in categories.items():
        print(f"     • {cat}: {len(skill_list)}")

    return 0

if __name__ == "__main__":
    exit(main())
