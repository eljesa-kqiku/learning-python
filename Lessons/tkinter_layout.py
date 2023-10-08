from tkinter import *

window = Tk()
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)

label = Label(text="Label (0,0)")
label.grid(column=0, row=0)

new_button = Button(text="Button (2, 0)")
new_button.grid(column=2, row=0)

button = Button(text="Button (1, 1)")
button.grid(column=1, row=1)

entry = Entry()
entry.grid(column=3, row=2)
entry.insert(END, string="Entry (3,2)")

window.mainloop()
