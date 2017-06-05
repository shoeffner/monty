% Exercise Sheet 10 -- Regular Expressions


# Submission

By the end of this sheet you will have a number of different files to submit.
In Stud.IP you will have a directory for your own group, please upload them
there. It is easier for you if you just archive (preferably zip) all files and
upload your archive, but it is okay if you upload them one by one.


# Packages

**Attention**

For this exercise sheet you will need two additional Python packages. Install
them using:

```{ .bash }
pip install requests parse
```

If you have any troubles with installing them, let us know as soon as possible
so we can resolve issues fast.

You can find the documentations here:

- requests: http://docs.python-requests.org
- parse: https://github.com/r1chardj0n3s/parse/blob/master/README.rst


# Exercise 1: Making coffee revisited

*Note*: For a more exhaustive problem description, please refer to sheet
9 exercise 1 again.

In the file `coffeerecipes.txt` is a list of coffee recipes which are used as
inputs to the following FSA:

\begin{tikzpicture}[->,>=stealth,shorten >=1pt,auto,node distance=2.8cm,
                    semithick]
    \node[initial,state] (A)              {A};
    \node[state]         (B) [below of=A] {B};
    \node[state]         (C) [right of=A] {C};
    \node[state]         (D) [below of=C] {D};
    \node[state]         (E) [right of=C] {E};
    \node[state]         (F) [right of=D] {F};
    \node[state,accepting]         (G) [right of=F] {G};

    \path (A) edge              node {P} (C)
              edge [loop above] node {C} (A)
              edge              node {F} (B)
          (B) edge              node {P} (D)
              edge [loop below] node {C} (B)
          (C) edge              node {C} (E)
              edge              node {F} (D)
          (D) edge              node {C} (F)
          (E) edge [loop above] node {C} (E)
              edge              node {F} (F)
          (F) edge [loop below] node {C} (F)
              edge              node {B} (G)
          (G) edge [loop below] node {C} (G)
          ;
\end{tikzpicture}

Check which of the recipes are correct by using regular expressions with the
`re` module. Do not use last weeks solutions. Submit your code in a file named
`coffeeregex.py`.


# Exercise 2: Requests, `sys.argv`, and time

Go to [Project Gutenberg](https://www.gutenberg.org/) and search for some
books. Pick a book! We picked @darwin, which has [ID 1228](https://www.gutenberg.org/ebooks/1228).

Write a script `bookreview.py` which, given an ID[^pgid], performs
the following tasks, which are explained in more detail below:

1. Download the book and save it as `{author}-{title}.txt`. You can
   extract the required information from the first line of the downloaded file.
   Measure how long it takes and present the user the time.
1. Preprocess the book by removing the preamble and license. Don't remove this
   information from the saved version.
1. Search for all sentences containing the words in the `wordlist.txt`. Store
   each first sentence in a file `{author}-{title}-sentences.txt`. Store
   the counts in a file called `{author}-{title}-words.csv`.


## Running the program

To analyze @darwin, we could run the program like this: `python bookreview.py
1228`. To access the id `1228` from inside the program, you can use
`sys.argv[1]`[^argparse] (you need to import `sys`).

[^argparse]: If you want to be really fancy, take a look at `argparse`. But for
this homework it is probably overkill.


## Downloading the book

Use the `requests` library to download the book from Project Gutenberg. Find
a way to create proper URLs to the text-only version of a Project Gutenberg
book. When downloading the data, measure the time and present the user with
some output about it.

You can extract the author and title information from the first line, in our
book it is:

`\ufeffThe Project Gutenberg EBook of On the Origin of Species, by Charles Darwin`

To extract the information, you can adapt this snippet:

```{ .python .exec }
import parse
pgline = ('\ufeffThe Project Gutenberg EBook of On the ' +
          'Origin of Species, by Charles Darwin')
result = parse.parse('\ufeffThe Project Gutenberg EBook of ' +
                     '{title}, by {author}', pgline)
title = result['title']
author = result['author']
print('{}: {}'.format(author, title))
```

The weird `\ufeff` is the byte order mark, it tells programs how to read the
data inside the file. It is counted single character, so you can either skip it
(`pgline[1:]`) or select it like in the example. You can use `repr(...)` to
make it visible. If you have troubles, try to leave it out, skip it, parse
parts, ... You will be able to get this done.

Use the author and title information to write the contents you downloaded to
a file `{author}-{title}.txt`.


## Preprocessing the data

A Project Gutenberg file contains some data before and after the actual book
contents. These contain meta data and license statements. "Clean" the data by
removing everything before and including `*** START OF THIS PROJECT GUTENBERG
EBOOK {} ***` and everything from `*** END OF THIS PROJECT GUTENBERG EBOOK {}
***`. Note that the placeholder is the title in uppercase letters, i.e.
`title.upper()`.


## Crawling the data

In the file `wordlist.txt` are some words. Load the list and search all
sentences which contain the words, respectively.

Write one example sentence per word into the file
`{author}-{title}-sentences.txt`. Write a csv file
`{author}-{title}-words.csv` which contains the words and their
respective counts.


## Example output

Here is an example output for program call `python bookreview.py 1228`.
Your output can differ.

*Output:*

```
Downloaded 1228, Charles Darwin: On the Origin of Species, in 7.118 s.

The word counts are:
  he        81
  she       14
  love       3
  live      21
  hate       0
  food      21
  body      16
  wise       0
  plant     33
  rich       4
  legend     0

Some example sentences:

 Last year he sent to
me a memoir on this subject, with a request that I would forward it
to Sir Charles Lyell, who sent it to the Linnean Society, and it is
published in the third volume of the Journal of that Society.

 Though nature grants vast periods of time
for the work of natural selection, she does not grant an indefinite
period; for as all organic beings are striving, it may be said, to seize
on each place in the economy of nature, if any one species does
not become modified and improved in a corresponding degree with its
competitors, it will soon be exterminated.

```


```{ .csv file='books/Charles Darwin-On the Origin of Species-words.csv' }
```


```{ file='books/Charles Darwin-On the Origin of Species-sentences.txt' }
```


# References
