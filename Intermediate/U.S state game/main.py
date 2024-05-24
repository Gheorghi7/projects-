import pandas
import turtle

screen = turtle.Screen()
screen.title('U.S States Game')
data = pandas.read_csv('50_states.csv')
image = 'blank_states_img.gif'
states = data['state']
game = True
screen.addshape(image)
count = 0
turtle.shape(image)
arr = []
arr_turtle = []
while game:
    answer_state = screen.textinput(f"{count}/50 Guess the state", "What`s another state`s name:")
    if answer_state == '' or count == 50:
        game = False

    for st in states.array:
        if answer_state.capitalize() == st and answer_state not in arr:
            tim = turtle.Turtle()
            tim.up()
            tim.hideturtle()
            x = data[data['state'] == st]
            tim.goto(*x['x'].values, *x['y'].values)
            tim.write(st, align='center',font=('Ariel', 10, 'normal'))
            arr_turtle.append(tim)
            count += 1
            arr.append(answer_state)
            print(answer_state.capitalize())
turtle.mainloop()
