# Desktop Theme to HTML Converter

Converts a Microsoft Plus desktop theme into a HTML page.

This is a classic example of wondering if one could without wondering if
one should.

## Usage

Download a [desktop theme from Archive.org](https://archive.org/details/windowsdesktopthemes). [Inside Your Computer](https://archive.org/details/inside_201808) is a good one, just make sure you note the caveats below.

Extract the .Theme file and its associated directory somewhere locally. It should
look like this:

```
'Inside Your Computer'
'Inside your Computer (16 bit).Theme'
```

Assuming you extracted those files to a directory named `theme`, you can then run
the following:

`python3 convert-theme.py -p theme > output.html`

This will create a HTML file named `output.html`. Open this file in your web browser
to see the results of your desktop theme conversion.

## Supported features

* :white_check_mark: Desktop wallpaper
* :red_circle: Icons
* :red_circle: Window colors
* :red_circle: Fonts
* :red_circle: Sounds

## Caveats

This script has only been tested with Python 3.10.12 on Ubuntu Linux.

### Capitalization in file paths

In 1995, Windows apparently did not care about capitalization in file paths.
Linux does, however. If you have a .Theme file that contains lower case paths and
the files are in upper case directories, you'll have to modify the .Theme file
before running the converter.

For example, the "Inside Your Computer" desktop theme that ships with Microsoft Plus,
the wallpaper path is given as:

`%ThemeDir%Inside your Computer\Inside your Computer Wallpaper.jpg`

This is wrong because the actual path includes a **capital Y** in **your**:

`%ThemeDir%Inside Your Computer\Inside your Computer Wallpaper.jpg`

If you see this in a .Theme file, just change it to match the correct path.
