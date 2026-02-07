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

## Installation

**Recommended: Global installation**

Clone to `~/.rust-docs-index` for use across all projects:

```bash
git clone https://github.com/gregoryraymond/indexed-rust-docs.git ~/.rust-docs-index
```

Then in any Rust project, append to your `CLAUDE.md`:

```bash
# Create CLAUDE.md if it doesn't exist, then append the index
cat ~/.rust-docs-index/CLAUDE.md >> CLAUDE.md
```

Or use the `# include` directive for dynamic updates:

```markdown
# include ~/.rust-docs-index/CLAUDE.md
```

**Per-project installation**

Alternatively, clone into your project directory:

```bash
git clone https://github.com/gregoryraymond/indexed-rust-docs.git
```

Then reference in your project's `CLAUDE.md`:

```markdown
# include ./indexed-rust-docs/CLAUDE.md
```

## What This Provides

- **Error code routing** - E0382 → ownership skill
- **Task-based skill selection** - "async" → concurrency skill
- **Documentation indexes** - Links to Rust Book, Tokio, Tauri, etc.
- **Pattern reference** - Quick lookup for common patterns
- **Retrieval-led reasoning** - Claude consults skills before answering

## How It Works

When you include `CLAUDE.md` in your project, Claude Code will:

1. See the index of available skills and documentation
2. Route compiler errors to relevant skill files (e.g., E0382 → ownership)
3. Select skills based on your task type (e.g., web → domain-web)
4. Read the full skill content on-demand to provide guidance
5. Follow documentation URLs for deep-dive information

**Example workflow:**
```
You: "Getting error E0382: use of moved value"
Claude: Reads ~/.rust-docs-index/rust-docs/rust-skills/m01-ownership/SKILL.md
Claude: Provides guidance on ownership, move semantics, and solutions
```

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

After adding new skills or documentation, rebuild the index:

```bash
cd ~/.rust-docs-index
python3 reindex-docs.py  # Recommended
# or
./reindex-docs.sh
# or with Claude Code
/reindex-docs
```

The scripts will regenerate `CLAUDE.md` with updated paths and metadata.

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
