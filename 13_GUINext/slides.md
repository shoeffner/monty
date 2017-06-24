% GUI -- What next?


# User interfaces

How does the user interact with your code?

- Command line interface (CLI)
- Graphical user interface (GUI)

There are many more fine-grained definitions and notions!


# Command line interfaces

- Issue command after command
- Mostly used inside the terminal
- Examples: Shell, Python, Text adventures, ...


# Graphical user interfaces

- Event driven
- Render windows, buttons, etc.
- Examples: spyder, webbrowsers, office programs...


# Event driven

\begin{tikzpicture}[->,node distance = 4cm, auto, thick]
    \tikzstyle{every state}=[fill=blue!10,draw=black,rectangle]
    \node [state] (register) {register listeners};
    \node [state,right of=register] (eventcheck) {any events?};
    \node [state,right of=eventcheck] (notify) {notify listeners};
    \draw (register) edge (eventcheck)
            (eventcheck) edge [bend right] node {yes} (notify)
            (notify) edge [bend right] (eventcheck)
            (eventcheck)  edge [loop above]  node {no} (eventcheck);
\end{tikzpicture}


# Event types

What events do you think can happen?


# Event types

- Keyboard inputs/Mouse Inputs
- Opening, Closing, Minimizing, Maximizing
- Screen updates
- Calculation results
- ...

$\Rightarrow$ High complexity and flexibility needed!


# Redraw

GUIs need to redraw changes, e.g. a button press:

![](img/button_normal.png){width=150}![](img/button_pressed.png){width=150}



# Redraw demo

\scriptsize

```{ .python file=code/button_only.py }
```

\normalsize

\note{
`Tk()` creates the window (the "root" element), `mainloop` runs the event loop
and handles events.

Since it runs indefinitely, it also keeps the program from closing!

The Button can close the program (`quit` on the root element).
}


# Redraw: A tree approach

\begin{center}
    \begin{tikzpicture}[->,node distance=2cm, auto, thick]
        \node [rectangle, draw=black] (root) {root};
        \node [rectangle, draw=black, below left of=root] (f1) {frame};
        \node [rectangle, draw=black, below right of=root] (f2) {frame};
        \node [rectangle, draw=black, below of=f1] (b1) {button};
        \node [rectangle, draw=black, below left of=f2] (b2) {button};
        \node [rectangle, draw=black, below right of=f2] (lbl) {label};
        \draw (root) edge (f1)
            (root) edge (f2)
            (f1) edge (b1)
            (f2) edge (b2)
            (f2) edge (lbl);
    \end{tikzpicture}
\end{center}

- Each element has a parent (except root).
- Each element knows its children.

Why is this useful?

\note{
Using a tree is useful because on updates of an element only that element and
its children need to be redrawn.
}


# The tree GUI

\tiny

```{ .python file=code/tree_example.py }
```

\normalsize


# What next?

- threading
- inheritance
- numpy
- project euler and similar programming puzzles
- other reads
- classes
- databases
- different programming languages

# References
