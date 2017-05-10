"""This module handles the maze solving."""


def solve_maze(maze, y, x):
    """Solves a maze recursively.

    The maze will be modified in-place!

    The maze should be a list of lists (each inner list representing
    a row). y and x denote the current position of the mouse, where
    y is the row index and x the column index.

    The maze solver works with backtracking:

        If the maze is not solved:
            For all directions:
                If direction is free (i.e. the maze has a 0 in the next space):
                    Walk into the direction (set the next space to 1)
                    Solve the maze from the new position.
                    If solving was successful:
                        return True
                    Otherwise:
                        Reset the field to 0.
                Elif the cheese is found (next space is 3):
                    return True

    Args:
        maze: The maze.
        y: The mouse row.
        x: The mouse column.

    Returns:
        True if the maze was solved successfully, else False.
    """
    if not solved(maze):
        for yshift, xshift in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if not maze[y + yshift][x + xshift]:
                maze[y + yshift][x + xshift] = 1
                success = solve_maze(maze, y + yshift, x + xshift)
                if success:
                    return True
                else:
                    maze[y + yshift][x + xshift] = 0
            elif maze[y + yshift][x + xshift] == 3:
                return True
    return False


def solved(maze):
    """Checks if the maze was solved.

    The maze is solved, if there is no 3 to be found.

    Returns:
        True if the maze has no 3.
    """
    for row in maze:
        if 3 in row:
            return False
    return True


def get_start(maze):
    """Searches for the 1 inside the maze.

    Returns:
        The row and column of the found 1.
        E.g. if 1 was in row 3 and column 4, this would return:
            3, 4
        If there is no 1 in the maze, this returns
            -1, -1
    """
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == 1:
                return y, x
    return -1, -1
