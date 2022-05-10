import tkinter as tk

WIDTH = 500
HEIGHT = 300


class WindowConfig(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.resizable(False, False)
        self.title("GELOS Enterprise")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


class App:

    def __init__(self, window):
        self.no_acc_text = None
        self.signup_btn = None
        self.confirm_key = True
        self.b = None
        self.a = None
        self.user = None
        self.pwd = None
        self.file = None

        # FRAME
        self.frame = tk.Frame(window)
        self.frame.place(anchor=tk.CENTER, rely=0.5, relx=0.5)
        self.signup_frame = tk.Frame(window, width=WIDTH, height=HEIGHT, bg="black")

        self.entry_text = tk.StringVar()
        self.entry_text1 = tk.StringVar()
        tk.Entry(self.frame, textvariable=self.entry_text, width=30, font=("Arial", 10)).grid(row=1, column=1, padx=5,
                                                                                              pady=5)
        tk.Entry(self.frame, textvariable=self.entry_text1, width=30, font=("Arial", 10)).grid(row=2, column=1, padx=5,
                                                                                               pady=5)

        tk.Label(self.frame, text="Username").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.frame, text="Password").grid(row=2, column=0, padx=5, pady=5)

        tk.Button(self.frame, text="Login", command=self.on_click).grid(columnspan=2, row=3, pady=10)

        wlc = tk.Label(self.frame, text="Hello, welcome to GELOS Enterprise!", font=("Calibri", 20), height=2)
        wlc.grid(columnspan=2, row=0, column=0, sticky=tk.N)

        signup_btn = tk.Button(self.frame, text="Sign up", command=lambda: self.click_sign_up(self.signup_frame))
        signup_btn.grid(columnspan=2, row=4)

    def on_click(self):
        self.a = self.entry_text.get()
        self.b = self.entry_text1.get()

        self.reading()

    def reading(self):
        self.file = open("accounts.txt", "r")
        for line in self.file.readlines():
            data = line.strip()
            self.user, self.pwd = data.split(".")
            # print("Accounts:{}, Password:{}".format(self.user, self.pwd))
            if (self.a == self.user) and (self.b == self.pwd):
                self.confirm_key = True
                # print("It's inside. Ah~")
                break
            else:
                self.confirm_key = False
                # print("It's not inside yet... Put it in senpai~")
        self.file.close()
        if self.confirm_key is False:
            self.no_acc_text = tk.Label(self.frame, text="Click 'sign up' to make a new account.", font=("Arial", 10))
            self.no_acc_text.grid(columnspan=2, row=5, sticky=tk.S, ipady=10)
        print(self.confirm_key)

    def click_sign_up(self, frm):
        frm.tkraise()
        tk.Label(self.signup_frame, text='Page 1', font='times 35', bg='red')


root = WindowConfig()
App(root)
root.mainloop()
