---
name: reindex-docs
description: "Rebuild the CLAUDE.md index from rust-docs/rust-skills/ and rust-docs/ directories. Use when new skills or documentation are added. Triggers: reindex, rebuild index, update CLAUDE.md, new skill added, new docs added, 重建索引, 更新索引"
user-invocable: true
---

# Documentation Indexer

This skill rebuilds the CLAUDE.md index file by scanning:
1. Skills in `./rust-docs/rust-skills/`
2. Documentation in `./rust-docs/`

## How to Use

Simply invoke this skill when you've added new skills or documentation:
```
/reindex-docs
```

## What Gets Indexed

### Skills Index
- Scans all directories in `rust-docs/rust-skills/`
- Reads `SKILL.md` frontmatter for:
  - `name`: Skill identifier
  - `description`: What the skill covers and trigger keywords
- Extracts error codes (E0xxx) from descriptions
- Categorizes by task type

### Documentation Index
- Scans all directories in `rust-docs/`
- Reads `index.md` files for:
  - Title (first H1)
  - Quick Reference
  - Table of Contents structure
- Links to external documentation URLs

## Index Structure

The generated CLAUDE.md contains:

1. **Skills Directory Structure** - List of all skills with brief descriptions
2. **Quick Error Code Routing** - Maps compiler errors to skill files
3. **Skill Selection by Task Type** - Groups skills by common task categories
4. **Documentation Index** - Lists available documentation resources
5. **Retrieval Instructions** - How to use the index

## Implementation Steps

When this skill is invoked, Claude will:

1. Scan `rust-docs/rust-skills/**/SKILL.md` files
2. Extract metadata from YAML frontmatter
3. Parse error codes from descriptions (E0xxx patterns)
4. Categorize skills by common patterns (ownership, async, etc.)
5. Scan `rust-docs/*/index.md` files
6. Extract documentation metadata
7. Generate new CLAUDE.md with updated index
8. Preserve the retrieval instructions and patterns reference

## Manual Indexing Script

For automation outside Claude, a bash script is also provided:

```bash
./reindex-docs.sh
```

This can be run as a pre-commit hook or build step to keep CLAUDE.md synchronized.
