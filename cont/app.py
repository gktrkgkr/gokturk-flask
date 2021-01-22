import os
import requests
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

PASSWORD = "karadeniz"
PUBLIC_IP_ADDRESS ="34.121.66.9"
DBNAME ="IoT"
PROJECT_ID ="halogen-pier-297117"
INSTANCE_NAME ="halogen-pier-297117:us-central1:smartcampus"

app.config["SECRET_KEY"] = "yoursecretkey"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:karadeniz@34.121.66.9/IoT?unix_socket =/cloudsql/halogen-pier-297117:smartcampus'

db = SQLAlchemy(app)

class contact(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    surname = db.Column(db.Unicode)
    email = db.Column(db.Unicode)
    message = db.Column(db.Unicode)

    def init(self, name, surname, email, message):
        self.name = name
        self.surname = surname
        self.email = email
        self.message = message


@app.route("/")
def aboutme():
    return render_template("aboutme.html")

@app.route("/contactme", methods=['POST', 'GET'])
def contactme():

    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['surname'] or not\
               request.form['email'] or not request.form['message']:
            flash('Please enter all the fields')
        else:
            newlog = contact(name=request.form['name'], surname=request.form['surname'],
                             email=request.form['email'], message=request.form['message'])
            db.session.add(newlog)
            db.session.commit()
            flash("Message sent!")
        return render_template("contactme.html")
    else:
        return render_template("contactme.html")



@app.route("/favs")
def lectures():
    return render_template("lectures.html")

@app.route("/lectures")
def favs():
    return render_template("favs.html")

@app.route("/weather", methods=['POST'])
def weather():
    cityname = request.form['city']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cityname+'&appid=97e933b466c8bbb86bf0e6ab9784ef71')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_c = temp_k - 273.15
    return render_template("weather.html", temp=int(temp_c), cityname=cityname)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)))