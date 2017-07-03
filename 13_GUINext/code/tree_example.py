import tkinter as tk

class TreeWindow:

    def __init__(self, root):
        self.root = root
        root.title("The tree example GUI")

        self.frame1 = tk.Frame(root, border=4, relief=tk.SUNKEN)
        self.frame1.pack(fill=tk.X, padx=5, pady=5)
        self.frame2 = tk.Frame(root, border=4, relief=tk.SUNKEN)
        self.frame2.pack(fill=tk.X, padx=5, pady=5)

        self.close_button = tk.Button(self.frame1, text="Close", command=root.quit)
        self.close_button.pack()
        self.do_nothing = tk.Button(self.frame2, text="Do nothing")
        self.do_nothing.pack()

        self.label = tk.Label(self.frame2, text="This is a label.")
        self.label.pack()

if __name__ == '__main__':
    root = tk.Tk()
    TreeWindow(root)
    root.mainloop()
    root.destroy()
