# Fedora Package Review request draft

Use this as the basis for KeyFlip's Fedora Package Review request after the spec and SRPM are hosted at stable, directly downloadable URLs.

## Summary

**Package:** `keyflip`

**Summary:** GNOME utility for controlling a laptop's internal keyboard

**Description:**

KeyFlip is a GNOME utility for safely enabling and disabling supported laptop internal keyboards while keeping external USB and Bluetooth keyboards active. It provides Laptop and Desk modes, automatic external-keyboard detection, safety checks, and a reversible privileged helper for supported i8042/AT internal keyboards.

The source package also builds `gnome-shell-extension-keyflip`, which provides the GNOME Shell panel controls, global keyboard shortcut, and automatic mode switching integration.

## Review request fields

- **Spec URL:** `<DIRECT-HTTPS-URL-TO-keyflip.spec>`
- **SRPM URL:** `<DIRECT-HTTPS-URL-TO-keyflip-0.2.0-0.1.beta.src.rpm>`
- **Upstream URL:** https://github.com/miflow13/KeyFlip
- **Upstream release:** https://github.com/miflow13/KeyFlip/releases/tag/v0.2.0-beta
- **License:** MIT
- **Build architecture:** noarch

## Notes for reviewer

This is my first Fedora package submission, so I am seeking a Fedora packager sponsor as part of the review process.

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

Replace the two placeholder URLs above with stable direct-download URLs for the exact spec and SRPM being reviewed. Keep the review request updated whenever either file changes so the reviewer is always evaluating the current pair.
