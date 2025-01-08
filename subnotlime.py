from tkinter import *
from tkinter import messagebox, ttk

times = 8

def fake_command():
    pass

def new_command():
    rid(edit_frame)
    current_status.set("File Status")
    file_frame.grid(row=0,column=0,columnspan=2, padx=20, pady=20)
    messagebox.showerror("Popup Title", "Popup Description")

def edit_command():
    global times
    times += 1
    rid(file_frame)
    current_status.set("Edit Status")
    edit_frame.grid(row=0,column=0,columnspan=2, padx=20, pady=20)
    response = messagebox.askquestion("Popup Title", "Popup Description")
    label = Label(root, text=response).grid(row=times,column=0)

def rid(x):
    x.grid_forget()

root = Tk()
root.title("Elite 3")
#root.geometry("1024x768")

# blah blah blah
my_menu = Menu(root)
root.config(menu=my_menu)
file = Menu(my_menu)
edit = Menu(my_menu)
view = Menu(my_menu)
help_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file)
file.add_command(label="New", command=new_command)
file.add_separator()
file.add_command(label="Exit", command=root.quit)
my_menu.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut", command=edit_command)
edit.add_command(label="Copy", command=edit_command)
edit.add_command(label="Paste", command=edit_command)
my_menu.add_cascade(label="View", menu=view)
my_menu.add_cascade(label="Help", menu=help_menu)

file_frame = Frame(root, width=200, height=200, bd=1, bg="blue", relief="sunken")
#file_frame.grid(row=1,column=0,columnspan=2, padx=20, pady=20)

file_frame_label = Label(file_frame, text="File Frame", font=("Cantarell", 20))
file_frame_label.pack(padx=20, pady=20)

edit_frame = Frame(root, width=200, height=200, bd=1, bg="blue", relief="sunken")
#file_frame.grid(row=1,column=0,columnspan=2, padx=20, pady=20)

edit_frame_label = Label(edit_frame, text="Edit Frame", font=("Cantarell", 20))
edit_frame_label.pack(padx=20, pady=20)

current_status = StringVar()
current_status.set("Waiting")

v = IntVar()
w = StringVar()
rbutton_1 = Radiobutton(root,text="One", variable=v, value=1)
rbutton_2 = Radiobutton(root,text="Two", variable=v, value=2)
rbutton_3 = Radiobutton(root,text="Three", variable=v, value=3)
rbutton_1.grid(row=1,column=0)
rbutton_2.grid(row=2,column=0)
rbutton_3.grid(row=3,column=0)

def show_value():
    if v.get() == 1:
        label = Label(root, text="Clicked radio button one")
    elif v.get() == 2:
        label = Label(root, text="Clicked radio button two")
    elif v.get() == 3:
        label = Label(root, text="Clicked radio button three")
    label.grid(row=4,column=0)

button = Button(root, text="Click Me", command=show_value)
button.grid(row=5,column=0)

my_check = Checkbutton(root, text="Pepperoni", variable=w, onvalue="pepperoni", offvalue="no_pepperoni")
my_check.deselect()
my_check.grid(row=6,column=0)

def toppings():
    global times
    times += 1
    if w.get() == "pepperoni":
        label2 = Label(root, text=f"You ordered {w.get()}")
    else:
        label2 = Label(root, text=f"You didn't want to order {w.get().replace("no_", "")}")
    label2.grid(row=times-1,column=0)

button2 = Button(root, text="Order Topping", command=toppings)
button2.grid(row=7,column=0)

my_status = Label(root, textvariable=current_status, bd=2, relief="sunken", width=56,anchor=E)
my_status.grid(row=8192,column=0)

def select():
    global times
    times += 1
    label3 = Label(root, text=combo.get())
    label3.grid(row=times+3,column=0)

options = ["Python", "Dictionary", "Or", "Python", "List"]
combo = ttk.Combobox(root,values=options)
combo.grid(row=10,column=0)
combo.current(0)

button3 = Button(root, text="Select", command=select)
button3.grid(row=11,column=0)


def window():
    window = Toplevel(root)
    window.mainloop()

button3 = Button(root, text="Window", command=window)
button3.grid(row=1024,column=0)

root.mainloop()