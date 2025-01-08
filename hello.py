from tkinter import *
import base64

root = Tk()
root.title("Elite")
root.geometry("1024x768")
padx=5
pady=3
my_label = Label(root, text="Pack is not a good thing to use", justify="left", bg="black", fg="white", font=("Cantarell", 32))
my_label_2 = Label(root, text="Nevermind", relief="raised", font=("Cantarell", 28))
my_label_3 = Label(root, text="Pack is really a good thing to use", relief="ridge", state=DISABLED, font=("Cantarell", 24))
my_label_4 = Label(root, text='[PACK EVERYTHING]', font=("Cantarell", 16))
my_label.grid(row=0,column=0, sticky=W)
my_label_2.grid(row=0,column=1, sticky=W)
my_label_3.grid(row=1, column=0, sticky=W)
my_label_4.grid(row=1, column=1, sticky=W)
root.mainloop()