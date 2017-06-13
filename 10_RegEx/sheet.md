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


# Exercise 1: Requests

Go to [Project Gutenberg](https://www.gutenberg.org/) and search for some
books. Pick a book! We picked @darwin, which has [ID 1228](https://www.gutenberg.org/ebooks/1228).

Write a script `bookreview.py` which, given an ID, performs
the following tasks, which are explained in more detail below:

1. Download the book and save it as `{author}-{title}.txt`. You can
   extract the required information from the first line of the downloaded file.
1. Preprocess the book by removing the preamble and license. Don't remove this
   information from the saved version.
1. Search for all sentences containing the words in the `wordlist.txt`. Store
   each first sentence in a file `{author}-{title}-sentences.txt`. Store
   the counts in a file called `{author}-{title}-words.csv`.


## Running the program

To analyze @darwin, we need to provide the ID 1228. You may pick another book
if you like. Note that you may hard code the ID, but we recommend to use
a variable -- especially if you attempt the bonus tasks (see below).


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
data inside the file. It is counted as a single character, so you can either
skip it (`pgline[1:]`) or parse around it like we do in the example. You can
use `repr(...)` to make it visible. If you have troubles, try to leave it out,
skip it, parse parts, ... You will be able to get this done.

Use the author and title information to write the contents you downloaded to
a file `{author}-{title}.txt`.


## Preprocessing the data

A Project Gutenberg file contains some data before and after the actual book
contents. These contain meta data and license statements. "Clean" the data by
removing everything before and including `*** START OF THIS PROJECT GUTENBERG
EBOOK {} ***` and everything from `*** END OF THIS PROJECT GUTENBERG EBOOK {}
***`. Note that the placeholder is the title in uppercase letters, i.e.
`title.upper()`. You can just use `.index` on a string to find a substrings
occurrence. Use it to slice the string: `bookcontent[start:end]`.


## Crawling the data

In the file `wordlist.txt` are some words. Load the list and search all
sentences which contain the words, respectively.

Write one example sentence per word into the file
`{author}-{title}-sentences.txt`. Write a csv file
`{author}-{title}-words.csv` which contains the words and their
respective counts.


# Bonus tasks

1. Use `sys.argv` to read a custom book ID when running the program, e.g.
   `python bookreview.py 1228` would use the ID `1228` which can be found in
   the list `sys.argv` at position `1`.
1. Measure the download duration using `time`. You can measure time by taking
   difference between the start and end time of an action. `time.time()` gives
   you the current time in seconds since January 1st, 1970, 00:00:00 UTC.


## Example output

Here is an example output for program call `python bookreview.py` (or, if you finished the bonus tasks, `python bookreview.py 1228`).
Your output can differ.

*Output:*

```
Downloaded 1228, Charles Darwin: On the Origin of Species, in 2.009 s.

The word counts are:
  he       120
  she       18
  love       3
  live      29
  hate       0
  food      48
  body      34
  wise       0
  plant     59
  rich       5
  legend     0

Some example sentences:

 Last year he sent to
me a memoir on this subject, with a request that I would forward it
to Sir Charles Lyell, who sent it to the Linnean Society, and it is
published in the third volume of the Journal of that Society.

 She can act on every internal organ, on every shade of
constitutional difference, on the whole machinery of life.
```


```{ .csv file='books/Charles Darwin-On the Origin of Species-words.csv' }
```


```{ file='books/Charles Darwin-On the Origin of Species-sentences.txt' }
```


# References
