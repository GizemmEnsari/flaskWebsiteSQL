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
            if usr == None: # user credentials not in database
                return render_template("login.html", note = "error, username not found")
            else:
                if inptPswrd == usr.password:
                    return render_template("index.html", username = inptUsrnm ,note = "logged in as "+ inptUsrnm)
                else:
                    return render_template("index.html" , note = "Error, wrong password or username ")

@app.route("/createUser",methods=["GET","POST"])
def createUser():

    if request.method == "POST":
        inptUsrnm = request.form["username"]
        inptPswrd = request.form["password"]
    if inptUsrnm == "" or inptPswrd == "":
        return render_template("login.html", message = "Error, no entry")

    if inptUsrnm != "" and inptPswrd != "":
        usr = User.query.filter_by(username=inptUsrnm).first()
        if usr != None:  # if user already exists
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
        return render_template("index.html", note = "account created as "+ inptUsrnm)
    return render_template("index.html", note = "account created as "+ inptUsrnm)


@app.route("/logout", methods=["POST","GET"] )
def logout():
    return render_template("login.html")

@app.route("/runCode", methods=['POST', 'GET'])
def runCode():
    if request.method == 'POST':
        code = request.form["enterCode"]
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("index.html", print_output=output, codearea=code)
    else:
        return render_template("index.html")

@app.route("/enterCode", methods=["POST","GET"])
def enterCode():
    pass

@app.route("/mySpace1" , methods = ["POST", "GET"])
def mySpace1():
    return render_template("space1.html" )


@app.route("/mySpace2", methods = ["POST","GET"])
def mySpace2():
    return render_template("space2.html")

@app.route("/mySpace3",methods = ["POST", "GET"])
def mySpace3():
    return render_template("space3.html")


@app.route("/myProfile",methods=["POST", "GET"])
def myProfile():
    #global usr
    if request.method == "POST":
        return render_template("myProfile.html", inptUsrnm = usr.username)
    pass

def main():
    with app.app_context():
        server_db.create_all()
    app.run(debug = True)