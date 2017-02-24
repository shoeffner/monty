# monty
Course material for Basic Programming in Python in the summer semester 2017 at
Osnabrück University.

## Compile

You will need [pandoc](http://pandoc.org/) to compile the materials.
Additionally you need to install the python requirements, as the custom pandoc
filters rely on them.

To compile a specific chapter, just run:

```sh
make NUM
```

where `NUM` is the chapter (e.g. `01`) you want to compile. If you only want to compile the
slides or the homework sheet, just use the following commands, respectively. The `zip` command zips the sheet and solution directories.

```sh
make slidesNUM
make sheetNUM
make solutionNUM
make zipNUM
```

### Examples:

```sh
make 04
make slides01
make sheet03
make zip05
```

## Directory structure

For everything to work properly, please create a filestructure like this:

    root
    |-- 01_HelloPython
    |   |-- hello.py
    |   |-- nicholas.py
    |   |-- sheet.list
    |   |-- sheet.md
    |   |-- slides.md
    |   |-- solution.list
    |   `-- solution.md
    |-- 02_VariablesAssignments
    |   |-- sheet.md
    |   |-- slides.md
    |   `-- solution.md
    |-- ...
    `-- NN_Title
        |-- *.py
        |-- *
        |   `-- *.py
        |-- sheet.list
        |-- sheet.md
        |-- slides.md
        |-- solution.list
        `-- solution.md

The `*.list` files contain a list of all files (except for the pdf) to be included into the respective zip files.
For example, for sheet 01 it could look like this:

    hello.py
    nicholas.py

For sheet NN with a subdir it could look like this:

    task01/*.py
    task02/test.py
