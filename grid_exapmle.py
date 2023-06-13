from tkinter import *

window = Tk()

window.title("my First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


my_label = Label(text="hello", font=("Arial", 20, "bold") )
my_label.grid(column=0, row=0)

button1 = Button(text="button1")
button1.grid(column=3, row=0)

button12 = Button(text="button2")
button12.grid(column=2, row=1)

entry = Entry(width=10)
entry.get()

entry.grid(column=4, row=3)

window.mainloop()

