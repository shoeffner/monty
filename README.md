# monty
Course material for Basic Programming in Python in the summer semester 2017 at
Osnabrück University.

## Compile

You will need [pandoc](http://pandoc.org/) to compile the materials.

To compile a specific chapter, just run:

```sh
make NUM
```

where `NUM` is the chapter (e.g. `01`) you want to compile. If you only want to compile the
slides or the homework sheet, just use these commands, respectively:

```sh
make slidesNUM
make sheetNUM
```

### Examples:

```sh
make 04
make slides01
make sheet03
```

## Directory structure

For everything to work properly, please create a filestructure like this:

    root
    |-- 01_HelloPython
    |   |-- slides.md
    |   `-- sheet.md
    |-- 02_VariablesAssignments
    |   |-- slides.md
    |   `-- sheet.md
    |-- ...
    `-- NN_Title
        |-- slides.md
        `-- sheet.md

