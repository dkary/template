# Cookiecutter Python Template

A template folder/file structure for Python Analysis Projects. Adapted from [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/)

## Setup on your Machine

You'll need to install the [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html). Open Anaconda Prompt and run:

```
> pip install cookiecutter
```

Make a practice template by running the code below and pressing enter to select the default folder name:

```
> cookiecutter gh:dkary/template
```

## Initializing an Analysis

Open Anaconda prompt, navigate to the project folder, and run:

```
> cookiecutter template
```

Note: You no longer need to point to the repository because 'template' will be cached on your machine after the initial setup.

## Tweaking

You can prevent the .gitkeep files from showing up in your folders by removing them from the cached cookie (although it's a bit of a hack). Using Anaconda Prompt:

```
C:\Users\username> cd .cookiecutters
C:\Users\username\.cookiecutters> DEL /S /Q *.gitkeep
```
