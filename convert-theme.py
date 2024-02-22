#! /usr/bin/env python

"""Converts a Microsoft Plus desktop theme into a HTML page."""

from os import listdir
import argparse

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

print (theme)

# Generate the HTML output.
output = '<html>\n'
output += '<head>\n'
output += '<title>' + theme_filename.replace('.Theme', '') + '</title>\n'
output += '</head>\n'
output += '<body>\n'
output += '</body>\n'
output += '</html>\n'

# Print HTML output.
print (output)
