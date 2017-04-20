% Exercise Sheet 05 -- Handling Errors and Debugging

# Submission

By the end of this sheet you will have a number of different files to submit.
In Stud.IP you will have a directory for your own group, please upload them
there. It is easier for you if you just archive all files and upload your
archive (preferably zip), but it is okay if you upload them one by one.

# Exercise 1:



# Exercise 2: Reading and writing csv files

At the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/)
you can find a lot of interesting data sets to do some Machine Learning. While
we don't want to do Machine Learning today, we still want to read and process
some data.

Check out the famous [iris
dataset](https://archive.ics.uci.edu/ml/datasets/Iris) and download the file
`iris.data`. If you read the website carefully you will find some problems with
the data set:

> This data differs from the data presented in Fishers article

Which is followed by descriptions of the differences. Your task is to correct
these differences using a script `iris_correction.py` and save a corrected
version named `iris.csv`. (You don't need to submit the corrected file.)

You can take a look into the `csv` module to read and write the files, but it
is also possible to solve this exercise without.
