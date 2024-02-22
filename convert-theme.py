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
    if file.endswith('.Theme') or file.endswith('.theme'):
        theme_filename = file

# Open the .Theme file.
with open(args.path + '/' + theme_filename, encoding='utf8', errors='ignore') as theme_file:
    theme = theme_file.read()

# Create an images directory.
if not os.path.exists('images'):
    os.makedirs('images')

# Parse the theme variables.
wallpaper = ''

colors = {
    'Hilight': '',
    'HilightText': '',
    'Window': '',
    'WindowText' : '',
    'WindowFrame' : '',
    'Menu': '',
    'ActiveBorder': '',
    'ActiveTitle': '',
    'TitleText': '',
    'InactiveBorder': '',
    'InactiveTitle': '',
    'InactiveTitleText' : '',
    'ButtonFace': '',
    'ButtonShadow': '',
    'ButtonHilight': '',
    'GrayText': '',
}

for line in theme.split('\n'):
    if line.startswith('Wallpaper='):
        wallpaper = line.split('=')[1]
        # Replace the %ThemeDir% variable with the theme's path.
        wallpaper = wallpaper.replace('%ThemeDir%', args.path + '/')
        # Replace Windows backslashes with Unix forward slashes.
        wallpaper = wallpaper.replace('\\', '/')

    # Loop through colors and find a match.
    for key in colors:
        if line.startswith(key + '='):
            colors[key] = rgbToHex(line.split('=')[1])

# Copy the wallpaper to the images directory.
os.system('cp "' + wallpaper + '" images/wallpaper.jpg')

# Generate the HTML output.
with open('template.html', 'r') as template_file:
    template = template_file.read()

    template = template.replace('%title%', theme_filename.replace('.Theme', ''))

    for key in colors:
        template = template.replace('%' + key + '%', colors[key])

print (template)
