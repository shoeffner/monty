import tkinter as tk

class ToggleWindow:

    def __init__(self, root):
        root.title("Updating a label")
        self.toggle_button = tk.Button(root, text="Toggle", command=self.toggle)
        self.toggle_button.pack()

        self.label_text = tk.StringVar()
        self.label_text.set('Hello!')
        self.label = tk.Label(root, textvariable=self.label_text)
        self.label.pack()

    def toggle(self):
        if self.label_text.get() == 'Hello!':
            self.label_text.set('Bye!')
        else:
            self.label_text.set('Hello!')

if __name__ == '__main__':
    root = tk.Tk()
    ToggleWindow(root)
    root.mainloop()
