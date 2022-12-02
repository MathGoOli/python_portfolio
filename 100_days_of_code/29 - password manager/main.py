from tkinter import *
from tkinter import messagebox
import json
from generate_password import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#  its on generate_pasword.py

def password_write():
    password = generate_password()
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "username": username,
        "password": password,
    }}
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered:\n"
                                                              f" email: {username} "
                                                              f"\n password:{password}\n"
                                                              f" is it ok to save?")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                #  reading old data
                data = json.load(data_file)
        except(FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #  updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #  saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ----------------------------  search  ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        messagebox.showinfo(title=f'website: {website_entry.get()}',
                            message=f"your username is: {data[website_entry.get()]['username']} \n"
                                    f"your password is: {data[website_entry.get()]['password']}")
    except KeyError:
        messagebox.showinfo(title="OOPS", message=f"there is no \"{website_entry.get()}\" website found")
        pass


# ---------------------------- UI SETUP ------------------------------- #

windown = Tk()
windown.title("Password Manager")
windown.config(width=500, height=500, padx=50, pady=50)

#  canvas

bg_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

#  label

website_label = Label(text="website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entries

website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=45)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "math@gmail.com")

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

#  buttons

generate_password_button = Button(text="Generate Password", command=password_write)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="ADD", width=39, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=3, row=1)
windown.mainloop()
