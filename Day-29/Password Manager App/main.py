from json.decoder import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from password_generator import Password_Generator
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new_password():
    password_entry.delete(0, END)
    generate_password = Password_Generator()
    new_password = generate_password.create_password()
    password_entry.insert(0, f"{new_password}")
    pyperclip.copy(new_password)
    messagebox.showinfo(message="Password copied to clipboard")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showwarning(title="Warning", message="Hey you left some entry unfilled")
        return
    new_data = {
        website_entry.get().lower(): {
            "email":email_entry.get(),
            "password":password_entry.get()
        }
    }
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
            messagebox.showinfo(title="Success", message="Password saved.")
    else:
        data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
            messagebox.showinfo(title="Success", message="Password saved.")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
#---------------------------SEARCH PASSWORD----------------------------#

def search_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)    
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="File not found")
    else:
        if website_entry.get().lower() in data:
            messagebox.showinfo(title=website_entry.get().capitalize(), message=f'Email: {data[website_entry.get().lower()]["email"]}\nPassword: {data[website_entry.get().lower()]["password"]}')
        elif len(website_entry.get()) == 0:
            messagebox.showwarning(title="Warning", message="Website field cannot be empty")
        else:
            messagebox.showerror(title="Not Found", message="No details of the website exists")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(425,400)
window.maxsize(425,400)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(90, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website = Label(text="Website")
website.grid(row=1, column=0)

email = Label(text="Email/Username")
email.grid(row=3, column=0)

password_label = Label(text="Password")
password_label.grid(row=4, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1,columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "vharshitkr01@gmail.com")
email_entry.grid(row=3, column=1,columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(row=4, column=1, columnspan=2)

# Buttons
generate_pass_btn = Button(text="Generate Password", width=30, command=new_password)
generate_pass_btn.grid(row=5, column=1, columnspan=2)

add_btn = Button(text="Save Info", width=30, command=save)
add_btn.grid(row=6, column=1,columnspan=2)

search_btn = Button(text="Search Password", width=30, command=search_password)
search_btn.grid(row=2, column=1,columnspan=2)

window.mainloop()