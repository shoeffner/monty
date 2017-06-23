from tkinter import Tk, Button


class SimpleWindow:

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

if __name__ == '__main__':
    root = Tk()
    SimpleWindow(root)
    root.mainloop()
