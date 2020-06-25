# Cookiecutter Python Template

A template folder/file structure for Python Analysis Projects. Adapted from [Cookiecutter Data Science](http://drivendata.github.io/cookiecutter-data-science/)

## Setup on your Machine

You'll need to install the [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html). Open Anaconda Prompt and run:

```
> pip install cookiecutter
```

## Initializing an Analysis

Open Anaconda prompt, navigate to the project folder, and run the code below (You'll be prompted to choose a folder name for the analysis. Press enter to select the default.):

```
> cookiecutter gh:dkary/template
```

In the future you can just run the code below (because the 'template' will be cached on your machine):

```
> cookiecutter template
```

## Tweaking

You can prevent the .gitkeep files from showing up in your folders by removing them from the cached cookie. Using Anaconda Prompt:

```
C:\Users\username> cd .cookiecutters
C:\Users\username\.cookiecutters> DEL /S /Q *.gitkeep
```
