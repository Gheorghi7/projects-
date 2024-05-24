import random
from tkinter import *

import pandas

data = pandas.read_csv('Untitled spreadsheet - Sheet1.csv')
to_learn = data.to_dict(orient='records')
choose = random.choice(to_learn)


def chenge_to_eng():
    canvas.itemconfig(up_text, text='English', fill='white')
    canvas.itemconfig(down_text, text=f"{choose['English']}", fill='white')
    canvas.itemconfig(fr, image=bg_image)
    print('True')
    window.after(3000, chenge_to_fr)


def chenge_to_fr():
    canvas.itemconfig(up_text, text='French', fill='black')
    canvas.itemconfig(down_text, text=f"{choose['French']}", fill='black')
    canvas.itemconfig(fr, image=fr_image)
    print('False')
def is_know():
    to_learn.remove(choose)
    print(len(to_learn))
    chenge_to_eng()


window = Tk()
window.config(bg='lightblue', pady=50, padx=25)
window.title('Flash card app')

# Images
bg_image = PhotoImage(file='card_back.png')
fr_image = PhotoImage(file='card_front.png')
right = PhotoImage(file='right.png')
wrong = PhotoImage(file='wrong.png')

# Canvas
canvas = Canvas(width=900, height=700, bg='lightblue', highlightthickness=0)
bg = canvas.create_image(450, 350, image=bg_image)
fr = canvas.create_image(450, 350, image=fr_image)
up_text = canvas.create_text(450, 200, text='', font=('Ariel', 40, 'italic'))
down_text = canvas.create_text(450, 400, text=f"", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# buttom
right_bt = Button(image=right, highlightthickness=0, command=is_know)
right_bt.grid(row=1, column=1)
wrong_bt = Button(image=wrong, highlightthickness=0, command=chenge_to_eng)
wrong_bt.grid(row=1, column=0)

window.mainloop()
