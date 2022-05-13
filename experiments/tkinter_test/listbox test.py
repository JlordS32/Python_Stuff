import tkinter as tk

root = tk.Tk()
root.title("Listbox")
root.geometry("300x500")

listbox = tk.Listbox()
listbox.pack(pady=15)

listbox.insert(tk.END, "Ok")
listbox.insert(tk.END, "Omae")

list = ["potato", "banana", "apple", "grapes", "one"]

for item in list:
    listbox.insert(tk.END, item)

def delete():
    listbox.delete(tk.ANCHOR)

def insert():
    x = entry_text.get()
    if x == "":
        pass
    else:
        listbox.insert(tk.END, x)

def select():
    label.config(text=listbox.get(tk.ANCHOR))

button = tk.Button(root, text="Delete", command=delete)
button.pack()

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text)
entry.pack(pady=10)

insert_btn = tk.Button(root, text="Insert", command=insert)
insert_btn.pack()

select_btn = tk.Button(root, text="Select", command=select)
select_btn.pack(pady=10)

label = tk.Label(root, text='')
label.pack()


root.mainloop()