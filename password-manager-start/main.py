from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers +password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
   

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pasword():
    
    new_data = {website_entry.get():{
                    "email":username_entry.get(),
                    "password":password_entry.get(),
                    }
                }

    if(website_entry.get() == "" or username_entry.get() == "" or password_entry.get() == "" ):
        messagebox.showerror(title = "oops", message = "Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website_entry.get(), message =  f"username: {username_entry.get()} \nPassword:  {password_entry.get()} \n  Is okay to save?")
        if(is_okay):
            try:
                with open('password.json', "r") as data_file:
                    data = json.load(data_file)
                    
            except:
                 with open('password.json',"w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else: 
             data.update(new_data)          
             with open('password.json',"w") as data_file:
                    json.dump(data, data_file, indent=4)

            website_entry.delete(0,END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search_method():
   
    try:
        with open('password.json', 'r') as data_file:
            data = json.load(data_file)
        website = data[website_entry.get()]
    except KeyError :
         messagebox.showerror(title='oops', message="There no saved username and password for this website")    
    except:
         messagebox.showinfo(title='ops', message="No data file found")
   
    else:
        messagebox.showinfo(title=website, message=f"passward: {website['email']}\n username: {website['password']}")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk() 
window.title('password manager')
window.config(padx = 50,pady = 50, background='white')

canvas = Canvas(width=200, height=200, background='white', highlightthickness=0)
myimg = PhotoImage(file="/home/levi/Documents/website/100 days of python/day_29/password-manager-start/logo.png")
canvas.create_image(100, 100, image =myimg)
canvas.grid(row = 0, column = 1)

website_label = Label(text="Website", background='white',pady = 3)
website_label.grid(row = 1, column = 0)

username_label = Label(text="Email/Username", background='white',pady = 3)
username_label.grid(row = 2, column = 0)

password_label = Label(text="Password", background='white',pady = 7, height = 1)
password_label.grid(row = 3, column = 0)

website_entry = Entry(width = 25, background='white')
website_entry.focus()
website_entry.grid(row = 1, column = 1)

search = Button(width = 8, text = "search", background='white', command = search_method)
search.grid(row = 1, column = 2)

username_entry = Entry(width = 39, background='white' )
username_entry.insert(0, "lewi@gmail.com")
username_entry.grid(row = 2, column = 1, columnspan = 2)


password_entry = Entry(width = 25, background='white' )
password_entry.grid(row = 3, column = 1)

generate = Button(text="Generate PW", background='white', command = generate_password)
generate.grid(row = 3, column = 2)

add = Button(text="Add", background='white', command=save_pasword, width = 37)
add.grid(row = 4, column = 1, columnspan=2)

window.mainloop()