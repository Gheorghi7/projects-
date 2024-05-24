import random
from tkinter import *
from tkinter import messagebox
import json

# constants
image = 'logo.png'
FONT = 'Ariel'
FONT_SIZE = 15
FONT_TYPE = 'normal'
#Seaching
def search_web():
    with open('data.json', mode='r') as read_js:
        data = json.load(read_js)
        if website_entry.get() in data:
            messagebox.showinfo(title=f"{website_entry.get().capitalize()}", message=f"Email: {data[website_entry.get().lower()]['email']}\nPassword: {data[website_entry.get().lower()]['password']} ")
        else:
            messagebox.showinfo(title='Notification', message='Website is not found')



# generator
alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w',
       'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
       'T',
       'U', 'V', 'W', 'X', 'Y', 'Z']


def generate():
    password_entry.delete(0, END)
    res = ''
    while len(res) < 10:
        res += random.choice(alf)
        res += str(random.randint(1, 9))
    password_entry.insert(0, res)
    return


# file
def write_in_file():
    new_dict = {website_entry.get().lower():{
        'email':email_enty.get().lower(),
        'password':password_entry.get(),
    }}
    if len(email_enty.get()) == 0 or len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        return messagebox.showinfo(title='Notification', message='Please dont leave any fields empty!!')
    elif messagebox.askokcancel(title='Save or not',
                                message=f"There are the details entered \nWebsite: {website_entry.get()}"
                                        f"\nEmail: {email_enty.get()}"
                                        f"\nPassword: {password_entry.get()}"):
        try:
            with open('data.json', mode='r') as wr_file:
                data = json.load(wr_file)
        except FileNotFoundError:
            with open('data.json', mode='w') as wr_file:
                json.dump(new_dict,wr_file, indent=4)
        else:
            data.update(new_dict)
            with open('data.json', mode='w') as wr_file:
                json.dump(data, wr_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title='notification', message='Your data has been added successfully♥')


# window
window = Tk()
window.title('Password Generate')
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=image)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website = Label(text='Website:', font=('Arial', 15, 'normal'))
website.grid(row=1, column=0)
email = Label(text='Email/Name:', font=('Ariel', 15, 'normal'))
email.grid(row=2, column=0)
password = Label(text='Password:', font=('Ariel', 15, 'normal'))
password.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=1)
email_enty = Entry(width=50)
email_enty.insert(0, 'GheorghiTacu@gmail.com')
email_enty.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1,columnspan=1)

# Button
gen = Button(text='Generate', width=10, command=generate)
gen.grid(row=3, column=2)

add = Button(text='Add', width=40, command=write_in_file)
add.grid(row=4, column=1, columnspan=2)

search = Button(text ='Search', width =10, command=search_web)
search.grid(row=1, column=2, columnspan=2)
window.mainloop()
