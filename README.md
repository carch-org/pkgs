<div align="center">
 
# Carch Package Builds

 <img src="https://img.shields.io/badge/Maintained%3F-Yes%20(Except%20Carch--Bin)-1c1c29?style=for-the-badge&color=ef9f9c&logoColor=85e185&labelColor=1c1c29">
 <img src="https://img.shields.io/github/license/carch-org/pkgs?style=for-the-badge&color=e0ea9d&logoColor=D9E0EE&labelColor=171b22">

<br>

[carch-bin](https://github.com/carch-org/pkgs/tree/main/carch-bin) is no longer maintained ❎

</div>

---

> [!IMPORTANT]
> Installing or uploading packages that act as installer scripts or customize the system in a way that diverges from the official guidelines is not allowed on the AUR.
>
>  As such, the package has been removed from the AUR. I respect the AUR guidelines, and I encourage you to check the main Carch project for alternative installation methods. Thank you!

> [!NOTE]
> Carch is not available on the AUR because it is a script. However, you can use the provided package build to run Carch as a package, similar to an AUR package, or visit the Carch [documentation](https://carch-org.github.io/docs) for the CLI installer.

*Assuming, You have already install dependency like: `make` & `git`*

### 📦 Package Build [ Stable ]

```sh [Package Build ]
git clone https://github.com/carch-org/pkgs
cd pkgs/carch
makepkg -si
```

### 📦 Git Package Build [ Latest Git-Build ]

```sh [Git Package Build ]
git clone https://github.com/carch-org/pkgs
cd pkgs/carch-git
makepkg -si
```

> [!NOTE]
> You can use the `carch` package for stable updates with the latest release, or use the `git package` to get the most recent changes directly from the Carch GitHub repository.

