# hyper - Fast HTTP for Rust

> Sources: https://hyper.rs/ | https://docs.rs/hyper/latest/hyper/ | https://github.com/hyperium/hyper

## Quick Reference

A fast and correct HTTP implementation for Rust. Low-level HTTP client and server library supporting HTTP/1, HTTP/2, with asynchronous design. Building block for web frameworks and applications.

## Table of Contents

### Getting Started

- [Official Guides](https://hyper.rs/guides/1/) - Complete guide collection
- [Initial Setup](https://hyper.rs/guides/1/init/setup/) - Installation and dependencies
- [Runtime Configuration](https://hyper.rs/guides/1/init/runtime/) - Async runtime setup with Tokio
- [Upgrading to v1.0](https://hyper.rs/guides/1/upgrading/) - Migration guide from v0.14

### Server Guides

- [Hello World Server](https://hyper.rs/guides/1/server/hello-world/) - Creating your first HTTP server
- [Echo Server](https://hyper.rs/guides/1/server/echo/) - Request/response echo implementation
- [Server Middleware](https://hyper.rs/guides/1/server/middleware/) - Middleware patterns and integration
- [Graceful Shutdown](https://hyper.rs/guides/1/server/graceful-shutdown/) - Proper server shutdown procedures

### Client Guides

- [Basic Client Usage](https://hyper.rs/guides/1/client/basic/) - Making HTTP requests
- [Connectors and Pools](https://hyper.rs/guides/1/client/connectors/) - Connection management, pooling, and HTTPS
- [Client POST Requests](https://hyper.rs/guides/1/client/post/) - Sending POST data

### Examples (GitHub)

**Basic Examples:**
- [hello.rs](https://github.com/hyperium/hyper/blob/master/examples/hello.rs) - Simple "Hello World" server
- [echo.rs](https://github.com/hyperium/hyper/blob/master/examples/echo.rs) - Echo server
- [client.rs](https://github.com/hyperium/hyper/blob/master/examples/client.rs) - CLI HTTP client
- [client_json.rs](https://github.com/hyperium/hyper/blob/master/examples/client_json.rs) - Client with JSON parsing

**Advanced Examples:**
- [gateway.rs](https://github.com/hyperium/hyper/blob/master/examples/gateway.rs) - Reverse proxy implementation
- [http_proxy.rs](https://github.com/hyperium/hyper/blob/master/examples/http_proxy.rs) - HTTP/HTTPS proxy with CONNECT
- [graceful_shutdown.rs](https://github.com/hyperium/hyper/blob/master/examples/graceful_shutdown.rs) - Server with graceful shutdown
- [upgrades.rs](https://github.com/hyperium/hyper/blob/master/examples/upgrades.rs) - WebSocket and protocol upgrades
- [state.rs](https://github.com/hyperium/hyper/blob/master/examples/state.rs) - Shared state across requests
- [multi_server.rs](https://github.com/hyperium/hyper/blob/master/examples/multi_server.rs) - Multiple listening ports
- [send_file.rs](https://github.com/hyperium/hyper/blob/master/examples/send_file.rs) - Async file serving
- [params.rs](https://github.com/hyperium/hyper/blob/master/examples/params.rs) - Form parameter handling
- [web_api.rs](https://github.com/hyperium/hyper/blob/master/examples/web_api.rs) - Service-to-service calls
- [service_struct_impl.rs](https://github.com/hyperium/hyper/blob/master/examples/service_struct_impl.rs) - Manual Service trait implementation
- [single_threaded.rs](https://github.com/hyperium/hyper/blob/master/examples/single_threaded.rs) - Single-threaded server with !Send state

### API Documentation

**Core Modules:**
- [hyper::body](https://docs.rs/hyper/latest/hyper/body/) - Streaming request and response bodies
- [hyper::client](https://docs.rs/hyper/latest/hyper/client/) - HTTP client functionality
- [hyper::server](https://docs.rs/hyper/latest/hyper/server/) - HTTP server functionality
- [hyper::service](https://docs.rs/hyper/latest/hyper/service/) - Asynchronous service trait
- [hyper::upgrade](https://docs.rs/hyper/latest/hyper/upgrade/) - Protocol upgrade support
- [hyper::ext](https://docs.rs/hyper/latest/hyper/ext/) - HTTP message extensions
- [hyper::rt](https://docs.rs/hyper/latest/hyper/rt/) - Runtime components (Executor, Timer)
- [hyper::ffi](https://docs.rs/hyper/latest/hyper/ffi/) - C API bindings for FFI

**Key Types:**
- [Request](https://docs.rs/hyper/latest/hyper/struct.Request.html) - HTTP request
- [Response](https://docs.rs/hyper/latest/hyper/struct.Response.html) - HTTP response
- [Error](https://docs.rs/hyper/latest/hyper/struct.Error.html) - Error type
- [Method](https://docs.rs/hyper/latest/hyper/struct.Method.html) - HTTP methods (GET, POST, etc.)
- [StatusCode](https://docs.rs/hyper/latest/hyper/struct.StatusCode.html) - HTTP status codes
- [HeaderMap](https://docs.rs/hyper/latest/hyper/struct.HeaderMap.html) - HTTP headers
- [Uri](https://docs.rs/hyper/latest/hyper/struct.Uri.html) - Request URI
- [Version](https://docs.rs/hyper/latest/hyper/struct.Version.html) - HTTP version (HTTP/1.1, HTTP/2)

### Additional Resources

- [GitHub Repository](https://github.com/hyperium/hyper) - Source code, issues, and discussions
- [v1.0 Release Announcement](https://seanmonstar.com/blog/hyper-v1) - Major release details
- [Contribution Guide](https://hyper.rs/contrib/) - How to contribute to hyper
- [Blog](https://hyper.rs/blog/) - Team announcements and updates

### Features & Configuration

- **http1** - HTTP/1 protocol support
- **http2** - HTTP/2 protocol support
- **client** - Client API
- **server** - Server API
- **ffi** - C API for foreign function interface
- **tracing** - Debug logging with tracing crate

## Common Queries → Documentation

| Query/Task | Documentation | URL |
|------------|---------------|-----|
| How do I get started? | Getting Started Guides | https://hyper.rs/guides/1/ |
| How do I set up dependencies? | Initial Setup | https://hyper.rs/guides/1/init/setup/ |
| How do I configure Tokio runtime? | Runtime Configuration | https://hyper.rs/guides/1/init/runtime/ |
| How do I create a simple server? | Hello World Server | https://hyper.rs/guides/1/server/hello-world/ |
| How do I make HTTP requests? | Basic Client | https://hyper.rs/guides/1/client/basic/ |
| How do I handle HTTPS connections? | Connectors and Pools | https://hyper.rs/guides/1/client/connectors/ |
| How do I send POST requests? | Client POST Guide | https://hyper.rs/guides/1/client/post/ |
| How do I add middleware? | Server Middleware | https://hyper.rs/guides/1/server/middleware/ |
| How do I shutdown gracefully? | Graceful Shutdown | https://hyper.rs/guides/1/server/graceful-shutdown/ |
| How do I upgrade protocols? | Upgrades Example | https://github.com/hyperium/hyper/blob/master/examples/upgrades.rs |
| How do I build a proxy? | Gateway/Proxy Examples | https://github.com/hyperium/hyper/blob/master/examples/gateway.rs |
| How do I share state? | State Example | https://github.com/hyperium/hyper/blob/master/examples/state.rs |
| How do I serve files? | Send File Example | https://github.com/hyperium/hyper/blob/master/examples/send_file.rs |
| How do I work with JSON? | Client JSON Example | https://github.com/hyperium/hyper/blob/master/examples/client_json.rs |
| What is the Service trait? | service module | https://docs.rs/hyper/latest/hyper/service/ |
| How do I work with request bodies? | body module | https://docs.rs/hyper/latest/hyper/body/ |
| How do I handle errors? | Error type | https://docs.rs/hyper/latest/hyper/struct.Error.html |
| How do I upgrade from v0.14? | Upgrading Guide | https://hyper.rs/guides/1/upgrading/ |
| What changed in v1.0? | Release Announcement | https://seanmonstar.com/blog/hyper-v1 |
