import os
import sys

import mazesolver


def main():
    """Searches for a possible way inside a maze.

    By default it searches the medium_maze, but if started with a program
    argument, it will use the provided maze, e.g.:

        python solve_maze.py mazes/simple_maze.txt

    Prints the loaded maze, solves the maze if possible, and prints a
    result or notification about the failure.
    """
    maze_file = os.path.join('mazes', 'medium_maze.txt')
    if len(sys.argv) > 1:
        maze_file = sys.argv[1]

    maze = mazesolver.io.load_maze(maze_file)

    print('Input')
    mazesolver.io.print_maze(maze)

    y, x = mazesolver.solver.get_start(maze)
    if y == -1:
        print('No start given!')
        return

    success = mazesolver.solver.solve_maze(maze, y, x)

    if success:
        print('Way found!')
        mazesolver.io.print_maze(maze)
    else:
        print('No possible way.')


if __name__ == '__main__':
    main()
