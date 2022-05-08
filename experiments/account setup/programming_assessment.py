import tkinter as tk

class WindowConfig(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.resizable(False, False)
        self.title("GELOS Enterprise")

class App:

    def __init__(self, root):

        frame = tk.Frame(root)
        frame.place(anchor=tk.CENTER, rely=0.5, relx=0.5)
        frame1 = tk.Frame(root)
        frame1.place(anchor=tk.CENTER, rely=0.1, relx=0.5)

        self.entry_text = tk.StringVar()
        self.entry_text1 = tk.StringVar()
        tk.Entry(frame, textvariable=self.entry_text, width=30, font=("Arial", 10)).grid(row=1, column=1, padx=5, pady=5)
        tk.Entry(frame, textvariable=self.entry_text1, width=30, font=("Arial", 10)).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Username").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(frame, text="Password").grid(row=2, column=0, padx=5, pady=5)

        tk.Button(frame, text="Login", command=self.OnClick).grid(columnspan=2, row=3, pady=10)

        wlc = tk.Label(frame1, text="Hello, welcome to GELOS Enterprise!", font=("Calibri", 20))
        wlc.grid(columnspan=2, row=0, column=0, sticky=tk.N)

    def OnClick(self):

        a = self.entry_text.get()
        b = self.entry_text1.get()

        print(a.title(), b)



root = WindowConfig()
App(root)
root.mainloop()