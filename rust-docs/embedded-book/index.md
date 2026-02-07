# The Embedded Rust Book

> Source: https://docs.rust-embedded.org/book/

## Quick Reference

Comprehensive guide to embedded systems programming with Rust. Covers bare-metal development, hardware interaction, debugging tools, and embedded-specific patterns for microcontrollers.

## Table of Contents

- [Introduction](https://docs.rust-embedded.org/book/intro/index.html) - Who this book is for and prerequisites
- [Meet Your Hardware](https://docs.rust-embedded.org/book/intro/hardware.html) - STM32F3DISCOVERY board overview
- [A `no_std` Rust Environment](https://docs.rust-embedded.org/book/intro/no-std.html) - Understanding bare metal environments
  - [Hosted Environments](https://docs.rust-embedded.org/book/intro/no-std.html#hosted-environments) - Standard library usage
  - [Bare Metal Environments](https://docs.rust-embedded.org/book/intro/no-std.html#bare-metal-environments) - Programming without OS
- [Tooling](https://docs.rust-embedded.org/book/intro/tooling.html) - Essential embedded Rust tools
  - [cargo-generate](https://docs.rust-embedded.org/book/intro/tooling.html#cargo-generate-or-git) - Project templates
  - [cargo-binutils](https://docs.rust-embedded.org/book/intro/tooling.html#cargo-binutils) - Binary inspection tools
  - [qemu-system-arm](https://docs.rust-embedded.org/book/intro/tooling.html#qemu-system-arm) - ARM emulation
- [Debugging Tools](https://docs.rust-embedded.org/book/intro/debugging-tools.html) - Tools for embedded debugging
  - [Probe-rs](https://docs.rust-embedded.org/book/intro/debugging-tools.html#probe-rs) - Modern Rust debugging tool
  - [OpenOCD](https://docs.rust-embedded.org/book/intro/debugging-tools.html#openocd) - On-chip debugger
  - [GDB](https://docs.rust-embedded.org/book/intro/debugging-tools.html#gdb) - GNU debugger
  - [Hardware Probes](https://docs.rust-embedded.org/book/intro/debugging-tools.html#probes) - ST-Link, J-Link, Rusty-probe
- [Installing the Tools](https://docs.rust-embedded.org/book/intro/install.html) - Platform-specific installation guides
  - [Linux](https://docs.rust-embedded.org/book/intro/install/linux.html) - Linux setup
  - [macOS](https://docs.rust-embedded.org/book/intro/install/macos.html) - macOS setup
  - [Windows](https://docs.rust-embedded.org/book/intro/install/windows.html) - Windows setup
- [Verify Installation](https://docs.rust-embedded.org/book/intro/install/verify.html) - Testing your setup
- [Getting Started](https://docs.rust-embedded.org/book/start/index.html) - First embedded program
  - [QEMU](https://docs.rust-embedded.org/book/start/qemu.html) - Emulator-based development
  - [Hardware](https://docs.rust-embedded.org/book/start/hardware.html) - Real hardware deployment
- [Memory Mapped Registers](https://docs.rust-embedded.org/book/start/registers.html) - Hardware register access
  - [Using PAC](https://docs.rust-embedded.org/book/start/registers.html#using-a-peripheral-access-crate-pac) - Peripheral Access Crates
  - [Using HAL](https://docs.rust-embedded.org/book/start/registers.html#using-a-hal-crate) - Hardware Abstraction Layers
- [Semihosting](https://docs.rust-embedded.org/book/start/semihosting.html) - Debug I/O for embedded systems
- [Panicking](https://docs.rust-embedded.org/book/start/panicking.html) - Handling panics in no_std
- [Exceptions](https://docs.rust-embedded.org/book/start/exceptions.html) - ARM Cortex-M exception handling
  - [Hard Fault Handler](https://docs.rust-embedded.org/book/start/exceptions.html#the-hard-fault-handler) - Critical fault handling
- [Interrupts](https://docs.rust-embedded.org/book/start/interrupts.html) - Interrupt handling in embedded Rust
- [IO](https://docs.rust-embedded.org/book/start/io.html) - Input/output operations
- [Peripherals](https://docs.rust-embedded.org/book/peripherals/index.html) - Working with microcontroller peripherals
  - [Memory Spaces](https://docs.rust-embedded.org/book/peripherals/index.html#linear-and-real-memory-space) - Understanding memory layout

## Common Queries → Documentation

| Query/Task | Section | URL |
|------------|---------|-----|
| How do I set up embedded Rust? | Installing the Tools | https://docs.rust-embedded.org/book/intro/install.html |
| What hardware do I need? | Meet Your Hardware | https://docs.rust-embedded.org/book/intro/hardware.html |
| How do I debug embedded code? | Debugging Tools | https://docs.rust-embedded.org/book/intro/debugging-tools.html |
| What is no_std? | no_std Environment | https://docs.rust-embedded.org/book/intro/no-std.html |
| How do I access hardware registers? | Memory Mapped Registers | https://docs.rust-embedded.org/book/start/registers.html |
| How do I handle interrupts? | Interrupts | https://docs.rust-embedded.org/book/start/interrupts.html |
| How do I handle panics? | Panicking | https://docs.rust-embedded.org/book/start/panicking.html |
| What is semihosting? | Semihosting | https://docs.rust-embedded.org/book/start/semihosting.html |
| How do I use QEMU? | QEMU | https://docs.rust-embedded.org/book/start/qemu.html |
| What are PACs and HALs? | Memory Mapped Registers | https://docs.rust-embedded.org/book/start/registers.html |
