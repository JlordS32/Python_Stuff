from tkinter import*

class Window(Tk):

    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("Ok game")
        self.resizable(False, False)

class frm(Frame):

    def __init__(self):
        super().__init__(background='black')

        Button(text="Hello").grid(row=0, column=0, sticky=N)
        Button(text="World").grid(row=0, column=1, sticky=N)

        Label(text="Omae wa mou shindeiru.", font=("Roboto", 40)
              ).grid(row=1, column=2)




window = Window()
frame = frm()
frame.grid()
window.mainloop()