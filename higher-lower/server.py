import random

from flask import Flask

rand_num = random.randint(0, 9)
app = Flask(__name__)


@app.route("/")
def main():
    return ("<h1 style='text-align: center'>Choose a random number from 0 to 9</h1>"
            "<img src=""https://media2.giphy.com/media/IcifS1qG3YFlS/giphy.gif?cid=ecf05e476kl00hd87reaexeqicio7xqijhn94a46kl30btb2&ep=v1_gifs_search&rid=giphy.gif&ct=g>")


@app.route('/<int:num>')
def random_choose(num):
    if rand_num < num:
        return ("<h1 style='text-align: center'>You are too high bro</h1>"
                "<img src='https://media0.giphy.com/media/MXi8nBJjIBgKbyA1MM/giphy.gif?cid=ecf05e478fycriv5pk6y06ltwimyio5330c4ge7lo5h2ui6o&ep=v1_gifs_search&rid=giphy.gif&ct=g'>")
    elif rand_num > num:
        return ("<h1 style='text-align: center'>You are too low bro</h1>"
                "<img src='https://media2.giphy.com/media/PXGvUV7Znz5wQ/giphy.gif?cid=ecf05e47k5ovhnyrxrqhy4z0tm3y58pukc5rzmqdtdtnfm4p&ep=v1_gifs_search&rid=giphy.gif&ct=g'>")

    else:
        return (f"<h1 style='text-align: center'>You right, it was {rand_num}</h1>"
                "<img src='https://media4.giphy.com/media/i6TiqPLXSRfs2L86fy/giphy.gif?cid=ecf05e479m3wp92fezc28361kyeal0d7kyk29i3eszxesp66&ep=v1_gifs_search&rid=giphy.gif&ct=g'>")


if __name__ == '__main__':
    app.run(debug=True)
