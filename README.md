<p align="center">
  <img src="./assets/keyflip-logo.png" alt="KeyFlip logo" width="600" />
</p>

# KeyFlip

[![Copr build status](https://copr.fedorainfracloud.org/coprs/mikachu/keyflip/package/keyflip/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/mikachu/keyflip/package/keyflip/)

**A GNOME utility for safely enabling and disabling your laptop's built-in keyboard without affecting external keyboards.**

KeyFlip started from a simple problem: when a laptop is used like a desktop, the built-in keyboard can become something you accidentally press, cover, or need to clean. KeyFlip turns that into a deliberate, reversible mode instead of a terminal command you have to remember.

**Current version:** `0.2.0-beta`

---

## What it does

- 💻 **Laptop Mode** — keeps the internal keyboard enabled
- ⌨️ **Desk Mode** — disables the internal keyboard while external keyboards remain available
- 🧹 **Cleaning Mode** — temporarily blocks keyboard input for 60 seconds while keeping the mouse or trackpad usable
- ⚡ **Global shortcut** — `Super + Shift + K` toggles Laptop/Desk Mode
- 🔌 **Automatic switching** — optionally enters Desk Mode when a USB or Bluetooth keyboard connects
- 🛡️ **Safety checks** — warns before disabling the internal keyboard when no external keyboard is detected
- 🖥️ **GNOME panel controls** — change modes without reopening the app
- 🪟 **Wayland + X11 support**

Panel controls, automatic switching, and the global shortcut continue working while the main KeyFlip window is closed.

---

## Install on Fedora

```bash
sudo dnf copr enable mikachu/keyflip
sudo dnf install keyflip
```

Then launch **KeyFlip** from the applications menu or run:

```bash
keyflip
```

If the GNOME panel integration does not appear after the first install, log out and back in. You can also enable the extension manually:

```bash
gnome-extensions enable keyflip@miflow13.github.io
```

---

## Screenshots

<img width="1920" alt="KeyFlip main window" src="https://github.com/user-attachments/assets/f43d125f-4547-4a41-83c9-76d11ffc778d" />

<img width="1920" alt="KeyFlip settings" src="https://github.com/user-attachments/assets/f9233967-490a-4506-992e-ba2315ce6e88" />

---

## Compatibility

KeyFlip is developed and tested primarily on **Fedora + GNOME**.

| Feature | Support |
| --- | --- |
| Fedora | ✅ |
| GNOME | ✅ |
| Wayland | ✅ |
| X11 | ✅ |
| i8042 / AT internal keyboards | ✅ |
| External USB keyboards | ✅ Remain enabled |
| Bluetooth keyboards | ✅ Remain enabled |
| Internal USB keyboards | ❌ Not yet supported |
| Internal I2C keyboards | ❌ Not yet supported |

The included GNOME extension currently targets **GNOME Shell 50**.

### Runtime dependencies

- Python 3
- GTK4 / `python3-gobject`
- `polkit`
- `util-linux`
- `systemd`
- `python3-evdev` on Fedora or `python-evdev` on Arch for Cleaning Mode

---

## How the modes work

### Laptop Mode

The built-in laptop keyboard works normally.

### Desk Mode

KeyFlip disables supported internal laptop keyboards while leaving USB and Bluetooth keyboards available. Use this when the laptop is being used more like a desktop or an external keyboard sits over or near the built-in one.

### Cleaning Mode

Cleaning Mode temporarily blocks keyboard input for **60 seconds** so the keyboard can be cleaned without triggering shortcuts or accidental typing. The mouse and trackpad remain usable, and **End Cleaning** restores input immediately.

<details>
<summary><strong>Cleaning Mode technical details</strong></summary>

Release any held keys before starting Cleaning Mode.

Cleaning temporarily pauses panel controls and automatic mode switching while preserving the previous Laptop/Desk Mode. If the internal keyboard was disabled before cleaning, it remains disabled afterward.

For devices that combine keyboard and pointer input on one event endpoint, KeyFlip attempts to filter keyboard events while forwarding pointer input. If this cannot be configured safely, Cleaning Mode stops instead of leaving only part of the keyboard set blocked.

New input devices are checked approximately every 100 ms during cleaning.

</details>

---

## Automatic keyboard detection

KeyFlip can automatically switch to Desk Mode when a USB or Bluetooth keyboard connects. When the last external keyboard disconnects, it can return to Laptop Mode.

Automatic switching is configurable from the main application.

## Global shortcut

With the GNOME extension enabled:

```text
Super + Shift + K
```

switches between Laptop Mode and Desk Mode from anywhere in GNOME.

To change it:

```bash
gsettings set io.github.miflow13.KeyFlip toggle-mode-shortcut "['<Super><Shift>j']"
```

Disable it:

```bash
gsettings set io.github.miflow13.KeyFlip toggle-mode-shortcut "[]"
```

Restore the default:

```bash
gsettings reset io.github.miflow13.KeyFlip toggle-mode-shortcut
```

---

## Manual installation

Download and extract:

```text
keyflip-0.2.0-beta.tar.gz
```

From the extracted directory:

```bash
sudo ./install.sh
```

This installs the GTK application, GNOME Shell extension, panel controls, global shortcut, and keyboard-control helper.

For Cleaning Mode on Fedora:

```bash
sudo dnf install python3-evdev
```

Combined keyboard/pointer devices also require `/dev/uinput`.

### Uninstall

From the source directory:

```bash
sudo ./uninstall.sh
```

Or remove the Fedora package:

```bash
sudo dnf remove keyflip
```

Optionally remove the COPR repository:

```bash
sudo dnf copr remove mikachu/keyflip
```

---

## Development and packaging

Create a source package with:

```bash
make package
```

This validates the source and creates:

```text
dist/keyflip-0.2.0-beta.tar.gz
```

Development validation uses tools including Node.js, `desktop-file-validate`, `appstreamcli`, and `glib-compile-schemas`; these are not required simply to run an installed copy.

### Arch

Place the source archive beside `packaging/arch/PKGBUILD`, then run:

```bash
updpkgsums
makepkg
```

### RPM

Place the source archive in the RPM `SOURCES` directory and build using:

```text
packaging/obs/keyflip.spec
```

---

## Engineering notes

KeyFlip combines a GTK4 application, GNOME Shell integration, system-level keyboard control, device detection, persistent settings, and safety fallbacks. The project is intentionally conservative around input-device changes: when KeyFlip cannot determine that a transition is safe, it prefers not to disable input.

## AI-assisted development

KeyFlip was developed with help from AI tools for coding, debugging, documentation, and learning. I review, test, modify, and take responsibility for everything released in this project.

---

## Status

KeyFlip is still in active development. Bug reports, hardware compatibility reports, and feature suggestions are welcome.
