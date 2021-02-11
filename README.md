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
- Hashes?
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

# How to use BKPM
**NOTE:**  if you're using the Python source file, BKPM should be run as: `$ python ./bkpm <options>`. For the sake of simplicity, we'll write all commands in compiled form; this means `$ bkpm -h` is equivalent to `$ python ./bkpm -h`.


BKPM's help dialog can be invoked by either messing up entering an option or with `$ bkpm -h`. It will output the following text:
```
Options:
   -i, --install: Install a new package
   -l, --update-list: Update the package lists. You MUST do this first in order to update packages!
   -u, --update: Update a package
   -a, --update-all: Update all installed packages
   -r, --remove: Remove a package
   -h, --help: Show this help dialog.
   -s, --source: Specify source for package (Official, Community, Custom
   -m. --manual-install: Install a local plugin (must be a .jar file)
```
- `$ bkpm -i <package>` will search for a package from BKPM's lists (also referred to as a *source*). If the package is found, the user will be prompted to install it. Agreeing to install the package will download it from the Source in the list, and move it to the configured Plugin Directory. It will also be added to `installed.csv`, along with its version.

- `$ bkpm -l` will update the official list (`list.csv`) and community list (`community.csv`), which may contain updated package versions.

- `$ bkpm -u <package>` will update the package mentioned, if one is availible. `$ bkpm -l` must be run first in order to check for a new version.

- `$ bkpm -a` will check for and update all installed packages from all sources. `$ bkpm -l` must be run first in order to check for a new version.

- `$ bkpm -r <package>` will remove the mentioned package and remove the entry from `installed.csv`.

- `$ bkpm -h` will show the help dialog above.

- `$ bkpm -s <source>` will only search the mentioned source for a package. Valid options are `official`,`community`, and `custom`. By default, BKPM checks all three sources, in the order of Official, Community, and Custom. **It must proceed any option** and can be used with `-i` and `-u`.

- `$ bkpm -m <path to package>` will install a local package as defined by the mentioned path. An entry in `installed.csv` will also be created, with the package name being that of the jar files, without the `.jar` extention, and all lowercase. The version string will simply be `?`. This is useful for custom plugins that aren't available online and are therefore unavailable in BKPM's lists.


Burg Kurg is my own server, and thus I opted to name this program after it. However, this program is for everyone, and contains no advertising for my server.
