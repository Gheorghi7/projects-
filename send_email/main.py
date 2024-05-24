from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(template_name_or_list='index.html')


@app.route('/login', methods=['POST'])
def recive_data():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        return f"Name is {name} Password is {password}"


if __name__ == '__main__':
    app.run(debug=True)
