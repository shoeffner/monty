import tkinter as tk

from gui import IrisVisualizer
from data import iris_data


def main():
    iris, labels = iris_data()

    root = tk.Tk()
    IrisVisualizer(root, labels, iris)
    root.mainloop()


if __name__ == '__main__':
    main()
