from tkinter import Tk, Button

class SimpleWindow:

    def __init__(self, root):
        self.root = root
        root.title("A simple GUI")

        self.close_button = Button(root, text="Close",
                                   command=root.quit)
        self.close_button.pack()

if __name__ == '__main__':
    root = Tk()
    SimpleWindow(root)
    root.mainloop()
