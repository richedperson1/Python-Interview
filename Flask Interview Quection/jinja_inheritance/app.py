from flask import *

app = Flask("__main__")


@app.route("/")
def homePage():
    return render_template("base.html")


@app.route("/index")
def indexPage():
    return render_template("index.html")


@app.route("/template_var")
def template_var():
    password1 = "Rutvik123654987"
    name1 = "Rutvik"
    userName1 = ["Rutvik_Jaiswal", "Rutvik"]
    contain = {"password": password1, "name": name1, "userName": userName1}
    return render_template("control_statement.html", context=contain)


if __name__ == "__main__":
    app.run(debug=True)
