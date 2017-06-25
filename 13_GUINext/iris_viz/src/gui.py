import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2TkAgg)


class IrisVisualizer:

    def __init__(self, root, iris_labels):
        self.root = root
        self.root.title('Iris data visualizer')

        self.init_canvas(plt.figure())
        self.init_controls(iris_labels)

        # Handles click on close properly
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def init_canvas(self, figure):
        self.frame_figure = tk.Frame(self.root, bd=1, relief=tk.SUNKEN)
        self.frame_figure.grid(row=0, column=0,
                               sticky=tk.NW+tk.SW)
        self.canvas = FigureCanvasTkAgg(figure, master=self.frame_figure)
        self.canvas.show()
        self.canvas.get_tk_widget().pack()

    def init_controls(self, iris_labels):
        self.frame_controls = tk.Frame(self.root, bd=1, relief=tk.SUNKEN)
        self.frame_controls.grid(row=0, column=1,
                                 sticky=tk.NE+tk.SE)
        self.label_title = tk.Label(self.frame_controls, text='Axes')
        self.label_title.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.frame_x = tk.Frame(self.frame_controls, bd=1, relief=tk.SUNKEN)
        self.frame_x.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.frame_y = tk.Frame(self.frame_controls, bd=1, relief=tk.SUNKEN)
        self.frame_y.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.label_x = tk.Label(self.frame_x, text='X-Axis')
        self.label_x.grid(row=0, column=0)

        self.label_y = tk.Label(self.frame_y, text='Y-Axis')
        self.label_y.grid(row=0, column=0)

        self.radios = []

        self._x_selection = tk.IntVar()
        self._x_selection.set(0)

        for row, label in enumerate(iris_labels):
            self.radios.append(
                tk.Radiobutton(self.frame_x, variable=self._x_selection,
                               value=row, text=label, command=self.update_plot)
            )
            self.radios[-1].grid(row=row, column=1, sticky=tk.W)

        self._y_selection = tk.IntVar()
        self._y_selection.set(1)
        for row, label in enumerate(iris_labels):
            self.radios.append(
                tk.Radiobutton(self.frame_y, variable=self._y_selection,
                               value=row, text=label, command=self.update_plot)
            )
            self.radios[-1].grid(row=row, column=1, sticky=tk.W)

    def close(self):
        plt.close()
        self.root.destroy()

    def update_plot(self):
        pass
