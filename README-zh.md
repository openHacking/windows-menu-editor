# Windows 菜单编辑器

简体中文 | [English](./README.md)

## 介绍

Windows 11 经典右键单击菜单编辑器。一键将你的windows11右键菜单改回windows 10旧版样式。
![](https://cdn.jsdelivr.net/gh/openHacking/static-files@main/img/16409371544461640937154438.png)

## 环境

- [Python 3.10](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [PyInstaller 4.7](http://www.pyinstaller.org/)

## 使用

1. 下载可执行文件：[Releases](https://github.com/openHacking/windows-menu-editor/releases)
2. 直接执行 `win-menu-editor.exe`


## 开发

```bash
pip install pyinstaller
python win/main.py
```

## 打包

```bash
pyinstaller -F -w -i ./win/assets/img/logo.ico ./win/main.py --add-data "./win/bat/classic.bat;bat" --add-data "./win/bat/default.bat;bat" -n "win-menu-editor" --noconfirm
```
## 参考

- [TKinter-UI](https://github.com/openHacking/TKinter-UI)
- [TkDocs](https://tkdocs.com/)