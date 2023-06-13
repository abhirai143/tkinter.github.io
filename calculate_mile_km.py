from tkinter import *

window = Tk()
window.title("Miles to Kilometer converter!.")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_eqaul_label = Label(text="is equal to")
is_eqaul_label.grid(column=0,row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def calculate_km():
    m_input = float(miles_input.get())
    result = round(m_input * 1.609)
    km_result.config(text=str(result))

calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)





















window.mainloop()