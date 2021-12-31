# Windows Menu Editor

English| [简体中文](./README-zh.md)

## Introduction

Windows 11 Classic Right-Click Menu Editor.Change your windows 11 right-click menu back to the old style of windows 10 with one click.
## Requirement

- [Python 3.10](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [PyInstaller 4.7](http://www.pyinstaller.org/)

## Develop

```bash
pip install pyinstaller
python win/main.py
```

## Build

```bash
pyinstaller -F -w -i ./win/assets/img/logo.ico ./win/main.py --add-data "./win/bat/classic.bat;bat" --add-data "./win/bat/default.bat;bat" -n "win-menu-editor" --noconfirm
```
## Reference

- [TKinter-UI](https://github.com/openHacking/TKinter-UI)
- [TkDocs](https://tkdocs.com/)