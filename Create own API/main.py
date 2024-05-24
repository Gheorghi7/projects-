import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
API_KEY = '1iacepttodeletethisone1'


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def rand_coffe():
    caffe_db = db.session.execute(db.select(Cafe))
    all_cafes = caffe_db.scalars().all()
    rand_choice = random.choice(all_cafes)

    return jsonify(rand_choice.to_dict())


@app.route('/all')
def get_all():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(caffe=[caffe.to_dict() for caffe in all_cafes])


@app.route('/search')
def search():
    query_loc = request.args.get('loc')
    caffe_db = db.session.execute(db.select(Cafe).where(Cafe.location == query_loc))
    all_cafes = caffe_db.scalars().all()
    if all_cafes:
        return jsonify(all_cafes=[cafes.to_dict() for cafes in all_cafes])
    else:
        return jsonify(errors={'Not found': 'Sorry we dont have a caffe at the location'})


@app.route('/add', methods=['POST'])
def post_req():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route('/update-price/<int:coffe_id>', methods=['PATCH'])
def update(coffe_id):
    new_price = request.args.get('new_price')
    user = db.get_or_404(Cafe, coffe_id)
    if user:
        user.coffe_price = new_price
        db.session.commit()
        return jsonify(error={'Success': 'Successfully updated the price'})
    else:
        return jsonify(error={'Error': 'somthing went wrong'})


@app.route('/report-closed/<coffe_id>', methods=['DELETE'])
def delete(coffe_id):
    secret_key = request.args.get('GetSecretAPIKey')
    cafes = db.get_or_404(Cafe, coffe_id)
    if cafes:
        if secret_key == API_KEY:
            db.session.delete(cafes)
            db.session.commit()
            return jsonify(success={'Success': 'Cafes closed successfully'})
        else:
            return jsonify(error={'KeyError': 'Your key is not correct'})
    else:
        return jsonify(error={'IdNotExist': 'Cafes with this id is not exist'})


# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
