# Fedora Package Review request draft

Use this as the basis for KeyFlip's Fedora Package Review request after the SRPM is hosted at a stable, directly downloadable URL.

## Summary

**Package:** `keyflip`

**Summary:** GNOME utility for controlling a laptop's internal keyboard

**Description:**

KeyFlip is a GNOME utility for safely enabling and disabling supported laptop internal keyboards while keeping external USB and Bluetooth keyboards active. It provides Laptop and Desk modes, automatic external-keyboard detection, safety checks, and a reversible privileged helper for supported i8042/AT internal keyboards.

The source package also builds `gnome-shell-extension-keyflip`, which provides the GNOME Shell panel controls, global keyboard shortcut, and automatic mode switching integration.

## Review request fields

- **FAS username:** `mikachu13`
- **Spec URL:** https://raw.githubusercontent.com/miflow13/KeyFlip/e9942c5de39bab74b93335a070c4db346f042119/packaging/fedora/keyflip.spec
- **SRPM URL:** `<DIRECT-HTTPS-URL-TO-keyflip-0.2.0-0.1.beta.fc46.src.rpm>`
- **Upstream URL:** https://github.com/miflow13/KeyFlip
- **Upstream release:** https://github.com/miflow13/KeyFlip/releases/tag/v0.2.0-beta
- **License:** MIT
- **Build architecture:** noarch

## Notes for reviewer

This is my first Fedora package submission, so I am seeking a Fedora packager sponsor as part of the review process. The review request should block `FE-NEEDSPONSOR`.

The package has been test-built against Fedora Rawhide in upstream CI from the immutable `v0.2.0-beta` release archive. The build validates the desktop file, AppStream metadata, GSettings schema, Python sources, and shell scripts before producing the SRPM and binary RPMs.

The GNOME Shell integration is split into the conventionally named `gnome-shell-extension-keyflip` subpackage. The main `keyflip` package recommends that subpackage so users get the desktop integration by default while keeping package ownership clear.

The published beta archive contains stale upstream repository URLs in AppStream metadata. The Fedora package carries `0001-fix-appstream-urls.patch` to backport the already-fixed upstream metadata from the development branch.

### rpmlint

Current Rawhide CI result:

```text
keyflip.noarch: W: no-manual-page-for-binary keyflip
3 packages and 1 specfiles checked; 0 errors, 1 warnings, 12 filtered, 0 badness
```

The remaining warning is non-fatal. KeyFlip currently documents its command usage in the upstream README rather than a dedicated man page. A man page can be added upstream in a future release if requested during review.

## Before filing

1. Download the `keyflip-fedora-review` artifact from the latest successful `Fedora package review prep` GitHub Actions run.
2. Extract `keyflip-0.2.0-0.1.beta.fc46.src.rpm`.
3. Host that SRPM at a stable, publicly accessible direct-download URL. A dedicated GitHub prerelease such as `fedora-review-0.2.0-beta-1` is suitable; clearly label it as Fedora review material rather than an end-user release.
4. Replace the SRPM placeholder above with the direct asset URL.
5. File the Fedora Package Review request using the fields and notes above and block `FE-NEEDSPONSOR`.

The SPEC URL above is pinned to the exact Git commit used for the successful Rawhide review build, so it should remain immutable for this review revision.
