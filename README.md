# monty
Course material for Basic Programming in Python in the summer semester 2017 at
Osnabrück University.


## Prerequisites

You will need [pandoc](http://pandoc.org/) to compile the materials.
Additionally you need to install the python requirements, as the custom pandoc
filters rely on them.
I recommend using [SplitShow](https://github.com/mpflanzer/splitshow) (for
MacOS) to show the notes properly. The full setup is something along these
lines, adjust accordingly:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" || exit 1
    brew update && brew upgrade && brew doctor
    brew install python3 pandoc pandoc-citeproc
    brew cask install mactex splitshow
    pip3 install -r requirements.txt


## Compile

To compile a specific chapter, just run:

```sh
make NUM
```

where `NUM` is the chapter (e.g. `01`) you want to compile. If you only want to compile the
slides or the homework sheet, just use the following commands, respectively. The `zip` command zips the sheet and solution directories.

```sh
make notesNUM
make slidesNUM
make sheetNUM
make solutionNUM
make zipNUM
```

* `slides` creates the slides to be uploaded (includes notes as individual slides).
* `notes` creates the slides with notes on the same slide to be viewed e.g. via
  [SplitShow](https://github.com/mpflanzer/splitshow).
* `sheet` creates the exercise sheet.
* `solution` creates the exercise solution sheet.
* `zip` zips the exercises and solutions in individual zip files to be uploaded
  conveniently.

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
    |   |-- dates.txt
    |   |-- hello.py
    |   |-- nicholas.py
    |   |-- sheet.list
    |   |-- sheet.md
    |   |-- slides.md
    |   |-- solution.list
    |   `-- solution.md
    |-- 02_VariableAssignment
    |   |-- dates.txt
    |   |-- sheet.md
    |   |-- slides.md
    |   `-- solution.md
    |-- ...
    `-- NN_Title
        |-- *.py
        |-- *
        |   `-- *.py
        |-- dates.txt
        |-- sheet.list
        |-- sheet.md
        |-- slides.md
        |-- solution.list
        `-- solution.md

The `dates.txt` files contain two rows, the first specifies the date of the
lecture (to be included in slides and notes), the second specifying the
deadline for the homeworks. An example file would be:

    Tue, 04 Apr 2017
    Mon, 10 Apr 2017

The `*.list` files contain a list of all files (except for the pdf) to be
included into the respective zip files.
For example, for sheet 01 it could look like this:

    hello.py
    nicholas.py

For sheet NN with a subdir it could look like this:

    task01/*.py
    task02/test.py
