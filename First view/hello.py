from flask import Flask

app = Flask(__name__)


def make_bold(fn):
    def wrapper():
        return f"<b>{fn()}</b>"

    return wrapper


def make_em(fn):
    def wrapper():
        return f"<em>{fn()}</em>"

    return wrapper


def make_under(fn):
    def wrapper():
        return f"<u>{fn()}</u>"

    return wrapper


@app.route("/bye")
@make_bold
@make_em
@make_under
def bye():
    return "bye!!"


@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello world!</h1>'
            '<p style="text-align: center">The kitten picture</p>'
            '<img src="https://www.lomsnesvet.ca/wp-content/uploads/sites/21/2019/08/Kitten-Blog-683x1024.jpg" width=200>')


@app.route("/username/<name>/<int:number>")
def call(name, number):
    return f"Hello, my name is  {name} and im {number} years old"


if __name__ == '__main__':
    app.run(debug=True)
