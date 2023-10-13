from tkinter import *
from tkinter import messagebox
from random import randint, choice, randrange, shuffle
from pyperclip import copy
import json


# Password Manager

# Save Password
def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website != '' and email != '' and password != '':
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }
        try:
            with open("data.json", mode='r') as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode='w') as file:
                # Save new data
                json.dump(new_data, file, indent=4)
        else:
            # Update old data
            data.update(new_data)
            with open("data.json", mode='w') as file:
                # Save updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please fill in all fields!")


def search():
    website = website_input.get()
    try:
        with open("data.json", mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        website_data = data.get(website)
        if website_data is not None:
            messagebox.showinfo(title=website,
                                message=f"Email: {website_data.get('email')}\nPassword: {website_data.get('password')}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} found")


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
website_input = Entry(width=22)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=41)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(END, 'eljesakqiku@gmail.com')

password_input = Entry(width=22)
password_input.grid(column=1, row=3)

# Buttons
search_btn = Button(text="Search", command=search,
                    bg='#31C6D4', fg="#ffffff", bd=0, pady=1, width=15)
search_btn.grid(column=2, row=1)

generate_password_btn = Button(text="Generate Password", command=generate_password,
                               bg='#31C6D4', fg="#ffffff", bd=0, pady=1,width=15)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=35, bg='#27E1C1', fg="#ffffff", bd=0, pady=3, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, pady=3)

window.mainloop()
