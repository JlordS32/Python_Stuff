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
        # VARIABLES
        self.no_acc_text = None
        self.signup_btn = None
        self.confirm_key = True
        self.passw = None
        self.acc = ""
        self.user = None
        self.pwd = None
        self.file = None

        # FRAME
        self.acs_frame = tk.Frame(window, border=200)
        self.signup_frame = tk.Frame(window, border=100)
        self.main_frame = tk.Frame(window, border=50)

        self.signup_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.acs_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame.place_configure(rely=0.5, relx=0.5, anchor=tk.CENTER)
        self.signup_frame.place_configure(rely=0.5, relx=0.5, anchor=tk.CENTER)
        self.acs_frame.place_configure(rely=0.5, relx=0.5, anchor=tk.CENTER)

        # MAIN FRAME
        self.entry_text = tk.StringVar()
        self.entry_text1 = tk.StringVar()

        self.main_entry = tk.Entry(self.main_frame, textvariable=self.entry_text, width=30, font="arial 10")
        self.main_entry.grid(row=1, column=1, padx=5, pady=5)
        self.main_entry1 = tk.Entry(self.main_frame, textvariable=self.entry_text1, width=30, font="arial 10")
        self.main_entry1.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.main_frame, text="Username").grid(row=1, column=0, pady=5, sticky=tk.E)
        tk.Label(self.main_frame, text="Password").grid(row=2, column=0, pady=5, sticky=tk.E)

        tk.Button(self.main_frame, text="Login", command=lambda: self.on_click(self.acs_frame)).grid(columnspan=2, row=3, pady=10)

        wlc = tk.Label(self.main_frame, text="Hello, welcome to GELOS Enterprise!", font=("Calibri", 20), height=2)
        wlc.grid(columnspan=2, row=0, column=0, sticky=tk.N)

        signup_btn = tk.Button(self.main_frame, text="Sign up", command=lambda: self.click_sign_up(self.signup_frame))
        signup_btn.grid(columnspan=2, row=4)

        # SIGN UP FRAME
        main_btn = tk.Button(self.signup_frame, text="Create Account", command=lambda: self.click_sign_up(self.main_frame))
        main_btn.grid(row=3, column=0, columnspan=2, pady=10)

        signup_text = tk.Label(self.signup_frame, text="Sign up", font="calibri 20")
        signup_text.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.signup_frame, text="Username").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.signup_frame, text="Password").grid(row=2, column=0, padx=5, pady=5)

        self.sign_entry = tk.StringVar()
        self.sign_entry1 = tk.StringVar()

        self.signup_entry = tk.Entry(self.signup_frame, textvariable=self.sign_entry, width=30, font="arial 10")
        self.signup_entry.grid(row=1, column=1, padx=5, pady=5)
        self.signup_entry1 = tk.Entry(self.signup_frame, textvariable=self.sign_entry1, width=30, font="arial 10")
        self.signup_entry1.grid(row=2, column=1, padx=5, pady=5)

    def on_click(self, frm):
        self.acc = self.entry_text.get()
        self.passw = self.entry_text1.get()

        self.reading()

        if self.confirm_key is True:
            frm.tkraise()
            self.welcome_screen()

    def reading(self):
        self.file = open("accounts.txt", "r")
        for line in self.file.readlines():
            data = line.strip()
            self.user, self.pwd = data.split(".")
            # print("Accounts:{:15s} Password:{}".format(self.user, self.pwd))
            if (self.acc == self.user) and (self.passw == self.pwd):
                self.confirm_key = True
                break
            else:
                self.confirm_key = False
        self.file.close()
        if self.confirm_key is False:
            tk.Label(self.main_frame, text="Account doesn't exist on the server.").grid(columnspan=2, row=5, pady=5)
            self.no_acc_text = tk.Label(self.main_frame, text="Click 'sign up' to make a new account.", font="arial 10")
            self.no_acc_text.grid(columnspan=2, row=6, sticky=tk.S)
        print(self.confirm_key)

    def click_sign_up(self, frm):
        self.main_entry.delete(0, tk.END)
        self.main_entry1.delete(0, tk.END)
        self.signup_entry.delete(0, tk.END)
        self.signup_entry1.delete(0, tk.END)
        frm.tkraise()

    def welcome_screen(self):
        tk.Label(self.acs_frame, text="Welcome {}".format(self.acc)).pack()



window = WindowConfig()
App(window)
window.mainloop()
