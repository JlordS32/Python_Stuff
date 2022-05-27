from tkinter import *

root = Tk()


def window_config():
    root.geometry("500x500")
    root.maxsize(1000, 800)
    root.title("First test")


class app:

    def __init__(self, root):
        text = Label(root, text="Hello World!")
        text.pack()

        text.configure(font=("Courier", 30))

        self.entry_text = StringVar()
        e = Entry(root, textvariable=self.entry_text)
        e.pack()

        b = Button(root, text="Touch me~", command=self.button_pressed)
        b.pack()

    def button_pressed(self):
        user = self.entry_text.get()
        print("ok", user)

app(root)
window_config()
root.mainloop()
