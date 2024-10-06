from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pwd_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers+ password_symbols+password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # Copy password to clipboard
    pyperclip.copy(password)

    # Show "Copied" message
    copied_label.config(text="Copied!")

    # Remove the message after 2 seconds
    window.after(2000, lambda: copied_label.config(text=""))

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # check empty strings
    if len(website) == 0 or len(password)==0:
        messagebox.showerror(title = 'Oops', message="Please don't leave any fields empty!")
    else:
        try:
            # Read the existing passwords from the file
            with open('password.txt', 'r') as pwd_file:
                saved_data = pwd_file.readlines()
        except FileNotFoundError:
            saved_data = []

        # Check if the website already exists
        new_data = f"{website} | {email} | {password}\n"
        for index, line in enumerate(saved_data):
            saved_website = line.split(" | ")[0]
            if saved_website == website:
                # Ask the user if they want to overwrite the existing password
                overwrite = messagebox.askyesno(title='Duplicate Entry',
                                                message=f'You already have a password saved for {website}. Do you want to overwrite it?')
                if overwrite:
                    # Overwrite the existing entry by replacing the old one with the new entry
                    saved_data[index] = new_data
                    with open('password.txt', 'w') as pwd_file:
                        pwd_file.writelines(saved_data)
                    messagebox.showinfo(title='Success', message='Password overwritten successfully!')
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                return

        # If no duplicate is found, confirm and save the new password
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}'
                                                              f"\nPassword: {password} \n Is it ok to save?")
        if is_ok:
            with open('password.txt', 'a') as pwd_file:
                pwd_file.write(new_data)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50, bg=YELLOW)

# canvas setup
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
pwd_image = PhotoImage(file='logo.png')
canvas.create_image(120,100,image=pwd_image)
canvas.grid(column=1,row=0)

# create the labels
# website label
label_web = Label(text="Website", fg = 'black', bg=YELLOW)
label_web.grid(column=0,row=1)

# username label
label_username = Label(text="Email/Username", fg = 'black', bg=YELLOW)
label_username.grid(column=0,row=2)

# password label
label_pwd = Label(text="Password", fg = 'black', bg=YELLOW)
label_pwd.grid(column=0,row=3)

# copied message label
copied_label = Label(text="", fg="green", bg=YELLOW)  # This label will show the "Copied" message
copied_label.grid(column=1, row=5, columnspan=2)

#create entries
website_entry = Entry(width=38, bg=YELLOW, fg='black', highlightbackground=YELLOW, insertbackground="black")
website_entry.grid(column=1,row=1, columnspan=2)
email_entry = Entry(width=38, bg=YELLOW, fg='black', highlightbackground=YELLOW, insertbackground="black")
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, "ying.liu0331@gmail.com")
password_entry = Entry(width=21, bg=YELLOW, fg='black', highlightbackground=YELLOW, insertbackground="black")
password_entry.grid(column=1, row=3)

# create the buttons
button_pwd_generate = Button(text="Generate Password", command=pwd_generate, highlightbackground=YELLOW)
button_pwd_generate.grid(column=2,row=3)

button_add = Button(text="Add", command=save, width=36, highlightbackground=YELLOW)
button_add.grid(column=1,row=4,columnspan = 2)

window.mainloop()
