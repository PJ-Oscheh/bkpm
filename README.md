# bkpkg
Burg Kurg Package Manager

**NOTE:** bkpkg is still under development. Currently, it can:

- Download packages given their source is in `list.csv` and record said package and its version in `installed.csv`.
- Update packages when the version reported in `list.csv` is different from that in `installed.csv`
- Update the `list.csv` database.

ToDo:

- Implement self-updating
- Implement server software updating
- Easy method to manually add packages to `installed.csv`
- Downloads from sources like Spigot, where the URL doesn't end in `.jar`
- More, probably

Bkpkg is a package manager for Minecraft server admins to easily install and update plugins (and soon, the server software itself!). Feel free to create a Pull Request to add desired plugins!

The plugins's source must be manually updated in `list.csv`, but `list.csv` can be updated from bkpkg, so we encourage our users to create a Pull Request to update links, so that those changes can be sent to everyone!

Burg Kurg is my own server, and thus I opted to name this program after it. However, this program is for everyone!
