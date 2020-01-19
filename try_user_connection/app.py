from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
db = SQLAlchemy(app)


from models import *

@app.route('/')
def hello():
    return render_template("home.html")

@app.route("/get_book_/<number>")
def get_book_name(number):
    return "room : {}".format(number)

@app.route("/details")
def get_book_details():
    number = request.args.get('number')
    floor = request.args.get('floor')
    return "number : {}, floor: {}".format(number, floor)

@app.route("/rooms/get_all_rooms")
def get_all_rooms():
    try:
        rooms = Living_room.query.all()
        return jsonify([room.serialize() for room in rooms])
    except Exception as e:
        return(str(e))

@app.route("/rooms/get_room_by_number/<m_number>")
def get_room_by_number(m_number):
    try:
        room = Living_room.query.filter_by(room_number = m_number).first()
        return jsonify(room.serialize())
    except Exception as e:
        return(str(e))

# @app.route('/llr')
# def list_living_rooms():
#     rooms = Living_room.query.all()
#     return rooms

if  __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
