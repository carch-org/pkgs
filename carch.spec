Name:           carch
Version:        5.2.4 
Release:        1%{?dist}
Summary:        A simple Rust-based CLI tool (built with Ratatui) to streamline and automate your Linux system’s initial setup. 
License:        MIT 
URL:            https://github.com/harilvfs/%{name}
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo

Requires:       bash
Requires:       man
Requires:       man-pages
Requires:       git
Requires:       wget
Requires:       curl

Suggests:       bash-completion-devel

%description
Carch is a simple CLI tool to help automating linux system setups. It provides a convenient way to install and
configure packages and system settings.

%prep
%autosetup -p1

%build
export CARGO_TARGET_DIR=build
cargo build --frozen --release --all-features

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d

install -Dm755 build/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
install -Dm644 .github/README.md %{buildroot}%{_datadir}/doc/%{name}/README.md

echo "Version=%{version}" >> %{name}.desktop
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm644 completions/bash/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 completions/zsh/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 completions/fish/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

for size in 16 24 32 48 64 128 256; do
    install -Dm644 assets/icons/carch_logo_${size}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Wed Jul 23 2025 Your Name <harilvfs@chalisehari.com.np> - 5.2.4-1
- Refer to the full changelog: https://github.com/harilvfs/carch/blob/main/CHANGELOG.md
