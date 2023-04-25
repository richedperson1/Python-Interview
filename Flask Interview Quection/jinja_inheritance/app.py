from flask import *

app = Flask("__main__")


@app.route("/")
def homePage():
    return render_template("base.html")


@app.route("/index")
def indexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
