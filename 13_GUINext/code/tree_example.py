import tkinter as tk

class TreeWindow:

    def __init__(self, root):
        self.root = root
        root.title("The tree example GUI")

        self.frame1 = tk.Frame(root, border=4, relief=tk.SUNKEN)
        self.frame1.pack(fill=tk.X, padx=5, pady=5)
        self.frame2 = tk.Frame(root, border=4, relief=tk.SUNKEN)
        self.frame2.pack(fill=tk.X, padx=5, pady=5)

        self.close_button = tk.Button(self.frame1, text="Close",
                                      command=root.quit)
        self.close_button.pack()
        self.print_button = tk.Button(self.frame2, text="Toggle",
                                      command=self.toggle_label)
        self.print_button.pack()

        self.label_text = tk.StringVar()
        self.label = tk.Label(self.frame2, textvariable=self.label_text)
        self.toggle_label()
        self.label.pack()

    def toggle_label(self):
        if self.label_text.get() == 'Toggle me!':
            self.label_text.set('Don\'t toggle me!')
        else:
            self.label_text.set('Toggle me!')

if __name__ == '__main__':
    root = tk.Tk()
    TreeWindow(root)
    root.mainloop()
