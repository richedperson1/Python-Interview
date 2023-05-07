"""
Prints the number of time you have visited a
particular page within a session. (Implement
using Cookie as well as Flask-Session)

"""

from flask import Flask,render_template,session,make_response,redirect,url_for


app = Flask(__name__)

app.secret_key = "asdfkhasjkdcnkjasdhfuh4651646"
@app.route("/")
def homePage():
    return render_template("home.html")


@app.route("/count")
def countingPageView():

    if "count" in session:
        session["count"]+=1
    else:
        session["count"] = 0

    return render_template("count.html")


@app.route("/hello_fun",methods = ["post"])
def heelo():
    return "Hellow"

@app.route("/reponse")
def make_response_Func():
    a = make_response(redirect(url_for("heelo")))
    
    return "Hello "

app.run()

