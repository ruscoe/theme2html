#! /usr/bin/env python

"""Converts a Microsoft Plus desktop theme into a HTML page."""

from os import listdir
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", type=str, required=True, help="the path containing the .Theme file")

args = parser.parse_args()

# Find the .Theme file.
theme_filename = ''
for file in listdir(args.path):
    if file.endswith('.Theme'):
        theme_filename = file

# Open the .theme file.
with open(args.path + '/' + theme_filename, encoding='utf8', errors='ignore') as theme_file:
    theme = theme_file.read()

# print (theme)

# Create an images directory.
if not os.path.exists('images'):
    os.makedirs('images')

# Parse the theme variables.
wallpaper = ''
for line in theme.split('\n'):
    line.replace('ThemeDir', args.path + '/')
    if line.startswith('Wallpaper='):
        wallpaper = line.split('=')[1]
        break

print(wallpaper)

# Generate the HTML output.
with open('template.html', 'r') as template_file:
    template = template_file.read()
    template = template.replace('%title%', theme_filename.replace('.Theme', ''))

# Print HTML output.
print (template)
