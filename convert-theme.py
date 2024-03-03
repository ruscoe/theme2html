#! /usr/bin/env python

"""Converts a Microsoft Plus desktop theme into a HTML page."""

from os import listdir
import argparse
import os

def rgbToHex(rgb):
    colors = rgb.split(' ')
    return '#%02x%02x%02x' % (int(colors[0]), int(colors[1]), int(colors[2]))

def cleanUpThemePath(path):
    # Replace the %ThemeDir% variable with the theme's path.
    path = path.replace('%ThemeDir%', args.path + '/')
    # Replace Windows backslashes with Unix forward slashes.
    path = path.replace('\\', '/')
    return path

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

# Create a sounds directory.
if not os.path.exists('sounds'):
    os.makedirs('sounds')

# Parse the theme variables.
wallpaper = ''
computer_icon = ''
network_icon = ''
bin_icon = ''
bin_full_icon = ''

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
    'ButtonText': '',
    'GrayText': '',
    'Scrollbar': '',
}

sounds = {
    'Default': '[AppEvents\Schemes\Apps\.Default\.Default',
    'AppGPFault': '[AppEvents\Schemes\Apps\.Default\AppGPFault',
}

previous_line = ''

for line in theme.split('\n'):
    if previous_line.startswith('[CLSID\{20D04FE0-3AEA-1069-A2D8'):
        computer_icon = cleanUpThemePath(line.split('=')[1].replace(',0', ''))

    if previous_line.startswith('[CLSID\{208D2C60-3AEA-1069-A2D7'):
        network_icon = cleanUpThemePath(line.split('=')[1].replace(',0', ''))

    if line.startswith('Wallpaper='):
        wallpaper = cleanUpThemePath(line.split('=')[1])

    if line.startswith('empty='):
        bin_icon = cleanUpThemePath(line.split('=')[1].replace(',0', ''))

    if line.startswith('full='):
        bin_full_icon = cleanUpThemePath(line.split('=')[1].replace(',0', ''))

    # Loop through colors and find a match.
    for key in colors:
        if line.startswith(key + '='):
            colors[key] = rgbToHex(line.split('=')[1])

    # Loop through sounds and find a match.
    for key in sounds:
        if previous_line.startswith(sounds[key]):
            sound_path = cleanUpThemePath(line.split('=')[1])
            os.system('cp "' + sound_path + '" sounds/' + key + '.wav')

    previous_line = line

# Copy the wallpaper to the images directory.
os.system('cp "' + wallpaper + '" images/wallpaper.jpg')

# Copy the Recycle Bin icon to the images directory.
if bin_icon:
    os.system('cp "' + bin_icon + '" images/bin.ico')

# Copy the Full Recycle Bin icon to the images directory.
if bin_full_icon:
    os.system('cp "' + bin_full_icon + '" images/bin_full.ico')

# Copy the My Computer icon to the images directory.
if computer_icon:
    os.system('cp "' + computer_icon + '" images/computer.ico')

# Copy the Network Neighborhood icon to the images directory.
if network_icon:
    os.system('cp "' + network_icon + '" images/network.ico')

# Generate the HTML output.
with open('template.html', 'r') as template_file:
    template = template_file.read()

    template = template.replace('%title%', theme_filename.replace('.Theme', ''))

    for key in colors:
        template = template.replace('%' + key + '%', colors[key])

print (template)
