import random
import string
from tkinter import *

window = Tk()

class window_config:

    def __init__(self, window):
        window.maxsize(400, 400)
        window.title("Password Generator")
        window.geometry("400x400")

class App:

    def __init__(self, window):

        label = Label(window, text="Password Generator")
        label.config(font=("Arial", 25))
        label.place_configure(relx=0.5, rely=0.1, anchor=CENTER)

        button = Button(text="Generate", font=("Arial", 15), command=self.on_click)
        button.place_configure(relx=0.5, rely=0.25, anchor=CENTER)

    def on_click(self):
        q = Label(text="How many characters do you want for your password?", font=("Arial", 11))
        q.place_configure(relx=0.5, rely=0.4, anchor=CENTER)

        self.entry_text = StringVar()
        e = Entry(width=20, font=("Arial", 15), textvariable=self.entry_text)
        e.place_configure(relx=0.5, rely=0.5, anchor=CENTER)

        b2 = Button(text="Press to generate", font=("Arial", 10), command=self.password_generator)
        b2.place_configure(relx=0.5, rely=0.6, anchor=CENTER)

    def password_generator(self):
        self.length = int(self.entry_text.get())

        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        num = string.digits
        symbol = string.punctuation

        password = lower_case + upper_case + num + symbol

        ans = "".join(random.sample(password, self.length))
        print("Here's the generated password:", ans)
        f = open("pass_generated.txt", "a")
        f.write(ans + "\n")
        f.close()

        gen_pass = Label(text="Generated password: {}".format(ans))
        gen_pass.place_configure(relx=0.5, rely=0.8, anchor=CENTER)
        gen_pass.configure(font=("Arial", 15))

App(window)
window_config(window)
window.mainloop()
