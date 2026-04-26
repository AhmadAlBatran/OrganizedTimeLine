import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(240))
    date = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


@app.route("/")
def hello():
    return "Welcome to Organized Time Line. "


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    # Check if username already exists
    existing_user = User.query.filter_by(username=data["username"]).first()
    if existing_user:
        return jsonify({"message": "Username already taken"}), 409

    user = User(username=data["username"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    if user.password != data["password"]:
        return jsonify({"message": "Wrong password"}), 401

    return jsonify({"message": "Login attempt successful"}), 200


@app.route("/create_event", methods=["POST"])
def create_event():
    data = request.get_json()
    event = Event(
        header=data["header"],
        description=data["description"],
        date=datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S"),
        duration=data["duration"],
        user_id=data["user_id"],
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({"message": "Event Created"}), 201


@app.route("/read_event", methods=["GET"])
def read_event():
    data = request.get_json()
    event = Event.query.filter_by(user_id=data["user_id"], id=data["id"]).first()

    if not event:
        return jsonify({"message": "Event not found"}), 404

    return jsonify(
        {
            "id": event.id,
            "header": event.header,
            "description": event.description,
            "date": event.date,
            "duration": event.duration,
            "user_id": event.user_id,
        }
    ), 200


@app.route("/delete_event", methods=["DELETE"])
def delete_event():
    data = request.get_json()
    db.session.delete(Event.query.filter_by(id=data["id"]).first())
    db.session.commit()

    return jsonify({"message": "Event Deleted By ID"}), 200


@app.route("/update_event", methods=["PUT"])
def update_event():
    data = request.get_json()
    event = Event.query.filter_by(id=data["id"]).first()

    if not event:
        return jsonify({"message": "Event not found"}), 404

    event.header = (data["header"],)
    event.description = data["description"]
    event.date = datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S")
    event.duration = data["duration"]

    db.session.commit()

    return jsonify({"message": "Event_updated"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
