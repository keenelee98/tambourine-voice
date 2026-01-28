# Releasing Tambourine

This document covers the release process for maintainers.

## Building for Distribution

### macOS Universal Binary

To build a `.dmg` that runs on both Intel and Apple Silicon Macs:

```bash
# One-time setup: add Intel target
rustup target add x86_64-apple-darwin

# Build universal binary
cd app
pnpm tauri build --target universal-apple-darwin
```

**Output:** `app/src-tauri/target/universal-apple-darwin/release/bundle/dmg/Tambourine_<version>_universal.dmg`

### Platform-Specific Builds

For single-architecture builds (smaller file size, current platform only):

```bash
cd app
pnpm tauri build
```

**Output locations:**
- macOS: `app/src-tauri/target/release/bundle/dmg/`
- Windows: `app/src-tauri/target/release/bundle/msi/`
- Linux: `app/src-tauri/target/release/bundle/appimage/`
