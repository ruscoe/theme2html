#! /usr/bin/env python

"""Converts a Microsoft Plus desktop theme into a HTML page."""

from os import listdir
import argparse
import os

def rgbToHex(rgb):
    colors = rgb.split(' ')
    return '#%02x%02x%02x' % (int(colors[0]), int(colors[1]), int(colors[2]))

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', type=str, required=True, help='the path containing the .Theme file')

args = parser.parse_args()

# Find the .Theme file.
theme_filename = ''
for file in listdir(args.path):
    if file.endswith('.Theme'):
        theme_filename = file

# Open the .Theme file.
with open(args.path + '/' + theme_filename, encoding='utf8', errors='ignore') as theme_file:
    theme = theme_file.read()

# print (theme)

# Create an images directory.
if not os.path.exists('images'):
    os.makedirs('images')

# Parse the theme variables.
wallpaper = ''
window_background = ''
inactive_border = ''
inactive_title_background = ''
inactive_title_color = ''
for line in theme.split('\n'):
    if line.startswith('Wallpaper='):
        wallpaper = line.split('=')[1]
        # Replace the %ThemeDir% variable with the theme's path.
        wallpaper = wallpaper.replace('%ThemeDir%', args.path + '/')
        # Replace Windows backslashes with Unix forward slashes.
        wallpaper = wallpaper.replace('\\', '/')
    if line.startswith('Menu='):
        # Parse the window background.
        window_background = rgbToHex(line.split('=')[1])
    if line.startswith('InactiveBorder='):
        # Parse the inactive title background.
        inactive_border = rgbToHex(line.split('=')[1])
    if line.startswith('InactiveTitle='):
        # Parse the inactive title background.
        inactive_title_background = rgbToHex(line.split('=')[1])
    if line.startswith('InactiveTitleText='):
        # Parse the inactive title color.
        inactive_title_color = rgbToHex(line.split('=')[1])

# Copy the wallpaper to the images directory.
os.system('cp "' + wallpaper + '" images/wallpaper.jpg')

# Generate the HTML output.
with open('template.html', 'r') as template_file:
    template = template_file.read()
    template = template.replace('%title%', theme_filename.replace('.Theme', ''))
    template = template.replace('%window_background%', window_background)
    template = template.replace('%inactive_border%', inactive_border)
    template = template.replace('%inactive_title_background%', inactive_title_background)
    template = template.replace('%inactive_title_color%', inactive_title_color)

# Print HTML output.
print (template)
