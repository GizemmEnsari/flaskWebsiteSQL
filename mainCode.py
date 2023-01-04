from subprocess import PIPE, STDOUT, run
from flaskWebsiteSQL.serverDB import User, Flask, SQLAlchemy, app, server_db, render_template, request, redirect, url_for
global usr

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/checkCredentials", methods=["POST","GET"] )
def checkCredentials():
    if request.method=="POST":
        inptUsrnm = request.form["username"]
        inptPswrd = request.form["password"]
        if inptUsrnm == "" or inptPswrd == "":
            return render_template("login.html",note="Error, No Entry")
        else:
            usr = User.query.filter_by(username = inptUsrnm).first()
            if usr == None:
                return render_template("login.html", note = "error, username not found")
            else:
                if inptPswrd == usr.password:
                  #  print("giz")
                    return render_template("index.html", username = inptUsrnm ,note = "logged in as "+ inptUsrnm)
                else:
                    return render_template("index.html" , note = "Error, wrong password or username ")

@app.route("/createUser",methods=["GET","POST"])
def createUser():

    if request.method == "POST":
    #    print("post")
        inptUsrnm = request.form["username"]
        inptPswrd = request.form["password"]
    if inptUsrnm == "" or inptPswrd == "":
        return render_template("login.html", message = "Error, no entry")

    if inptUsrnm != "" and inptPswrd != "":
        usr = User.query.filter_by(username=inptUsrnm).first()
        if usr != None:
            return render_template("login.html", message = "Error, this user already exists")
        user = User(
            username = inptUsrnm,
            password = inptPswrd,
            #generalCodeSpace='',
            #personalCodeSpace1='',
        )
        server_db.session.add(user)
        server_db.session.commit()
        print(user)
#         print("KKJ")
        return render_template("index.html", username = inptUsrnm)
   # print("retttt")
    return render_template("index.html", username = inptUsrnm)
# print("fssfs")


@app.route("/logout", methods=["POST","GET"] )
def logout():
    return render_template("login.html")

@app.route("/enterCode", methods=["POST","GET"])
def enterCode():
    pass


@app.route("/myProfile",methods=["POST", "GET"])
def myProfile():
    global usr
    if request.method == "POST":
        inptUsrnm = User.query.filter_by(username = )
        return render_template("myProfile.html", inptUsrnm)

def main():
    with app.app_context():
        server_db.create_all()
    app.run(debug = True)