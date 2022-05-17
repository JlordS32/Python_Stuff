from tkinter import *

class MyApp:

    def __init__(self, window):

        window.title("Jaylou")
        window.geometry("500x400")
        window.maxsize(1000, 800)

        self.label_text = StringVar()
        label = Label(window, text="Hello World!", textvariable=self.label_text)
        label.pack()

        # label["text"] = "New label text"
        # label["font"] = ("Arial", 40)

        label.configure(text="New label text", font=("Arial", 50))

        self.entry_text = StringVar()
        self.entry = Entry(window, textvariable=self.entry_text)
        self.entry.pack()

        # label["textvariable"] = entry_text

        button = Button(window, text="Press", command=lambda: self.press_button())
        button.pack()

    def press_button(self):
        text = self.entry_text.get()
        self.entry.delete(0, END)
        self.label_text.set(text)

    def add(self, value):
        print(value)
        self.label_text.set(value)



window = Tk()
MyApp(window)
window.mainloop()