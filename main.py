from tkinter import *
# messagebox is a different file
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # List Comprehension to add random letters to list
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Join will join the list items with the first "" provided
    password_generated = "".join(password_list)

    password.delete(0, END)
    password.insert(0, password_generated)

    # Add password to clipboard
    pyperclip.copy(password_generated)

    print(f"Your password is: {password_generated}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    if website.get() == "":
        messagebox.showerror(title="Error", message="Make sure to enter value of website before Searching.!")
    else:
        try:
            with open("data.json", mode="r") as output_file:
                data = json.load(output_file)
                email_value = data[website.get()]["email"]
                pass_value = data[website.get()]["password"]
                messagebox.showinfo(title="Info",
                                    message=f"Email: {email_value}\n Password: {pass_value}")
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="Details are not yet provided.!")
        except KeyError:
            messagebox.showerror(title="Error", message="Details are not yet provided.!")


def save():
    new_data = {
        website.get(): {
            "email": username.get(),
            "password": password.get()
        }}
    if len(website.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Oops", message="Make sure to enter values before saving.!")
    else:
        try:
            with open("data.json", mode="r") as output_file:
                # Read old data
                data = json.load(output_file)
                # Update the old data with the new one
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", mode="w") as output_file:
                # Add it to json
                json.dump(new_data, output_file, indent=4)
        else:
            with open("data.json", mode="w") as output_file:
                # Add it to json
                json.dump(data, output_file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=2, row=1)

label_site = Label(text="Website:")
label_site.grid(column=1, row=2)
website = Entry(width=21)
website.grid(column=2, row=2)
# when the program starts focus method will make the default entry option on email
website.focus()

label_uname = Label(text="Email/Username:")
label_uname.grid(column=1, row=3)
username = Entry(width=38)
username.grid(column=2, row=3, columnspan=2)
username.insert(0, "example_email@gmail.com")

label_uname = Label(text="Password:")
label_uname.grid(column=1, row=4)
password = Entry(width=21)
password.grid(column=2, row=4)

genpass_button = Button(text="Generate Password", highlightthickness=0, command=password_gen)
genpass_button.grid(column=3, row=4)

search_button = Button(text="Search", highlightthickness=0, command=find_password, width=13)
search_button.grid(column=3, row=2)

addpass_button = Button(text="Add", highlightthickness=0, width=34, command=save)
addpass_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
