# Tokio - Asynchronous Runtime for Rust

> Sources: https://tokio.rs/ | https://docs.rs/tokio/latest/tokio/

## Quick Reference

An event-driven, non-blocking I/O platform for writing asynchronous applications with Rust. Provides async runtime, task scheduling, timers, networking, and synchronization primitives.

## Table of Contents

### Tutorial

- [Overview](https://tokio.rs/tokio/tutorial) - Introduction to Tokio
- [Setup](https://tokio.rs/tokio/tutorial/setup) - Installing and configuring Tokio
- [Hello Tokio](https://tokio.rs/tokio/tutorial/hello-tokio) - First async application
- [Spawning](https://tokio.rs/tokio/tutorial/spawning) - Spawning asynchronous tasks
- [Shared State](https://tokio.rs/tokio/tutorial/shared-state) - Sharing data between tasks
- [Channels](https://tokio.rs/tokio/tutorial/channels) - Message passing between tasks
- [I/O](https://tokio.rs/tokio/tutorial/io) - Asynchronous I/O operations
- [Framing](https://tokio.rs/tokio/tutorial/framing) - Parsing byte streams into frames
- [Async in Depth](https://tokio.rs/tokio/tutorial/async) - Understanding async/await internals
- [Select](https://tokio.rs/tokio/tutorial/select) - Waiting on multiple async operations
- [Streams](https://tokio.rs/tokio/tutorial/streams) - Asynchronous iteration

### Topics

- [Bridging with Sync Code](https://tokio.rs/tokio/topics/bridging) - Integrating async and sync code
- [Graceful Shutdown](https://tokio.rs/tokio/topics/shutdown) - Clean application shutdown
- [Getting Started with Tracing](https://tokio.rs/tokio/topics/tracing) - Instrumentation basics
- [Next Steps with Tracing](https://tokio.rs/tokio/topics/tracing-next-steps) - Advanced tracing
- [Unit Testing](https://tokio.rs/tokio/topics/testing) - Testing async code

### Core Modules

- [tokio::task](https://docs.rs/tokio/latest/tokio/task/) - Asynchronous task management
  - `spawn()` - Spawn tasks on the runtime
  - `JoinHandle` - Task completion handle
  - `spawn_blocking()` - Run blocking operations
  - `yield_now()` - Yield control to scheduler
- [tokio::sync](https://docs.rs/tokio/latest/tokio/sync/) - Synchronization primitives
  - `mpsc` - Multi-producer, single-consumer channel
  - `oneshot` - Single-value channel
  - `broadcast` - Multi-producer, multi-consumer channel
  - `watch` - Single-producer, multi-consumer channel
  - `Mutex` - Async mutex
  - `RwLock` - Async read-write lock
  - `Semaphore` - Async semaphore
  - `Barrier` - Async barrier
  - `Notify` - Async notification primitive
- [tokio::time](https://docs.rs/tokio/latest/tokio/time/) - Time utilities
  - `sleep()` - Asynchronous sleep
  - `timeout()` - Timeout for futures
  - `interval()` - Periodic timer
  - `Instant` - Time measurement
  - `Duration` - Time duration
- [tokio::net](https://docs.rs/tokio/latest/tokio/net/) - Asynchronous networking
  - `TcpListener` - TCP server socket
  - `TcpStream` - TCP client socket
  - `UdpSocket` - UDP socket
  - `UnixListener` - Unix domain socket listener
  - `UnixStream` - Unix domain socket stream
- [tokio::fs](https://docs.rs/tokio/latest/tokio/fs/) - Asynchronous filesystem operations
  - `File` - Async file handle
  - `read()` - Read file contents
  - `write()` - Write file contents
  - `read_dir()` - Directory iteration
- [tokio::io](https://docs.rs/tokio/latest/tokio/io/) - Core I/O traits
  - `AsyncRead` - Async reading
  - `AsyncWrite` - Async writing
  - `AsyncBufRead` - Buffered async reading
  - `AsyncReadExt` - Extension methods
  - `AsyncWriteExt` - Extension methods
- [tokio::process](https://docs.rs/tokio/latest/tokio/process/) - Child process management
  - `Command` - Process builder
  - `Child` - Running process handle
- [tokio::signal](https://docs.rs/tokio/latest/tokio/signal/) - OS signal handling
  - Unix signals (SIGTERM, SIGINT, etc.)
  - Windows Ctrl+C handling
- [tokio::runtime](https://docs.rs/tokio/latest/tokio/runtime/) - Runtime configuration
  - `Builder` - Runtime builder
  - `Runtime` - Runtime handle
  - Multi-threaded scheduler
  - Current-thread scheduler

### Macros

- [#[tokio::main]](https://docs.rs/tokio/latest/tokio/attr.main.html) - Main function macro for async runtime
- [#[tokio::test]](https://docs.rs/tokio/latest/tokio/attr.test.html) - Test macro for async tests
- [tokio::spawn!](https://docs.rs/tokio/latest/tokio/macro.spawn.html) - Spawn async tasks
- [tokio::select!](https://docs.rs/tokio/latest/tokio/macro.select.html) - Wait on multiple futures (first completion)
- [tokio::join!](https://docs.rs/tokio/latest/tokio/macro.join.html) - Wait on multiple futures (all complete)
- [tokio::try_join!](https://docs.rs/tokio/latest/tokio/macro.try_join.html) - Join with early error return

### Features

- **full** - Enable all features
- **rt** - Runtime (required)
- **rt-multi-thread** - Multi-threaded runtime
- **net** - Networking
- **io-util** - I/O utilities
- **time** - Time utilities
- **fs** - Filesystem
- **sync** - Synchronization primitives
- **signal** - Signal handling
- **process** - Process spawning
- **macros** - tokio::main and tokio::test
- **tracing** - Instrumentation support

### Additional Resources

- [Glossary](https://tokio.rs/tokio/glossary) - Term definitions
- [API Documentation](https://docs.rs/tokio) - Complete API reference
- [Discord Community](https://discord.gg/tokio) - Support and discussions
- [GitHub Discussions](https://github.com/tokio-rs/tokio/discussions) - Q&A and ideas

## Common Queries → Documentation

| Query/Task | Section | URL |
|------------|---------|-----|
| How do I get started? | Setup | https://tokio.rs/tokio/tutorial/setup |
| How do I spawn async tasks? | Spawning | https://tokio.rs/tokio/tutorial/spawning |
| How do I share data between tasks? | Shared State | https://tokio.rs/tokio/tutorial/shared-state |
| How do I use channels? | Channels | https://tokio.rs/tokio/tutorial/channels |
| How do I do async I/O? | I/O | https://tokio.rs/tokio/tutorial/io |
| How do I use select? | Select | https://tokio.rs/tokio/tutorial/select |
| How do I handle timeouts? | time module | https://docs.rs/tokio/latest/tokio/time/ |
| How do I test async code? | Unit Testing | https://tokio.rs/tokio/topics/testing |
| How do I shut down gracefully? | Graceful Shutdown | https://tokio.rs/tokio/topics/shutdown |
| How do I use TCP sockets? | net module | https://docs.rs/tokio/latest/tokio/net/ |
