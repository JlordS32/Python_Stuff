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
        entry = Entry(window, textvariable=self.entry_text)
        entry.pack()

        # label["textvariable"] = entry_text

        button = Button(window, text="Press", command= lambda: self.add("1"))
        button.pack()

    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)

    def add(self, value):
        print(value)
        self.label_text.set(value)



window = Tk()
MyApp(window)
window.mainloop()