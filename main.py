import string
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

lowercase = [x for x in string.ascii_lowercase]
uppercase = [x for x in string.ascii_uppercase]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Generate the password


def gen_pass():
    pwd_letters = [choice(lowercase) for _ in range(randint(5, 8))] + \
                  [choice(uppercase) for _ in range(randint(5, 8))]
    pwd_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pwd_numbers = [choice(numbers) for _ in range(randint(4, 5))]

    pwd_list = pwd_letters + pwd_symbols + pwd_numbers
    shuffle(pwd_list)

    password = "".join(pwd_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# Save the password to a file


def save_pwd():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure that no fields are empty...")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"The following details have been provided\nEmail: {email}\n"
                                               f"Password: {password} Do you wish to save?")
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f"{website}, {email}, {password}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abc123@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
generate_pass_btn = Button(text="Generate password", command=gen_pass)
generate_pass_btn.grid(column=2, row=3)

save_pwd_btn = Button(text="Add", command=save_pwd, width=35)
save_pwd_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
