from tkinter import *

root = Tk()

class window_config:

    def __init__(self, root):

        root.resizable(False, False)
        root.geometry("400x600")
        root.title("Jlord's Calculator")
        root.configure(background="#17161b")
        root.overrideredirect()

class app:

    def __init__(self, root):

        frame = Frame(root, bg="#17161b")
        frame.place(rely=0.25)

        for i in range(10);
        Button(frame, text="1", font=("Roboto", 40), bg="#2E2C36", fg="white", height=1, width=2)

        decimal_button = Button(frame, text=".", font=("Roboto", 40), bg="#2E2C36", fg="white", height=1, width=2)
        equal_button = Button(frame, text="=", font=("Roboto", 40), bg="#2E2C36", fg="white", height=1, width=2)
        plus_button = Button(frame, text="+", font=("Roboto", 40), bg="#2E2C36", fg="white", height=1, width=2)
        min_button = Button(frame, text="-", font=("Roboto", 40), bg="#2E2C36", fg="white", height=1, width=2)
        mult_button = Button(frame, text="x", font=("Roboto", 40), bg="#2E2C36", fg="white", height=1, width=2)
        div_button = Button(frame, text="/", font=("Roboto", 40), bg="#2E2C36", fg="white", height=1, width=2)
        del_button = Button(frame, text="del", font=("Roboto", 20), bg="#2E2C36", fg="white", height=13, width=4)

        button1.grid(row=2, column=0, padx=2.5, pady=2.5)
        button2.grid(row=2, column=1, padx=2.5, pady=2.5)
        button3.grid(row=2, column=2, padx=2.5, pady=2.5)
        button4.grid(row=1, column=0, padx=2.5, pady=2.5)
        button5.grid(row=1, column=1, padx=2.5, pady=2.5)
        button6.grid(row=1, column=2, padx=2.5, pady=2.5)
        button7.grid(row=0, column=0, padx=2.5, pady=2.5)
        button8.grid(row=0, column=1, padx=2.5, pady=2.5)
        button9.grid(row=0, column=2, padx=2.5, pady=2.5)
        button0.grid(row=3, column=0, padx=2.5, pady=2.5)
        decimal_button.grid(row=3, column=1, padx=2.5, pady=2.5)
        equal_button.grid(row=3, column=2, padx=2.5, pady=2.5)
        plus_button.grid(row=3, column=3, padx=2.5, pady=2.5)
        min_button.grid(row=2, column=3, padx=2.5, pady=2.5)
        mult_button.grid(row=1, column=3, padx=2.5, pady=2.5)
        div_button.grid(row=0, column=3, padx=2.5, pady=2.5)
        del_button.grid(row=0, column=4, padx=2.5, pady=2.5, rowspan=4)

        self.show_text = StringVar()
        show = Entry(root, bg="#FFFFFF", font=("Roboto", 20), textvariable=self.show_text)
        show.place(relx=0.0125, rely=0.15, height=50, width=390)

        results_text = StringVar()
        results = Label(root, font=("Roboto", 30), bg="#323138", fg="white", textvariable=results_text)
        results.place(height=75, width=390, relx=0.0125, rely=0.015)

    def button_1(self):

        value = 1
        self.show_text.set(value)

    def button_2(self):

        value = 2
        self.show_text.set(value)


app(root)
window_config(root)
root.mainloop()