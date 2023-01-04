#from mainCode.serverDB import Flask, SQLAlchemy, app, User, Admin, render_template, url_direct
from serverDB import  app, server_db
from subprocess import PIPE, STOUT, run

@app.route("/", methods = ["POST"])
def index():
    return ("Hello")

def main():
    with app.app_context():
        server_db.create_all()
    app.run(debug = True)