# TravelExpenses
Project for cleaning and preparing travel expense data.

1. [Folders](#1-folders)
2. [Connections](#2-connections)
3. [Local development](#3-local-development)

## 1. Folders
|Folder|Description|
|---|---|
|.vscode|Contains configuration files for use with VS Code.|
|input|Contains input data to be processed.|
|output|Contains output processed data.|
|reports|Contains Power BI reports based on output data.|
|scripts|The scripts folder contains raw Python representations of Jupyter notebooks used for processing data.|

## 2. Connections
*TODO*

## 3. Local development
### 1. Jupyter notebooks and Python scripts
Development is done with Jupyter notebooks in VS Code. The .ipynb file format is JSON based and not ideal for working with git, so files should be synced between the .ipynb and .py formats using the JupyText Sync VS Code Task. This task converts files from .ipynb to .py and vice-versa.

When opening the project for the first time, open any script and execute `Ctrl+Shift+B` to generate a corresponding .ipynb.

To persist changes made in a .ipynb to a scripts file (and to git), make sure the relevant notebook is currently open and again run `Ctrl+Shift+B` to sync back to the .py file.

Changes are always synced from the file that is currently open to the other format. Always make sure the correct file is open, or changes could be lost!
