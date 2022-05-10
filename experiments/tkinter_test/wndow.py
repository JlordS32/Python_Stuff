import tkinter as tk

class WindowConfig(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Tkinter")
        self.maxsize(1000, 800)
        self.resizable(True, True)
        self.geometry("500x500")

class App:

    def __init__(self, root):
        img = tk.PhotoImage(file="logo\\hacker.png")

        frame = tk.Frame(root)
        frame.pack()

        tk.Label(frame, text="Hello World", font=("Arial", 20), fg="purple",
                 relief=tk.RAISED, bd=10, image=img, compound="bottom").pack()


root = WindowConfig()
icon = tk.PhotoImage(file="logo\logo.png")
root.iconphoto(True, icon)
App(root)
root.mainloop()