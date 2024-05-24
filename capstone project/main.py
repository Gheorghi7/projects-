from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
date_for_post = date.today().strftime('%B %d, %Y')


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ck = CKEditor()
ck.init_app(app)


class Form(FlaskForm):
    title = StringField('The blog post title')
    subtitle = StringField('The subtitle')
    author = StringField("The author's name")
    img_url = StringField('A URL for the background image')
    body = CKEditorField('The body (the main content) of the post')
    submit = SubmitField('Submit post')


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    db_posts = db.session.execute(db.select(BlogPost))
    all_db_posts = db_posts.scalars().all()
    for post in all_db_posts:
        posts.append(post)

    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<post_id>', methods=['POST', 'GET'])
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)

    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new_post', methods=['POST', 'GET'])
def add_new_post():
    flask_form = Form()
    if flask_form.validate_on_submit():
        new_post = BlogPost(
            title=flask_form.title.data,
            subtitle=flask_form.subtitle.data,
            body=flask_form.body.data,
            author=flask_form.author.data,
            img_url=flask_form.img_url.data,
            date=date_for_post
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=flask_form)


# TODO: edit_post() to change an existing blog post
@app.route('/edit/<post_id>', methods=['POST', 'GET'])
def edit(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = Form(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=edit_form, is_edit=True)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>')
def delete(post_id):
    del_post = db.get_or_404(BlogPost, post_id)
    db.session.delete(del_post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
