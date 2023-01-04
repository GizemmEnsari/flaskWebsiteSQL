from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
server_db = SQLAlchemy(app)

class User(server_db.Model):
        id = server_db.Column(server_db.Integer, primary_key = True)
        username = server_db.Column(server_db.String,unique = True , nullable = False)
        password = server_db.Column(server_db.String,unique = True, nullable = False )
        #generalCodeSpace = server_db.Column(server_db.String)
        # personalCodeSpace1 = server_db.Column(server_db.String)
        # personalCodeSpace2 = server_db.Column(server_db.String)
        # personalCodeSpace3 = server_db.Column(server_db.String)
        #level = server_db.Column(server_db.Integer)


exampleCodeQA = ["write a code that contains an if statement" , "write a code that contains a for loop", "write a\
                 code that contains a while loop", "write the same code inside of a function", "make your code more \
                 usable, and create a class and gg"]
# class Admin(server_db.Model):saa2
#         pass
