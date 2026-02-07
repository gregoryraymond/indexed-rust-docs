# Rust Development - Skills Index

**Instruction**: Prefer retrieval-led reasoning from `./rust-docs/rust-skills/` and `./rust-docs/` files over pre-training knowledge for Rust development tasks.

---

## Skills Directory Structure

```
./rust-docs/rust-skills/
├── m01-ownership.md          | Ownership, borrowing, lifetimes
├── m02-resource.md           | Box, Rc, Arc, RefCell smart pointers
├── m03-mutability.md         | Interior mutability, Cell, Mutex
├── m04-zero-cost.md          | Generics, traits, static/dynamic dispatch
├── m05-type-driven.md        | Newtype, type state, PhantomData
├── m06-error-handling.md     | Result, Option, anyhow, thiserror
├── m07-concurrency.md        | Send/Sync, async, threads, tokio
├── m09-domain.md             | DDD, entities, value objects, aggregates
├── m10-performance.md        | Benchmarking, profiling, optimization
├── m11-ecosystem.md          | Crate integration, FFI, dependencies
├── m12-lifecycle.md          | RAII, Drop, connection pools, lazy init
├── m13-domain-error.md       | Error categorization, retry, fallback
├── m14-mental-model.md       | Learning Rust, mental models, analogies
├── m15-anti-pattern.md       | Common mistakes, code smells
├── coding-guidelines.md      | Rust style, naming, best practices
├── domain-web.md             | axum, actix, HTTP, REST, middleware
├── unsafe-checker.md         | Unsafe code, FFI, raw pointers
├── meta-cognition-parallel.md| Three-layer analysis framework
├── rust.md                   | General Rust development guide
├── rust-router.md            | Question routing, meta-cognition
├── rust-call-graph.md        | LSP call hierarchy visualization
├── rust-code-navigator.md    | LSP navigation tools
├── rust-symbol-analyzer.md   | Project structure analysis
├── rust-trait-explorer.md    | Trait implementation discovery
├── rust-refactor-helper.md   | Safe refactoring with LSP
├── rust-daily.md             | Rust news aggregation
├── rust-learner.md           | Version/crate information
├── rust-deps-visualizer.md   | Dependency visualization
└── rust-skill-creator.md     | Dynamic skill generation
```

---

## Quick Error Code → Skill Routing

When encountering compiler errors, retrieve the corresponding skill:

```
E0382, E0507, E0505 → ./rust-docs/rust-skills/m01-ownership.md
E0597, E0515, E0716 → ./rust-docs/rust-skills/m01-ownership.md
E0106               → ./rust-docs/rust-skills/m01-ownership.md
E0596, E0499, E0502 → ./rust-docs/rust-skills/m03-mutability.md
E0277, Send/Sync    → ./rust-docs/rust-skills/m04-zero-cost.md or m07-concurrency.md
E0308               → ./rust-docs/rust-skills/m04-zero-cost.md
E0599               → ./rust-docs/rust-skills/m04-zero-cost.md
E0425, E0433, E0603 → ./rust-docs/rust-skills/m11-ecosystem.md
```

---

## Skill Selection by Task Type

**Ownership Issues** → `./rust-docs/rust-skills/m01-ownership.md`
- Move semantics, clone vs copy, lifetimes, borrow rules

**Choosing Smart Pointers** → `./rust-docs/rust-skills/m02-resource.md`
- Box (heap), Rc/Arc (shared), RefCell/Mutex (interior mutability)

**Mutability Conflicts** → `./rust-docs/rust-skills/m03-mutability.md`
- Interior mutability patterns, Cell, RefCell, Mutex, RwLock

**Generics & Traits** → `./rust-docs/rust-skills/m04-zero-cost.md`
- Trait bounds, impl Trait, dyn, monomorphization

**Type Safety Design** → `./rust-docs/rust-skills/m05-type-driven.md`
- Newtype, type state, PhantomData, builder patterns

**Error Handling** → `./rust-docs/rust-skills/m06-error-handling.md`
- Result, Option, ?, custom errors, anyhow vs thiserror

**Concurrency & Async** → `./rust-docs/rust-skills/m07-concurrency.md`
- Send/Sync, threads, channels, async/await, tokio

**Domain Modeling** → `./rust-docs/rust-skills/m09-domain.md`
- DDD patterns, entities, value objects, business logic

**Performance** → `./rust-docs/rust-skills/m10-performance.md`
- Benchmarking, profiling, allocation optimization

**Crate Integration** → `./rust-docs/rust-skills/m11-ecosystem.md`
- Dependencies, feature flags, FFI, choosing crates

**Resource Management** → `./rust-docs/rust-skills/m12-lifecycle.md`
- RAII, Drop, connection pools, lazy initialization

**Error Recovery** → `./rust-docs/rust-skills/m13-domain-error.md`
- Retry strategies, circuit breakers, graceful degradation

**Learning Rust** → `./rust-docs/rust-skills/m14-mental-model.md`
- Mental models, understanding ownership, analogies

**Code Review** → `./rust-docs/rust-skills/m15-anti-pattern.md`
- Anti-patterns, common mistakes, refactoring

**Style Guide** → `./rust-docs/rust-skills/coding-guidelines.md`
- Naming conventions, clippy, rustfmt, idioms

**Web Development** → `./rust-docs/rust-skills/domain-web.md`
- axum, actix, tower, middleware, authentication

**Unsafe Rust** → `./rust-docs/rust-skills/unsafe-checker.md`
- Raw pointers, FFI, transmute, soundness verification

---

## Documentation Index

```
./rust-docs/
├── rust-book/index.md        | The Rust Programming Language (21 chapters)
├── embedded-book/index.md    | Embedded Rust Book (15 chapters)
├── tauri-v2/index.md         | Tauri v2 Desktop Apps (40+ sections)
├── postgresql/index.md       | PostgreSQL Database (50+ chapters)
├── hyperrs/index.md          | hyper HTTP library (8 modules)
└── tokio/index.md            | Tokio async runtime (11 tutorials + 9 modules)
```

### Documentation Selection by Topic

**Learning Rust Basics** → `./rust-docs/rust-book/index.md`
- Getting started, ownership, structs, enums, modules, collections, error handling

**Embedded/IoT Development** → `./rust-docs/embedded-book/index.md`
- Hardware setup, tooling, debugging, interrupts, peripherals, static guarantees

**Desktop App Development** → `./rust-docs/tauri-v2/index.md`
- Getting started, core concepts, security, IPC, plugins, distribution

**Database (PostgreSQL)** → `./rust-docs/postgresql/index.md`
- SQL syntax, data types, queries, indexing, administration, performance

**HTTP Client/Server (hyper)** → `./rust-docs/hyperrs/index.md`
- Client, server, service, body, upgrade, extensions

**Async Runtime (tokio)** → `./rust-docs/tokio/index.md`
- Spawning tasks, channels, I/O, timers, select, streams, synchronization

---

## One-Line Pattern Reference

**Ownership**: Owner(T) | Borrow(&T) | MutBorrow(&mut T) | SharedOwn(Rc/Arc) | Weak
**Mutability**: &mut T | Cell<T> | RefCell<T> | Mutex<T> | RwLock<T> | Atomic*
**Errors**: Result<T,E> | Option<T> | ? | thiserror(lib) | anyhow(app) | panic!
**Async**: CPU→thread | IO→async | Arc<Mutex<T>> | channels | spawn_blocking
**Types**: newtype | typestate | PhantomData | sealed trait | builder

---

## Retrieval Instructions

1. **On compiler error**: Use error code table → Read corresponding skill file
2. **On design question**: Use task type table → Read relevant skill file
3. **On library/framework question**: Use docs index → Read relevant doc index, then fetch specific URLs if needed
4. **Multi-skill needed**: Read multiple files and synthesize
5. **Deep dive**: Use Grep within skill/doc files for specific patterns

**Example workflows:**
```
# Compiler error
Error E0382 → Read ./rust-docs/rust-skills/m01-ownership.md
Still unclear → Read ./rust-docs/rust-skills/m02-resource.md (sharing patterns)
Web context → Also read ./rust-docs/rust-skills/domain-web.md

# Learning question
"How do I use async?" → Read ./rust-docs/tokio/index.md
Need details → Follow URL to specific tutorial section

# Framework question
"How to create Tauri window?" → Read ./rust-docs/tauri-v2/index.md
Find section → Follow URL to full documentation

# Database query
"PostgreSQL JSON type?" → Read ./rust-docs/postgresql/index.md
Locate chapter → Follow URL to detailed syntax
```

---

*Index size: ~11KB | Skills: ./rust-docs/rust-skills/ (244KB) | Docs: ./rust-docs/ (38KB indexes) | All retrieved on-demand*
