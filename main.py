from flask import Flask, render_template, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import requests
import json


app = Flask(__name__)

app.secret_key = os.urandom(24)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text)
    time = db.Column(db.Text)
    description = db.Column(db.Text)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/process", methods=["GET", "POST"])
def create_note():


  if request.method == "GET":
        return render_template("create_note.html")
  else:
        date = request.form["date"]
        time = request.form["time"]
        description = request.form["description"]

        note = Note(date=date, time=time, description=description)

        db.session.add(note)
        db.session.commit()

        return jsonify({'note' : note})


        # return redirect("/notes/create")


if __name__ == "__main__":
    app.run(debug=True)