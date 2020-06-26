# use a cookiecutter pre-generate hook to remove .gitkeep files in templates
# https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html#example-conditional-files-directories

import os

for root, dirs, files in os.walk('{{ cookiecutter.folder_name }}'):
    for currentFile in files:
        if currentFile == '.gitkeep':
            os.remove(os.path.join(root, currentFile))