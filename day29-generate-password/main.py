from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip  # for automatic copy vins kope tekstu kuru tu izvelies iekavas
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_letter = [choice(letters) for char in range(randint(8, 10))]  # !!!!!!!!!!!!!!!
    new_symbol = [choice(symbols) for char2 in range(randint(2, 4))]
    new_number = [choice(numbers) for char3 in range(randint(2, 4))]  # choice vnk jo random.choice vnk importojam choice nevis random

    com = new_letter + new_symbol + new_number
    shuffle(com)

    # password = ""
    # for char in com:
    #   password += char  VAR VKN USE .join !!!!!!!!!!!!!!!!!

    password = "".join(com)  # JOIN function
    password_input.insert(0, password)  # to inster in password input nevar izmantot CONFIG
    pyperclip.copy(password)  # copy password tekstu kad tiek runnots šis generate_password function


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    # messagebox.showinfo(title="Title",message="Message")
    new_data = {
        website: {
            'email': email,
            'password': password,

        }}

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open('data.json', mode='r') as data_file:  # mode = a  appendo klat tekstam
                # json.dump(new_data, data_file, indent=4) # data_file as the location we want to dump this new_data | indent how much indent EASIER TO READ
                # Reading old data
                data = json.load(data_file)  # load to read from it json file and open mode nomaini uz 'r' lai from write mode to read mode
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', mode='w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)  # deletes first word un replace ar END taka end text un jo ir tuks teksts vnk rakstas pa jaunam
            password_input.delete(0, END)




def find_password():
    # messagebox.showinfo(title="Title",message="Message")
    web_inp = website_input.get()
    try:
        with open("data.json", 'r') as check:
            data = json.load(check)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message="No details for the website exists")
    else:
        if web_inp in data:

            email = data[web_inp]['email']
            password = data[web_inp]['password']
            messagebox.showinfo(title=web_inp, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {web_inp} exists.")



        # messagebox.showinfo(show_info)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
password_input = Entry(width=30)
password_input.grid(row=3, column=1)

email_username_input = Entry(width=49)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0, 'email')  # inserts at that spot 0(where),then (where)also END to have it at end of the word like - emasmdmdsd| un beigas rakstitu

website_input = Entry(width=30)
website_input.grid(row=1, column=1, columnspan=1)
website_input.focus()  # when launch app cursor automatically is in it

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=15, command=find_password)
search.grid(row=1, column=2)

window.mainloop()
