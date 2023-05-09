"""
Prints the number of time you have visited a
particular page within a session. (Implement
using Cookie as well as Flask-Session)

"""

from flask import Flask,render_template,session,make_response,redirect,url_for,request


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


@app.route("/countCookies")
def make_response_Func():
    # Get the current count from the cookie
    cookie_count = request.cookies.get('counting')
    if cookie_count is None:
        cookie_count = 0
    else:
        cookie_count = int(cookie_count)

    # Increment the count and set the cookie
    cookie_count += 1
    res = make_response(render_template("count_cookies.html"))
    res.set_cookie("counting", str(cookie_count))

    return res
# app.run()

