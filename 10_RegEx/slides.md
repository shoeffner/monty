% Regular Expressions


# Matching strings: "Python binaries"

\begin{center}
\begin{tikzpicture}[->,>=stealth,shorten >=1pt,auto,node distance=2.8cm,
                    semithick]
    \node[initial,state]   (A)              {A};
    \node[state]           (B) [right of=A] {B};
    \node[state]           (C) [right of=B] {C};
    \node[state,accepting] (D) [right of=C] {D};
    \node[state]           (E) [node distance=1cm, below of=C] {\color{cyan}E};

    \path (A) edge              node {0} (B)
              edge [bend right] node {1, b} (E)
          (B) edge              node {b} (C)
              edge [bend right] node {0, 1} (E)
          (C) edge              node {0, 1} (D)
              edge              node {b} (E)
          (D) edge [loop right] node {0, 1} (D)
              edge [bend left]  node {b} (E)
          (E) edge [loop below] node {0, 1, b} (E)
          ;
\end{tikzpicture}
\end{center}

\note{
Last week we discussed the formal language "Python binaries" and how to check strings if they are part of it.

Today we learn a powerful tool to not only check if a string matches a certain
grammar (i.e. is part of a formal language), but also to find all matching
sequences inside long texts: Regular expressions.
}


# Regular Expressions (regex)

- Regex are often called *patterns*
- Regex were designed to match regular languages (Type 3, see next slide)
- TODO

# Chomsky hierarchy


# Formal definition of regular languages[^srcwikilang]

[^srcwikilang]: Adapted from @wiki2017reglang


# Regex for "Python binaries"


# Match vs. search


# Complex regex

- ^ and $
- groups
- character sets, negation
- .
- escaping


# Examples


# Greediness


# lookahead

TODO ?!

# Computer Communication


# The Internet


# IETF & W3C


# Internet Protocol


# HTTP verbs


# HTTP via urllib


# HTTP via requests


# Data exchange (form data, post/get) TODO


# JSON, xml, yaml


# REST vs. Website/Webapp


# API TODO


# Your tenth homework

- Solve the coffee brewing task again using regular expressions.
- Download a book and find some sentences containing specific words.
