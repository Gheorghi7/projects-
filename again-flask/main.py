import datetime
import requests

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template(template_name_or_list='hello.html', year=current_year)


@app.route('/guess/<name>')
def any_name(name):
    gender = requests.get(f'https://api.genderize.io?name={name}')
    response = requests.get(f'https://api.agify.io?name={name}')
    data = response.json()
    data_gender = gender.json()
    return render_template(template_name_or_list='api.html', person_name=name, gender=data_gender['gender'],
                           data=data['age'])


@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    data = response.json()
    return render_template(template_name_or_list="blog.html", data_file=data)


if __name__ == "__main__":
    app.run(debug=True)
