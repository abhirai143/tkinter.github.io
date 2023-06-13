from tkinter import *

window = Tk()

window.title("my First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="Simple Form!", font=("Arial", 24, "bold") )
my_label.pack()
entry1 = Entry(width=30)
entry2 = Entry(width=30)

entry1.insert(END, string="Email")
entry2.insert(END, string="Password")

entry1.pack()
entry2.pack()


def button_clicked():
    my_label.config(text="Welcome")
    user_input1 = entry1.get()
    user_input2 = entry2.get()
    print(user_input1, user_input2)


button = Button(text="submit", command=button_clicked)
button.pack()


















window.mainloop()