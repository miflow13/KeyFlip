%global prerelease beta

Name:           keyflip
Version:        0.2.0
Release:        0.1.%{prerelease}%{?dist}
Summary:        GNOME utility for controlling a laptop's internal keyboard

License:        MIT
URL:            https://github.com/miflow13/KeyFlip
Source0:        https://github.com/miflow13/KeyFlip/releases/download/v%{version}-%{prerelease}/keyflip-%{version}-%{prerelease}.tar.gz
Patch0:         0001-fix-appstream-urls.patch

BuildArch:      noarch
BuildRequires:  appstream
BuildRequires:  bash
BuildRequires:  desktop-file-utils
BuildRequires:  glib2
BuildRequires:  python3

Requires:       bash
Requires:       glib2
Requires:       gtk4
Requires:       libcanberra
Requires:       polkit
Requires:       python3
Requires:       python3-gobject
Requires:       systemd
Requires:       systemd-udev
Requires:       util-linux
Recommends:     gnome-shell-extension-keyflip = %{version}-%{release}

%description
KeyFlip is a GNOME utility for safely enabling and disabling supported laptop
internal keyboards while keeping external USB and Bluetooth keyboards active.
It provides Laptop and Desk modes, automatic external-keyboard detection,
safety checks, and a reversible privileged helper for supported i8042/AT
internal keyboards.

%package -n gnome-shell-extension-keyflip
Summary:        GNOME Shell integration for KeyFlip
Requires:       gnome-shell
Requires:       keyflip = %{version}-%{release}

%description -n gnome-shell-extension-keyflip
GNOME Shell integration for KeyFlip, providing panel controls, a global
keyboard shortcut, and automatic mode switching while the main KeyFlip window
is closed.

%prep
%autosetup -n keyflip-%{version}-%{prerelease} -p1
sed -i 's|Exec=/usr/local/bin/keyflip|Exec=keyflip|' \
    packaging/io.github.miflow13.KeyFlip.desktop
sed -i 's|https://github.com/miflow13/KeyFlip-|https://github.com/miflow13/KeyFlip|g' \
    gnome-extension/metadata.json

%build
# KeyFlip is implemented in interpreted Python, JavaScript, and shell code.

%install
# Shared keyboard-control helper and settings.
install -Dm755 keyflip-helper \
    %{buildroot}%{_libexecdir}/keyflip/keyflip-helper
install -Dm644 packaging/io.github.miflow13.KeyFlip.policy \
    %{buildroot}%{_datadir}/polkit-1/actions/io.github.miflow13.KeyFlip.policy
install -Dm644 packaging/io.github.miflow13.KeyFlip.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/io.github.miflow13.KeyFlip.gschema.xml
install -Dm644 assets/sounds/toggle-on.ogg \
    %{buildroot}%{_datadir}/keyflip/sounds/toggle-on.ogg
install -Dm644 assets/sounds/toggle-off.ogg \
    %{buildroot}%{_datadir}/keyflip/sounds/toggle-off.ogg

# GTK application.
install -Dm644 app.py %{buildroot}%{_libexecdir}/keyflip/app.py
install -Dm644 keyflip_app.py %{buildroot}%{_libexecdir}/keyflip/keyflip_app.py
install -Dm755 keyflip %{buildroot}%{_bindir}/keyflip
install -Dm644 assets/keyflip.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/io.github.miflow13.KeyFlip.png
install -Dm644 packaging/io.github.miflow13.KeyFlip.desktop \
    %{buildroot}%{_datadir}/applications/io.github.miflow13.KeyFlip.desktop
install -Dm644 packaging/io.github.miflow13.KeyFlip.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/io.github.miflow13.KeyFlip.metainfo.xml

# GNOME Shell extension.
extension_dir=%{buildroot}%{_datadir}/gnome-shell/extensions/keyflip@miflow13.github.io
install -d "$extension_dir"
install -m644 gnome-extension/extension.js gnome-extension/metadata.json \
    gnome-extension/stylesheet.css gnome-extension/*.svg "$extension_dir/"

%check
desktop-file-validate packaging/io.github.miflow13.KeyFlip.desktop
appstreamcli validate --no-net packaging/io.github.miflow13.KeyFlip.metainfo.xml
glib-compile-schemas --strict --dry-run packaging
python3 -m compileall -q app.py keyflip_app.py
bash -n keyflip keyflip-helper

%files
%license LICENSE
%doc README.md
%{_bindir}/keyflip
%{_libexecdir}/keyflip/app.py
%{_libexecdir}/keyflip/keyflip_app.py
%{_libexecdir}/keyflip/keyflip-helper
%{_datadir}/applications/io.github.miflow13.KeyFlip.desktop
%{_datadir}/icons/hicolor/512x512/apps/io.github.miflow13.KeyFlip.png
%{_datadir}/keyflip/
%{_datadir}/metainfo/io.github.miflow13.KeyFlip.metainfo.xml
%{_datadir}/polkit-1/actions/io.github.miflow13.KeyFlip.policy
%{_datadir}/glib-2.0/schemas/io.github.miflow13.KeyFlip.gschema.xml

%files -n gnome-shell-extension-keyflip
%{_datadir}/gnome-shell/extensions/keyflip@miflow13.github.io/

%changelog
* Mon Sep 14 2026 Miflow13 <pizzafan513@gmail.com> - 0.2.0-0.1.beta
- Prepare KeyFlip for Fedora package review
- Split GNOME Shell integration into a conventionally named subpackage
