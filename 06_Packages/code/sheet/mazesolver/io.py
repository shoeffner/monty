import sys


def load_maze(filename):
    """Loads a maze.

    Loads a maze from a given filename.

    A maze file contains the layout of the maze as rows of numbers separated by
    spaces. The numbers encode the following:

        0: Empty space.
        1: Starting position.
        2: Wall space (not accessible).
        3: Cheese position.

    Note that only exactly one 1 and one 3 are allowed. (This is not checked.)

    Args:
        filename: The file to be read.

    Returns:
        A list containing a list per line.
        For example if the file contained:

            2 2 2 2 2 2
            2 1 0 0 3 2
            2 2 2 2 2 2

        The resulting list would look like this:

            [[2, 2, 2, 2, 2, 2],
             [2, 1, 0, 0, 3, 2],
             [2, 2, 2, 2, 2, 2]]

    """
    maze = [[]]
    # TODO: Write this function to return what is asked above.

    return maze


def print_maze(maze, file=sys.stdout):
    """Prints the maze to the file.

    Args:
        maze: The maze to print.
        file: The file to print to, defaults to sys.stdout.
    """
    for row in maze:
        print(' '.join([str(v) for v in row]), file=file)


def store_maze(maze, filename):
    """Stores a maze into a file.

    The maze is stored in the same layout as described in load_maze(filename).

    Args:
        A maze as lists of lists.
    """
    with open(filename, 'w') as maze_file:
        print_maze(maze, maze_file)
