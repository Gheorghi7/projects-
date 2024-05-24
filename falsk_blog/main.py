from flask import Flask, render_template
import requests
from post import  Post
app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    data = response.json()
    return render_template("index.html", data=data)


@app.route('/post/<int:id>')
def post(id):

    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    data = response.json()
    return render_template("post.html", data=data, id_person=id)


if __name__ == "__main__":
    app.run(debug=True)
