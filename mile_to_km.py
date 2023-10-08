from tkinter import *

window = Tk()
window.config(padx=20, pady=20)
window.title("Mile to kilometer converter")

label = Label(text="is equal to")
label.grid(column=0, row=1)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

km_output_label = Label(text="0")
km_output_label.grid(column=1, row=1)

mile_input = Entry()
mile_input.insert(END, string="0")
mile_input.grid(column=1, row=0)
mile_input.config(width=10)
mile_input.focus()


def calculate():
    miles = int(mile_input.get())
    km = miles * 1.609344
    km_output_label.config(text=km)


calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)

window.mainloop()