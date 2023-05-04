from flask import session, redirect, url_for, render_template, Flask, request
from flask_caching import *
# from flask_cachecontrol import *

app = Flask(__name__)

app.secret_key = "ilove1506!JaiPatil"
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@cache.cached(timeout=60)
@app.route("/", methods=['POST', 'GET'])
def homeIndex():
    if request.method == "POST":
        userName = request.form["username"]
        passWord = request.form["password"]
        print("Username", "--"*5, userName)
        print("passWord", "--"*5, passWord)
        session["username"] = "Rutvik Jaiswal"
        if userName == "ru" and passWord == "12":
            return redirect(url_for("homePage"))

        return render_template("loginPage.html")

    else:
        if "username" in session:
            return redirect(url_for("homePage"))
        return render_template("loginPage.html")


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers.add(
        'Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return response


@app.route("/home", methods=["GET"])
def homePage():
    if request.method=="GET":
        if "username" in session:
            return render_template("index.html")
        else:
            return redirect(url_for("homeIndex"))


@app.route("/greeting")
def greetingForOther():
    if "username" in session:
        return "<h1> Hello my self Rutvik</h1>"
    return redirect(url_for("homeIndex"))
    

@app.route("/logOut", methods=["POST", 'GET'])
def logoutBtn():
    if request.method == "POST":
        session.pop("username")
        return redirect(url_for("homeIndex"))

    session.clear()

    return redirect(url_for("homeIndex"))


if __name__ == "__main__":
    app.run(debug=True)
