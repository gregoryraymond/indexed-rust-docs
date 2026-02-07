# Indexed Rust Documentation

Structured indexes of Rust skills and documentation for AI assistants.

> **Approach inspired by** [@next/codemod@canary agents-md](https://github.com/vercel/next.js/tree/canary/packages/codemods/transforms/agents-md) - a pattern for organizing domain knowledge as indexed markdown files.

## What's Inside

- **Rust Skills** - Guides for common Rust patterns, errors, and best practices
- **Documentation Indexes** - Curated links to official Rust documentation
- **Auto-indexing Tools** - Scripts to rebuild the index as content grows

## Structure

```
.
├── CLAUDE.md              # Main index file (auto-generated)
├── rust-docs/
│   ├── rust-skills/       # Skill guides organized by topic
│   │   ├── m01-ownership/
│   │   ├── m02-resource/
│   │   ├── m06-error-handling/
│   │   └── ...
│   ├── rust-book/         # Rust Book index
│   ├── tokio/             # Tokio documentation index
│   ├── embedded-book/     # Embedded Rust index
│   └── ...
├── reindex-docs.py        # Python indexer (recommended)
└── reindex-docs.sh        # Bash indexer (alternative)
```

## Usage

Clone and reference in your project's `CLAUDE.md`:

```bash
git clone https://github.com/gregoryraymond/indexed-rust-docs.git
```

```markdown
# include ./indexed-rust-docs/CLAUDE.md
```

The index provides:
- Error code routing (E0382 → ownership skill)
- Task-based skill selection (async → concurrency skill)
- Documentation links with URLs

## Skills Included

Ownership & borrowing, smart pointers, error handling, concurrency, async/await, performance, web development, unsafe/FFI, and more.

## Adding New Skills

1. Create a new directory in `rust-docs/rust-skills/`:
   ```bash
   mkdir rust-docs/rust-skills/my-new-skill
   ```

2. Create a `SKILL.md` with frontmatter:
   ```markdown
   ---
   name: my-new-skill
   description: "What this skill covers. Triggers: keywords, error codes"
   user-invocable: false
   ---

   # Skill Content
   ...
   ```

3. Rebuild the index:
   ```bash
   python3 reindex-docs.py
   # or
   ./reindex-docs.sh
   ```

4. Commit and push:
   ```bash
   git add .
   git commit -m "Add new skill: my-new-skill"
   git push
   ```

## Re-indexing

After adding new skills or documentation:

```bash
python3 reindex-docs.py  # Recommended
# or
./reindex-docs.sh
# or with Claude Code
/reindex-docs
```

## Contributing

PRs welcome! To add skills:

1. Create a new directory in `rust-docs/rust-skills/`
2. Add a `SKILL.md` with YAML frontmatter
3. Run `python3 reindex-docs.py`
4. Submit PR

## Requirements

Python 3.7+ with PyYAML (`pip install pyyaml`) or Bash 4.0+

## Acknowledgments

- Indexing approach inspired by [@next/codemod@canary agents-md](https://github.com/vercel/next.js/tree/canary/packages/codemods/transforms/agents-md)
- Official Rust documentation team
- Claude Code team for the agent skill framework

## License

MIT
