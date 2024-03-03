# Desktop Theme to HTML Converter

Converts a Microsoft Plus desktop theme into a HTML page.

![theme2html](https://github.com/ruscoe/theme2html/assets/87952/26bfe315-1f20-439e-80ec-1d007026c9cf)

## Demo

Live demos:

* [Mystery](https://ruscoe.org/theme2html/mystery/)
* [OS2 Warp](https://ruscoe.org/theme2html/os2/)

## Usage

Download a [desktop theme from Archive.org](https://archive.org/details/windowsdesktopthemes).
[Mystery](https://archive.org/details/mystery_202005) works well.

Extract the .Theme file and its associated directory somewhere locally. It should
look similar to this:

```
Mystery
Mystery (16 bit).Theme
```

Assuming you extracted those files to a directory named `theme`, you can then run
the following:

`python3 convert-theme.py -p theme > output.html`

This will create a HTML file named `output.html`. Open this file in your web browser
to see the results of your desktop theme conversion.

## Tested themes

* [Airwolf](https://archive.org/details/airwolf_202004)
* [Amiga](https://archive.org/details/amiga_201808)
* [Charlie and the Chocolate Factory](https://archive.org/details/chchocmv)
* [Mystery](https://archive.org/details/mystery_202005)
* [OS2 Warp](https://archive.org/details/theme_os2_warp_202005)
* [Star Wars Episode 1](https://archive.org/details/sw1_202005)
* [Tent Camping](https://archive.org/details/camping_202005)
* [The Abyss](https://archive.org/details/abyss-x3)
* [Windows XP](https://archive.org/details/theme_xp_pack_202005)
* [X-Files](https://archive.org/details/xfthem15)

## Caveats

### Capitalization in file paths

In 1995, Windows apparently did not care about capitalization in file paths.
Linux does, however. If you have a .Theme file that contains lower case paths and
the files are in upper case directories, you'll have to modify the .Theme file
before running the converter.

For example, in the "[Inside Your Computer](https://archive.org/details/inside_201808)"
desktop theme that ships with Microsoft Plus, the wallpaper path is given as:

`%ThemeDir%Inside your Computer\Inside your Computer Wallpaper.jpg`

The actual path includes a **capital Y** in **your** and so should be:

`%ThemeDir%Inside Your Computer\Inside your Computer Wallpaper.jpg`

If you see this in a .Theme file, change it to match the correct path before
running the conversion script.

### Others

* This script will not work if the .Theme file is in the same directory as the theme assets.
* This script has only been tested with Python 3.10.12 on Ubuntu Linux.
* Fonts haven't been implemented yet.
* Sounds haven't been implemented yet.

## License

[MIT](https://mit-license.org)

## The Internet Archive

This project is possible because of the Internet Archive. If you enjoy it, please
consider [making a donation](https://archive.org/donate).
