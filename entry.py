from tkinter import *
from PIL import ImageTk, Image

time = 1

def clicked(times):
    global time, e, test
    time += 1
    test = Label(root, text=f"{times} | {entry.get()}")
    test.pack()

def reset():
    global time
    time = 1

def boost():
    global time
    time += 1

def zilch():
    global time
    time = 0

def show():
    test.pack()

def kill():
    test.destroy()

def hide():
    test.pack_forget()

root = Tk()
root.title("Elite 3")
root.geometry("1024x768")
image = ImageTk.PhotoImage(Image.open("./untitled.png"))
image_label = Label(root, image=image)
image_label.pack()
button = Button(root,text="Show me stuff", command=lambda: clicked(time))
button2 = Button(root,text="text", command=reset)
button3 = Button(root,text="text", command=boost)
button4 = Button(root,text="text", command=zilch)
button5 = Button(root,text="show", command=show)
button6 = Button(root,text="hide", command=hide)
button7 = Button(root,text="kill", command=hide)
entry = Entry(root, width=300, font=("Cantarell", 32))
entry.pack()
button.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
root.mainloop()