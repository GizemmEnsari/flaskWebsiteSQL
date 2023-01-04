from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
server_db = SQLAlchemy(app)

class User(server_db.Model):
    pass

class Admin(server_db.Model):
    pass
