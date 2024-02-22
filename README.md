# Desktop Theme to HTML Converter

Converts a Microsoft Plus desktop theme into a HTML page.

This is a classic example of wondering if one could without wondering if
one should.

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
