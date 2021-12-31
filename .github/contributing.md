# Contributing Guide

## Requirement
When we get a project, we must first install the dependencies contained in requirement.txt in the project runtime environment:

```bash
pip install -r requirement.txt
```
When we want to write the dependencies in the environment into requirement.txt, we can use the freeze command:
```bash
pip freeze >requirements.txt
```

## Build exe

```bash
pyinstaller -w -i ./win/assets/img/logo.ico ./win/main.py --add-data "./win/bat/classic.bat;." --add-data "./win/bat/default.bat;." -n "win-menu-editor"
```
## Reference
https://tkdocs.com/tutorial/