import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Messagebox")
root.geometry("200x200")
root.configure(bg="black")

def popup():
    msg = messagebox.askyesno("Error!", "You love belva too much!")
    if msg is True:
        print("true")
    else:
        quit()


tk.Button(root, text="Pop", command=popup, width=10, height=5).place(anchor=tk.CENTER, relx=0.5, rely=0.5)

root.mainloop()