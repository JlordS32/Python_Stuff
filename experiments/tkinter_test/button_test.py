import tkinter as tk

def button_pressed():
    user = e.get()
    print(user)
    return None

root = tk.Tk()
root.geometry("500x100")
root.title("Button Test")

e = tk.Entry(root, width=20)
e.pack()

tk.Button(root, text="Press", command=button_pressed).pack()

root.mainloop()