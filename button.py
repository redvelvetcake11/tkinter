from tkinter import *

time = 1

def clicked(times):
    global time, e
    time += 1
    Label(root, text=f"{times} | {entry.get()}").pack()

root = Tk()
root.title("Elite 3")
root.geometry("1024x768")
button = Button(root,text="Show me stuff", command=lambda: clicked(time))
button2 = Button(root,text="text")
button3 = Button(root,text="text")
entry = Entry(root, width=50)
entry.pack()
button.pack()
button2.pack()
button3.pack()
root.mainloop()