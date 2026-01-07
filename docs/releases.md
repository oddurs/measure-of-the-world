# Releases

This document explains how releases work for *The Measure of the World*.

## Overview

Releases are automated via GitHub Actions. When you push a version tag (e.g., `v1.0.0`), the workflow automatically:

1. Builds the PDF from source
2. Creates a GitHub Release
3. Attaches the compiled PDF as a downloadable asset
4. Generates release notes from commit history

## Creating a Release

### 1. Ensure the build is clean

Before tagging, verify the document builds without errors:

```bash
make build
```

Check for:
- No undefined references (warnings shown in build output)
- No undefined citations (build will fail if present)

### 2. Tag the release

Use semantic versioning (`vMAJOR.MINOR.PATCH`):

```bash
git tag -a v1.0.0 -m "Release v1.0.0: Description of release"
git push origin v1.0.0
```

### 3. Monitor the workflow

The release workflow will trigger automatically. Monitor progress at:
`https://github.com/<owner>/measure-of-the-world/actions`

Once complete, the release will appear at:
`https://github.com/<owner>/measure-of-the-world/releases`

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):

| Version | When to use |
|---------|-------------|
| `v0.x.x` | Pre-publication drafts |
| `v1.0.0` | First complete manuscript |
| `vX.Y.0` | Significant content additions (new chapters, major revisions) |
| `vX.Y.Z` | Minor corrections, typo fixes, formatting improvements |

### Examples

- `v0.1.0` – Initial draft with first few chapters
- `v0.5.0` – Halfway milestone, chapters 1-12 complete
- `v1.0.0` – Complete first edition
- `v1.0.1` – Typo corrections
- `v1.1.0` – Added new appendix

## Draft Releases

For pre-release versions (not ready for general distribution), use the `-draft` suffix:

```bash
git tag -a v0.5.0-draft -m "Draft: Chapters 1-12 complete"
git push origin v0.5.0-draft
```

GitHub will mark these as pre-releases automatically.

## Workflow Details

The release workflow is defined in `.github/workflows/release.yml`:

- **Trigger**: Push of tags matching `v*`
- **Environment**: Ubuntu with TeX Live Full
- **Build command**: `make build`
- **Output**: `build/out/measure-of-the-world.pdf`
- **Release notes**: Auto-generated from commits since last tag

## Deleting a Tag

If you need to remove a tag (e.g., tagged prematurely):

```bash
# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin :refs/tags/v1.0.0
```

Then delete the corresponding release on GitHub if one was created.

## Manual Releases

If automation fails, you can create a release manually:

1. Build locally: `make build`
2. Go to GitHub → Releases → "Draft a new release"
3. Create or select a tag
4. Upload `build/out/measure-of-the-world.pdf`
5. Write release notes and publish
