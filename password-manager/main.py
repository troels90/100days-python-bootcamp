from tkinter import *
from tkinter import messagebox
from pyperclip import copy
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = 4  #int(input("How many letters would you like in your password?\n"))
    nr_symbols = 4  #int(input(f"How many symbols would you like?\n"))
    nr_numbers = 4  #int(input(f"How many numbers would you like?\n"))

    letter_len = int(len(letters))-1
    symbol_len = int(len(symbols))-1
    number_len = int(len(numbers))-1
    password_list = []

    for i in range (0, nr_letters):
      letter_place = random.randint(0,letter_len)
      password_list.append(letters[letter_place])

    for i in range (0, nr_symbols):
      symbol_place = random.randint(0, symbol_len)
      password_list.append(symbols[symbol_place])

    for i in range (0, nr_numbers):
      number_place = random.randint(0,number_len)
      password_list.append(numbers[number_place])

    ###Randomize Look
    password_size = int(len(password_list))
    password_str = ""

    for x in range (0, password_size):
      flex_size = int(len(password_list))-1
      position = random.randint(0, flex_size)
      password_str += password_list[position]
      password_list.pop(position)

    password_input.delete(0,END)
    password_input.insert(0, password_str)
    copy(password_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        if len(website) == 0:
            messagebox.showerror(title="Missing Information", message="Please enter a website.")
        elif len(password) == 0:
            messagebox.showerror(title="Missing Information", message="Please enter a password.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmaiL: {email} \nPassword: {password} \n \nVerify and save?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # json.dump(new_data, data_file, indent=4)
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

def search_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            # json.dump(new_data, data_file, indent=4)
            data = json.load(data_file)

        try:
            email = data[website]["email"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showerror(title="Error", message="No such website in database")
        else:
            messagebox.showinfo(title=website, message=f"Email:   {email}\nPassword:  {password} ")
        finally:
            website_input.delete(0, END)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found, nothing stored")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_input = Entry(width=35)
website_input.focus()
website_label.grid(column=0, row=1)
website_input.grid(column=1, row=1)
search_btn = Button(text="Search", width=11, command=search_password)
search_btn.grid(column=3, row=1)

email_label = Label(text="Email/Username:")
email_input = Entry(width=35)
email_input.insert(0, "trylle@glas.dk")
email_label.grid(column=0, row=2)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_input = Entry(width=35)
password_btn = Button(text="Generate", width=11, command=generate_password)
password_label.grid(column=0, row=3)
password_input.grid(column=1, row=3)
password_btn.grid(column=3, row=3)

add_button = Button(text="Add", width=20, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=20)

window.mainloop()
