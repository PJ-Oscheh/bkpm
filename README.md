# BKPM
Burg Kurg Package Manager

BKPM is a package manager for Minecraft server admins to easily install and update plugins (and soon, the server software itself!). Feel free to create a Pull Request to add desired plugins! However, please add desired plugins to the correct list:

**NOTE:** BKPM is still under development. Currently, it can:

- Download packages given their source is in `list.csv`, `community.csv`, or `custom.csv` and record said package and its version in `installed.csv`.
- Update packages when the version reported in a list is different from that in `installed.csv`
- Update the lists and database.

# ToDo:

- Implement self-updating
- Implement server software updating
- Easy method to manually add packages to `installed.csv`
- More, probably


# Which list do I add a plugin to?
## Official
If your plugin will be downloaded from a source owned by the original developer, add them to the official list, `list.csv`.
## Community
If your plugin will be downloaded from a source **not** owned by the original developer (such as a plugin compiled from source and rehosted by you or another user), add them to the community list, `community.csv`

Since we unfortunately can't download plugins directly from Spigot (where may plugins are hosted) due to its anti-DDOS protection, the next best thing we can do is rehost the plugins ourselves. **HOWEVER**, it's important we respect copyright laws; as such, only add a source to this list if:

- The plugin is open source and you compiled it yourself, and are hosting it on your own (for example, in your own GitHub repo).
- The plugin author has stated their compiled binary may be redistributed.
- The plugin is free; *BKPM may not be used for piracy*.
- The plugin doesn't already exist in the official list (`list.csv`).

## Custom
Don't add plugins to the custom list (`custom.csv`); that is for any sources an individual would like to add on their own, but not share publically.




The plugins's source link and version string must be manually updated in the lists, but the lists can be updated from BKPM, so we encourage our users to create a Pull Request to update source links (if necessary) and version strings, so that those changes can be sent to everyone!

Burg Kurg is my own server, and thus I opted to name this program after it. However, this program is for everyone, and contains no advertising for my server.
