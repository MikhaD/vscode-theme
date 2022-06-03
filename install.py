"""
Run this script to copy the current version of this theme to the directory visible to vs code
"""

import os
from os import path

files = ["package.json", "package.nls.json", "themes/mikhad-dark-color-theme.json"]
destination = f"{path.expanduser('~')}/.vscode/extensions/theme-mikhad-dark"

if (not path.exists(destination)):
	os.makedirs(f"{destination}/themes")

for file in files:
	with open(f"./{file}", "r") as readfrom, open(f"{destination}/{file}", "w") as writeto:
		writeto.write(readfrom.read())