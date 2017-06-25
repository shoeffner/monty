import tkinter as tk

class GridWindow:

    def __init__(self, root):
        root.title("The tree example GUI")

        self.label = tk.Label(root, text='Some label in the second row')
        self.label.grid(row=1, column=0, columnspan=3)

        self.close_button = tk.Button(root, text="Close", command=root.quit)
        self.close_button.grid(row=0, column=1, columnspan=2)
        self.do_nothing = tk.Button(root, text="Do nothing")
        self.do_nothing.grid(row=0, column=0)

if __name__ == '__main__':
    root = tk.Tk()
    GridWindow(root)
    root.mainloop()
