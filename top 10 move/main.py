from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = '815a138500b196fa87e6c398d3db3b1d'
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
db = SQLAlchemy()
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


class Edit(FlaskForm):
    change_rating = StringField('Rating')
    review = StringField('Review')
    submit = SubmitField('Save')


class AddMove(FlaskForm):
    title = StringField('Movie title')
    submit = SubmitField('Done')


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


#
# @app.route("/add", methods=["GET", "POST"])
# def add_movie():
#     form = AddMove()
#     return render_template("add.html", form=form)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    flask_edit = Edit()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if flask_edit.validate_on_submit():
        movie.rating = float(flask_edit.change_rating.data)
        movie.review = flask_edit.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=flask_edit)


@app.route('/delete')
def delete_movie():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/find')
def find_movie():
    movie_id = request.args.get('id')
    if movie_id:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}",
                                params={'api_key': API_KEY, 'language': 'en-US'})
        data = response.json()
        print(data)
        tst = Movie(
            title=data['title'],
            year=data['release_date'].split('-')[0],
            img_url=f"https://image.tmdb.org/t/p/original/{data['poster_path']}",
            description=data['overview']
        )
        db.session.add(tst)
        db.session.commit()
        return redirect(url_for('edit', id=tst.id))


@app.route('/add', methods=['POST', 'GET'])
def add_movie():
    form = AddMove()
    if form.validate_on_submit():
        ##REQUEST API
        response = requests.get('https://api.themoviedb.org/3/search/movie',
                                params={'query': form.title.data, 'api_key': API_KEY})
        data = response.json()["results"]
        return render_template('select.html', options=data)

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
