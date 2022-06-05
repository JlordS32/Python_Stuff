from tkinter import *

class MyApp:

    def __init__(self, root):

        root.geometry("500x500")
        root.maxsize(1000, 800)
        root.title("A widget")

        self.label_text = StringVar()
        text = Label(root, textvariable=self.label_text)
        text.pack()

        # text["text"] = "New ok"
        # text["font"] = "Arial", 30

        text.configure(text="The now new ok", font=("Arial", 30))

        # ENTRY
        self.entry_text = StringVar()
        e = Entry(root, textvariable=self.entry_text)
        e.pack()

        b = Button(root, text="Press me!", command=self.press_button())
        b.pack()

    def press_button(self):
        text = self.entry_text.get()
        self.label_text.set(text)
        print(text)



root = Tk()
MyApp(root)
root.mainloop()