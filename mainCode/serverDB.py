from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
server_db = SQLAlchemy(app)

class User(server_db.Model):
    id = server_db.Column(server_db.Integer, primary_key=True)
    username = server_db.Column(server_db.String, unique=True, nullable=False)
    password = server_db.Column(server_db.String, unique=True, nullable=False)
    code_seg = server_db.Column(server_db.String)
    personal_code_one = server_db.Column(server_db.String)
    personal_code_two = server_db.Column(server_db.String)
    personal_code_three = server_db.Column(server_db.String)


class Admin(server_db.Model):
    id = server_db.Column(server_db.Integer, primary_key=True)
    admin_name = server_db.Column(server_db.String, unique=True, nullable=False)
    admin_pass = server_db.Column(server_db.String, unique=True, nullable=False)
