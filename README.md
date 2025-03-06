# KevLaTeX Package

A set of python scripts as a CLI tool that help speed up the workflow when working with LaTex The main functions at the moment include

- Read a **csv** file and output the **LaTeX code** for a table
- Generate a **graph** from a **csv** file (まだ)
- Get the **LaTeX code** for an image from its **path** (まだ)
- An AI/WebScraping driven **references fetcher** (まだ)

It is important to mention that modules are accessed through relative imports.

# Installation

There are no external dependencies, so just install the required packages from the `requirements.txt` file after cloning the repository

```bash
# clone the repo into your own folder
git clone https://github.com/kevinher7/latex_scripts/
cd latex_scripts
pip install -r requirements.txt
```

# Scripts Implementation

1. Create a folder in your system to store this package and `git clone` the repo into it. Folder structure should be
   my_scripts
   └── latex_scripts
   ├── main.py
   ├── tables
   ├── ...

2. Add this directory to your PATH. This can be done from the terminal as

```bash
set PYTHONPATH=C:\Users\kevin\my-scripts
```

3. Create a batch script in the directory you created. The name of this file will be the **command name**

```mktable.bat
@echo off
set PYTHONPATH=C:\Users\kevin\my-scripts

:GETOPTS

cmd /c python -m latex_scripts.tables.generate_table %*
exit /B
```

This script manually sets PYTHONPATH to the directory, gets optional arguments and then runs the python script. The `%*` passes the previously collected optional arguments to the script.

4. Now you are ready to use the scripts

# Usage

Use the commands **by using the filename of the batch file created**

```bash
mktable my_data
```

- The first argument is the inpt file, which doesn't require to have the .csv extension, meaning that `mktale my_data.csv` is also a valid command.

You can use the --help flag to get a list of optional arguments and an explanation of the script

```bash
mktable --help
```

For example the `mktable` command can be executed with a `-c` flag to add a caption

```bash
mktable my_data -c "This is a table of my data"
```

Maybe I will add instructions on how to use different commands
