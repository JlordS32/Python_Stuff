from tkinter import *

window = Tk()


class WindowConfig:

    def __init__(self, window):
        window.geometry("350x700")
        window.resizable(False, False)
        window.title("Jlord's Calculator")
        window.config(bg="#17161b")


class CalculatorApp:
    expression = ""

    def __init__(self, window):
        frame = Frame(window, bg="#17161b")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, bordermode="inside")

        self.show_text = StringVar()
        show = Label(frame, textvariable=self.show_text, font=("Arial", 40), bg="#FFFFFF", width=10)
        show.grid(column=0, row=0, columnspan=4, pady=10)

        # BUTTON

        btn1 = Button(frame, text="1", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("1"))
        btn1.grid(column=0, row=1, padx=5, pady=5)

        btn2 = Button(frame, text="2", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("2"))
        btn2.grid(column=1, row=1, padx=5, pady=5)

        btn3 = Button(frame, text="3", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("3"))
        btn3.grid(column=2, row=1, padx=5, pady=5)

        div_btn = Button(frame, text="/", font=("Arial", 40), width=2, height=1,
                         bg="#2E2C36", fg="white", command=lambda: self.add("/"))
        div_btn.grid(column=3, row=1, padx=5, pady=5)

        btn4 = Button(frame, text="4", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("4"))
        btn4.grid(column=0, row=2, padx=5, pady=5)

        btn5 = Button(frame, text="5", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("5"))
        btn5.grid(column=1, row=2, padx=5, pady=5)

        btn6 = Button(frame, text="6", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("6"))
        btn6.grid(column=2, row=2, padx=5, pady=5)

        mult_button = Button(frame, text="*", font=("Arial", 40), width=2, height=1,
                             bg="#2E2C36", fg="white", command=lambda: self.add("*"))
        mult_button.grid(column=3, row=2, padx=5, pady=5)

        btn7 = Button(frame, text="7", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("7"))
        btn7.grid(column=0, row=3, padx=5, pady=5)

        btn8 = Button(frame, text="8", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("8"))
        btn8.grid(column=1, row=3, padx=5, pady=5)

        btn9 = Button(frame, text="9", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("9"))
        btn9.grid(column=2, row=3, padx=5, pady=5)

        min_button = Button(frame, text="-", font=("Arial", 40), width=2, height=1,
                            bg="#2E2C36", fg="white", command=lambda: self.add("-"))
        min_button.grid(column=3, row=3, padx=5, pady=5)

        dec_button = Button(frame, text=".", font=("Arial", 40), width=2, height=1,
                            bg="#2E2C36", fg="white", command=lambda: self.add("."))
        dec_button.grid(column=0, row=4, padx=5, pady=5)

        btn0 = Button(frame, text="0", font=("Arial", 40), width=2, height=1,
                      bg="#2E2C36", fg="white", command=lambda: self.add("0"))
        btn0.grid(column=1, row=4, padx=5, pady=5)

        clear_button = Button(frame, text="C", font=("Arial", 40), width=2, height=1,
                              bg="#2E2C36", fg="white", command=lambda: self.clear())
        clear_button.grid(column=2, row=4, padx=5, pady=5)

        add_button = Button(frame, text="+", font=("Arial", 40), width=2, height=1,
                            bg="#2E2C36", fg="white", command=lambda: self.add("+"))
        add_button.grid(column=3, row=4, padx=5, pady=5)

        equal_button = Button(frame, text="=", font=("Arial", 40), width=10, height=1,
                              bg="#2E2C36", fg="white", command=lambda: self.calculate())
        equal_button.grid(columnspan=4, column=0, row=5, padx=5, pady=5)

    def add(self, value):
        CalculatorApp.expression += value
        self.show_text.set(CalculatorApp.expression)

    def calculate(self):
        try:
            result = eval(CalculatorApp.expression)
            self.show_text.set(result)
            CalculatorApp.expression = str(result)
        except (SyntaxError, ZeroDivisionError):
            self.show_text.set("Error")
            if ZeroDivisionError:
                self.show_text.set("Division Error")

    def clear(self):
        CalculatorApp.expression = ""
        self.show_text.set(CalculatorApp.expression)


CalculatorApp(window)
WindowConfig(window)
window.mainloop()
