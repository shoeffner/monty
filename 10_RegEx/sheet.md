% Exercise Sheet 10 -- Regular Expressions


# Submission

By the end of this sheet you will have a number of different files to submit.
In Stud.IP you will have a directory for your own group, please upload them
there. It is easier for you if you just archive (preferably zip) all files and
upload your archive, but it is okay if you upload them one by one.


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
          (F) edge [loop below] node {F} (F)
              edge              node {B} (G)
          (G) edge [loop below] node {C} (G)
          ;
\end{tikzpicture}

Check which of the recipes are correct by using regular expressions with the
`re` module. Do not use last weeks solutions=

