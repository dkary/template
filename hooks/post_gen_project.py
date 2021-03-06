# use a cookiecutter hook to remove .gitkeep files in templates
# https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html#example-conditional-files-directories

import os

for root, dirs, files in os.walk('.'):
    for currentFile in files:
        if currentFile == '.gitkeep':
            os.remove(os.path.join(root, currentFile))