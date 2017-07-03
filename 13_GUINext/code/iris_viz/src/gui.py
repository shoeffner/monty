import tkinter as tk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2TkAgg)


class IrisVisualizer:

    def __init__(self, root, iris_labels, iris_data):
        """Initializes the IrisVisualizer.

        Args:
            root: The tk-parent.
            iris_labels: The labels for the iris data set (Sepal Width, etc.)
            iris_data: The iris data as a list of lists.
        """
        self.root = root
        self.root.title('Iris data visualizer')

        self.figure = plt.figure()
        self.data = iris_data
        self.labels = iris_labels

        self.init_canvas()
        self.init_controls()
        self.update_plot()

        # Handles click on close properly
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def init_canvas(self):
        """Initializes the matplotlib canvas.

        Adapted from
        https://matplotlib.org/examples/user_interfaces/embedding_in_tk.html

        Generates a frame and palces a figure canvas and a navigation toolbar
        inside it.
        """
        frame_figure = tk.Frame(self.root, bd=1, relief=tk.SUNKEN)
        frame_figure.grid(row=0, column=0, sticky=tk.NW+tk.SW)
        canvas = FigureCanvasTkAgg(self.figure, master=frame_figure)
        canvas.show()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2TkAgg(canvas, frame_figure)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def init_controls(self):
        """
        Initializes the radio boxes to choose x-axis and y-axis data
        dimensions.
        """
        self.frame_controls = tk.Frame(self.root, bd=1, relief=tk.SUNKEN)
        self.frame_controls.grid(row=0, column=1, sticky=tk.NE+tk.SE)
        tk.Label(self.frame_controls, text='Axes').grid(row=0, column=0,
                                                        sticky=tk.W+tk.E)

        self.frame_x = tk.Frame(self.frame_controls, bd=1, relief=tk.SUNKEN)
        self.frame_x.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.frame_y = tk.Frame(self.frame_controls, bd=1, relief=tk.SUNKEN)
        self.frame_y.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.label_x = tk.Label(self.frame_x, text='X-Axis')
        self.label_x.grid(row=0, column=0)

        self.label_y = tk.Label(self.frame_y, text='Y-Axis')
        self.label_y.grid(row=0, column=0)

        self._x_selection = tk.IntVar()
        self._x_selection.set(0)

        for row, label in enumerate(self.labels[:-1]):
            radio = tk.Radiobutton(self.frame_x, variable=self._x_selection,
                                   value=row, text=label,
                                   command=self.update_plot)
            radio.grid(row=row, column=1, sticky=tk.W)

        self._y_selection = tk.IntVar()
        self._y_selection.set(1)

        for row, label in enumerate(self.labels[:-1]):
            radio = tk.Radiobutton(self.frame_y, variable=self._y_selection,
                                   value=row, text=label,
                                   command=self.update_plot)
            radio.grid(row=row, column=1, sticky=tk.W)

    def close(self):
        """Closes the plot and destroys the GUI."""
        plt.close()
        self.root.destroy()

    def update_plot(self):
        """Clears the plot and redraws it, using the new data selected by
        the checkboxes."""
        axes = self.figure.gca()
        axes.clear()
        axes.set_title('Iris data')

        x = self._x_selection.get()
        y = self._y_selection.get()
        axes.set_xlabel(self.labels[x] + ' in cm')
        axes.set_ylabel(self.labels[y] + ' in cm')

        for cl, col in zip(list(set(d[4] for d in self.data)),
                           ['orange', 'green', 'blue']):
            axes.scatter(*zip(*((d[x], d[y]) for d in self.data if d[4] == cl)),
                         color=col, label=cl)

        axes.legend()
        self.figure.canvas.draw()
