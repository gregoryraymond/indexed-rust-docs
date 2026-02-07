# Tauri v2 Documentation

> Source: https://v2.tauri.app/

## Quick Reference

Build smaller, faster, and more secure desktop and mobile applications with Rust-powered web frontend framework. Cross-platform native apps using web technologies.

## Table of Contents

### Getting Started

- [Quick Start](https://v2.tauri.app/start/) - Prerequisites and project setup
- [Prerequisites](https://v2.tauri.app/start/prerequisites/) - System requirements and dependencies
- [Create a Project](https://v2.tauri.app/start/create-project/) - Initializing new Tauri projects
- [Frontend Configuration](https://v2.tauri.app/start/frontend/) - Configuring web frameworks
  - [Leptos](https://v2.tauri.app/start/frontend/leptos/) - Leptos integration
  - [Next.js](https://v2.tauri.app/start/frontend/nextjs/) - Next.js setup
  - [Nuxt](https://v2.tauri.app/start/frontend/nuxt/) - Nuxt.js configuration
  - [Qwik](https://v2.tauri.app/start/frontend/qwik/) - Qwik framework
  - [SvelteKit](https://v2.tauri.app/start/frontend/sveltekit/) - SvelteKit integration
  - [Trunk](https://v2.tauri.app/start/frontend/trunk/) - Trunk for Rust frontends
  - [Vite](https://v2.tauri.app/start/frontend/vite/) - Vite build tool
- [Upgrade & Migration](https://v2.tauri.app/start/upgrade/) - Migrating from v1 to v2

### Core Concepts

- [Architecture](https://v2.tauri.app/concept/architecture/) - Understanding Tauri's architecture
- [Process Model](https://v2.tauri.app/concept/process-model/) - Multi-process architecture
- [App Size](https://v2.tauri.app/concept/size/) - Optimizing application size
- [Inter-Process Communication](https://v2.tauri.app/concept/ipc/) - Frontend-Backend communication
  - [Brownfield Pattern](https://v2.tauri.app/concept/brownfield/) - Integrating into existing apps
  - [Isolation Pattern](https://v2.tauri.app/concept/isolation/) - Security isolation

### Security

- [Security Overview](https://v2.tauri.app/security/) - Security best practices
- [Permissions](https://v2.tauri.app/security/permissions/) - Permission system
- [Command Scopes](https://v2.tauri.app/security/scopes/) - Restricting command access
- [Capabilities](https://v2.tauri.app/security/capabilities/) - Fine-grained capabilities
- [Content Security Policy](https://v2.tauri.app/security/csp/) - CSP configuration
- [HTTP Headers](https://v2.tauri.app/security/headers/) - Security headers
- [Lifecycle Threats](https://v2.tauri.app/security/threats/) - Security threat model

### Development

- [Configuration](https://v2.tauri.app/develop/configuration/) - App configuration files
- [Calling Frontend from Rust](https://v2.tauri.app/develop/calling-frontend/) - Backend to frontend communication
- [Calling Rust from Frontend](https://v2.tauri.app/develop/calling-rust/) - Frontend to backend calls
- [Resources](https://v2.tauri.app/develop/resources/) - Embedding resources
- [Binary Embedding](https://v2.tauri.app/develop/sidecar/) - Bundling external binaries
- [State Management](https://v2.tauri.app/develop/state-management/) - Managing application state
- [Debugging](https://v2.tauri.app/develop/debug/) - Debugging tools
  - [VS Code](https://v2.tauri.app/develop/debug/vscode/) - Visual Studio Code debugging
  - [JetBrains IDEs](https://v2.tauri.app/develop/debug/jetbrains/) - IntelliJ, WebStorm, etc.
  - [Neovim](https://v2.tauri.app/develop/debug/neovim/) - Neovim debugging
  - [DevTools](https://v2.tauri.app/develop/debug/devtools/) - CrabNebula DevTools
- [Plugin Development](https://v2.tauri.app/develop/plugins/) - Creating Tauri plugins
- [Testing](https://v2.tauri.app/develop/tests/) - Testing frameworks

### Distribution

- [App Store](https://v2.tauri.app/distribute/appstore/) - Publishing to app stores
- [AppImage](https://v2.tauri.app/distribute/appimage/) - Linux AppImage packaging
- [AUR](https://v2.tauri.app/distribute/aur/) - Arch User Repository
- [Signing](https://v2.tauri.app/distribute/sign/) - Code signing for all platforms
- [CI/CD](https://v2.tauri.app/distribute/ci/) - Continuous integration
  - [GitHub Actions](https://v2.tauri.app/distribute/ci/github/) - GitHub CI/CD
  - [CrabNebula Cloud](https://v2.tauri.app/distribute/ci/crabnebula/) - Managed CI/CD

### Plugins

- [Official Plugins](https://v2.tauri.app/plugin/) - 30+ available plugins
  - [Clipboard](https://v2.tauri.app/plugin/clipboard/) - Clipboard access
  - [Dialog](https://v2.tauri.app/plugin/dialog/) - Native dialogs
  - [HTTP](https://v2.tauri.app/plugin/http/) - HTTP client
  - [Notifications](https://v2.tauri.app/plugin/notification/) - System notifications
  - [SQL](https://v2.tauri.app/plugin/sql/) - Database access
  - [WebSocket](https://v2.tauri.app/plugin/websocket/) - WebSocket support

### Reference

- [CLI Reference](https://v2.tauri.app/reference/cli/) - Command line interface
- [API Documentation](https://v2.tauri.app/reference/api/) - Complete API reference

### Learning

- [Tutorials](https://v2.tauri.app/learn/) - Practical guides
  - [Sidecars](https://v2.tauri.app/learn/sidecar/) - External process integration
  - [Splashscreens](https://v2.tauri.app/learn/splashscreen/) - Loading screens
  - [System Tray](https://v2.tauri.app/learn/system-tray/) - Tray icons
  - [Window Customization](https://v2.tauri.app/learn/window-customization/) - Custom windows

## Common Queries → Documentation

| Query/Task | Section | URL |
|------------|---------|-----|
| How do I get started? | Quick Start | https://v2.tauri.app/start/ |
| How do I call Rust from JavaScript? | Calling Rust from Frontend | https://v2.tauri.app/develop/calling-rust/ |
| How do I call JavaScript from Rust? | Calling Frontend from Rust | https://v2.tauri.app/develop/calling-frontend/ |
| How do I configure my app? | Configuration | https://v2.tauri.app/develop/configuration/ |
| How do I handle permissions? | Permissions | https://v2.tauri.app/security/permissions/ |
| How do I sign my app? | Signing | https://v2.tauri.app/distribute/sign/ |
| How do I build for production? | Distribution | https://v2.tauri.app/distribute/ |
| How do I debug my app? | Debugging | https://v2.tauri.app/develop/debug/ |
| How do I use plugins? | Plugins | https://v2.tauri.app/plugin/ |
| How do I migrate from v1? | Upgrade & Migration | https://v2.tauri.app/start/upgrade/ |
