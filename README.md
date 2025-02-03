<div align="center">
 
# `Carch Aur Packages`

 <img src="https://img.shields.io/badge/Maintained%3F-Yes-1c1c29?style=for-the-badge&color=ef9f9c&logoColor=85e185&labelColor=1c1c29"> <img src="https://img.shields.io/github/license/carch-org/pkgs?style=for-the-badge&color=e0ea9d&logoColor=D9E0EE&labelColor=171b22">

</div>

---

> [!INFO]
> Installing or uploading packages that act as installer scripts or customize the system in a way that diverges from the official guidelines is not allowed on the AUR.
>
>  As such, the package has been removed from the AUR. I respect the AUR guidelines, and I encourage you to check the main Carch project for alternative installation methods. Thank you!

<h4>
 
**Carch is available in the [AUR](https://aur.archlinux.org/) package repository.**
</h4>

**[Packages](https://aur.archlinux.org/packages/)**

**`carch`** **`carch-git`**
 
 - [Carch](https://aur.archlinux.org/packages/carch) - <strong>[Stable Build]</strong>
 - [Carch-Git](https://aur.archlinux.org/packages/carch-git) - <strong>[Github Latest Build]</strong>


<h4>
 
You can install it using an AUR package manager.

</h4>

 - [`paru`](https://aur.archlinux.org/packages/paru-bin)
 
 - [`yay`](https://aur.archlinux.org/packages/yay-bin)

<h4>
 
Select your desire `<packager>` then

</h4>

```sh [<i class="devicon-archlinux-plain"></i> paru]
paru -S carch
#or
paru -S carch-git

```

```sh [<i class="devicon-archlinuc-plain"></i> yay]
yay -S carch
#or
yay -S carch-git
```

### 📦 Package Build 

```sh [Package Build ]
git clone https://aur.archlinux.org/carch.git
cd carch
makepkg -si
```

### 📦 Git Package Build

```sh [Git Package Build ]
git clone https://aur.archlinux.org/carch-git.git
cd carch-git
makepkg -si
```

> [!NOTE]
> You can use the `carch` package for stable updates with the latest release, or use the `git package` to get the most recent changes directly from the Carch GitHub repository.

