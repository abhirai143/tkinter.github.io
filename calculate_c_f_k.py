from tkinter import *

window = Tk()
window.title("Miles to Kilometer converter!.")
window.config(padx=20, pady=20)

celsius_input = Entry(width=7)
celsius_input.grid(column=1, row=0)

celsius_label = Label(text="Celsius")
celsius_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

Fahrenheit_result = Label(text="0")
Fahrenheit_result.grid(column=1, row=1)

Fahrenheit_label = Label(text="Fahrenheit")
Fahrenheit_label.grid(column=2, row=1)

is_equal_label_Kelvin = Label(text="is equal to")
is_equal_label_Kelvin.grid(column=0, row=2)

kal_result = Label(text=0)
kal_result.grid(column=1, row=2)

kal_label = Label(text="Kelvin")
kal_label.grid(column=2, row=2)


def calculate_km():
    c_input = float(celsius_input.get())
    f_result = round((c_input * 9/5) + 32)
    Fahrenheit_result.config(text=str(f_result))
    k_result = round(c_input + 273.15)
    kal_result.config(text=str(k_result))


calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=3)





















window.mainloop()