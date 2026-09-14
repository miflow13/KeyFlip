# Fedora package review preparation

This directory contains the Fedora-oriented RPM spec for proposing KeyFlip to the official Fedora repositories.

## Current upstream release

- Upstream release: `v0.2.0-beta`
- Fedora version: `0.2.0-0.1.beta`
- Release archive: `keyflip-0.2.0-beta.tar.gz`
- SHA-256: `f6f8d4494e8b30de0599713453a6cf6ad289d854f9ff85e3bec448d78062175a`

The Fedora spec intentionally separates the GNOME Shell integration into the `gnome-shell-extension-keyflip` binary subpackage while keeping the GTK application, keyboard helper, recovery service, polkit policy, and shared resources in `keyflip`.

## Local review build on Fedora

Install the review tooling:

```bash
sudo dnf install fedora-review mock rpmdevtools rpmlint
```

Create the RPM build tree and download the exact upstream release archive:

```bash
rpmdev-setuptree
cp packaging/fedora/keyflip.spec ~/rpmbuild/SPECS/
curl -L \
  https://github.com/miflow13/KeyFlip/releases/download/v0.2.0-beta/keyflip-0.2.0-beta.tar.gz \
  -o ~/rpmbuild/SOURCES/keyflip-0.2.0-beta.tar.gz
sha256sum ~/rpmbuild/SOURCES/keyflip-0.2.0-beta.tar.gz
```

Build the source RPM:

```bash
rpmbuild -bs ~/rpmbuild/SPECS/keyflip.spec
```

Then build it in a clean Fedora environment with `mock` and inspect the result with `rpmlint`. The exact mock target should match the Fedora release or Rawhide target being proposed.

## Fedora review path

Before submitting:

1. Confirm the SRPM builds successfully in a clean `mock` environment.
2. Run `rpmlint` on the spec, SRPM, and built RPMs.
3. Run `fedora-review` locally where practical and address actionable failures.
4. Create/sign in to a Fedora Account and complete the Fedora contributor prerequisites.
5. File a new Fedora Package Review request with direct URLs to the spec and SRPM.
6. If this is the first Fedora package being maintained by the submitter, mark the review as needing a sponsor.
7. Work through reviewer feedback until the package is approved, then request/import the Fedora dist-git package and build it through Fedora infrastructure.

Do not treat the upstream GitHub copy of this spec as Fedora dist-git. Once accepted, Fedora's package repository becomes the packaging source of truth for official builds, while this copy remains useful as an upstream reference.
