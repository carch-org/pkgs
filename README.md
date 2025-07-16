This repo is mainly dedicated to [Carch](https://github.com/harilvfs/carch) for building and installing the Carch package on Arch, Fedora, and openSUSE.

For building rpm package for fedora and opensuse. you can see the spec file that is used to build rpm package. For your info opensuse also support rpms so this will work for both fedora and opensuse.

## Arch Linux

For Arch, we provide a PKGBUILD that directly grabs the precompiled binary from the latest release.

You can install Carch using this PKGBUILD:

```sh
git clone https://github.com/carch-org/pkgs ~/pkgs
cd ~/pkgs/carch-bin
makepkg -si
```

## Fedora & openSUSE

For Fedora and openSUSE, this repo includes a working spec file to build an RPM package.
openSUSE supports RPMs, so the same process works for both.

Below is a simple guide to build it yourself.

### 1. Install RPM Build Dependencies

Install all the core tools:

```sh
sudo dnf install rpm-build rpmdevtools redhat-rpm-config make gcc \
fedora-packager gnupg2 rpm-sign createrepo_c git patch tar
```

Also install the core build tools for Carch:

```sh
sudo dnf install cargo git
```

### 2. Set Up the Build Tree

```sh
rpmdev-setuptree
```

### 3. Get the Spec File

Download the `carch.spec` file into `~/rpmbuild/SPECS/`

```sh
wget https://github.com/carch-org/pkgs/raw/refs/heads/main/carch.spec ~/rpmbuild/SPECS/
```

Change to the SPECS directory:

```sh
cd ~/rpmbuild/SPECS
```

### 4. Download the Source Files

> Note: Make sure you are in `~/rpmbuild/SPECS/` before running this.

```sh
spectool -g -R carch.spec
```

### 5. Build the RPM

```sh
rpmbuild -ba carch.spec
```

Wait for the build to finish, then go to:

```sh
cd ~/rpmbuild/RPMS/x86_64/
```

You will see the `.rpm` file if the build was successful.

## Add GPG Signature (Recommended)

To avoid installation warnings (especially on openSUSE), it’s recommended to sign your RPMs.

### 1. Create a GPG Key

```sh
gpg --full-generate-key
```

Use a 4096 key size.
Enter your real name and email; the comment is optional.

List your generated keys:

```sh
gpg --list-keys
```

Or with long IDs:

```sh
gpg --list-keys --keyid-format LONG
```

### 2. Add Your GPG Name to RPM Macros

Edit (or create) `~/.rpmmacros`:

```sh
echo '%_gpg_name Your Name <yourmailid@gmail.com>' >> ~/.rpmmacros
```

### 3. Export & Import the Public Key

Export your public key:

```sh
gpg --export --armor yourgpgkey > publickey.asc
```

Import it into the RPM keyring:

```sh
sudo rpm --import publickey.asc
```

Alternatively, import directly:

```sh
sudo rpm --import <(gpg --export --armor yourkeyid)
```

### 4. Sign the RPM

Replace the filename with your actual RPM:

```sh
rpmsign --addsign ~/rpmbuild/RPMS/x86_64/carch-5.2.2-1.fc42.x86_64.rpm
```

You’ll be asked for the passphrase you set when creating your GPG key.

### 5. Verify the Signature

```sh
rpm --checksig ~/rpmbuild/RPMS/x86_64/carch-5.2.2-1.fc42.x86_64.rpm
```

A successful result looks like: 

```sh
carch-5.2.2-1.fc42.x86_64.rpm: digests signatures OK
```

### Install the RPM

```sh
sudo dnf install carch-5.2.2-1.fc42.x86_64.rpm
```

Or on openSUSE:

```sh
sudo zypper install carch-5.2.2-1.fc42.x86_64.rpm
```

> [!IMPORTANT]
> openSUSE may warn that the package is unsigned if it was signed on Fedora.
> To avoid this, sign the RPM on openSUSE too — for example, using a container like distrobox.
> If you sign on openSUSE, the same RPM works fine on Fedora too.
> If you only care about Fedora, signing on Fedora is enough.

I will also release pre-signed RPM packages built on openSUSE in the Carch releases, so you can just grab those directly if you prefer.

That’s it from my side!
If you notice anything missing or incorrect, feel free to contribute a fix.
Thank you!
