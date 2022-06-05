import tkinter as tk

def show_frame(frm):
    frm.tkraise()

root = tk.Tk()
root.geometry('250x250')

frame1 = tk.Frame(root, bg="black")
frame2 = tk.Frame(root, bg="yellow")

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nsew")

tk.Label(frame1, text="hello world", bg="red", font="arial 30").pack()

tk.Button(frame1, text="touch me", command=lambda: show_frame(frame2)).pack()

tk.Label(frame2, text="hello world", bg="blue", font="arial 30").pack()

tk.Button(frame2, text="touch me", command=lambda: show_frame(frame1)).pack()


root.mainloop()