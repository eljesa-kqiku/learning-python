from tkinter import *
from tkinter import messagebox
from random import randint, choice, randrange, shuffle
from pyperclip import copy


# Password Manager

# Save Password
def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website != '' and email != '' and password != '':
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the entered details: \nEmail: {email}\nPassword: {password}\n Proceed saving?")
        if is_ok:
            row = f"{website} | {email} | {password}\n"

            with open("data.txt", mode='a') as file:
                file.write(row)

            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please fill in all fields!")


# Password generator
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    all_chars = password_letters + password_symbols + password_numbers
    shuffle(all_chars)
    password = "".join(all_chars)

    password_input.delete(0, END)
    password_input.insert(0, password)
    copy(password)


# UI Setup
window = Tk()
window.config(padx=50, pady=50, bg="#ffffff")
window.title("Password Manager")

image = PhotoImage(file="logo.png")
canvas = Canvas(width=230, height=230, bg="#ffffff", highlightthickness=0)
canvas.create_image(103, 103, image=image)
canvas.grid(column=0, row=0, columnspan=3, pady=20)

# Labels
website_label = Label(text="Website: ", bg="#ffffff")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ", bg="#ffffff")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", bg="#ffffff")
password_label.grid(column=0, row=3)

# Inputs
website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, 'eljesakqiku@gmail.com')

password_input = Entry(width=22)
password_input.grid(column=1, row=3)

# Buttons
generate_password_btn = Button(text="Generate Password", bg='#31C6D4', fg="#ffffff", bd=0, pady=1,
                               command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=34, bg='#27E1C1', fg="#ffffff", bd=0, pady=3, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, pady=3)

window.mainloop()
