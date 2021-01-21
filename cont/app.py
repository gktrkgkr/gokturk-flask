import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask import request

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:karadeniz@34.121.66.9/IoT'
cors = CORS(app)

db = SQLAlchemy(app)

class contact(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    surname = db.Column(db.Unicode)
    email = db.Column(db.Integer)
    message = db.Column(db.Unicode)

    def init(self, name, surname, email, message):
        self.name = name
        self.surname = surname
        self.email = email
        self.message = message


@app.route("/")
def aboutme():
    return render_template("aboutme.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/favs")
def lectures():
    return render_template("lectures.html")

@app.route("/lectures")
def favs():
    return render_template("favs.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)))