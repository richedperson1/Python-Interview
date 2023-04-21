from flask import *

app = Flask(__name__)


@app.route("/")
def homePage():
    return render_template("index.html")


@app.route('/success/<name>')
def successING(name):
    return 'welcome %s' % name


@app.route("/login", methods=["POST"])
def loging_page():
    if request.method == "POST":
        name = request.form["nameOfLogin"].lower()
        password = request.form["loginPass"]
        if name == "rutvik":
            return "Welcome sir, You got want you want"

        return redirect(url_for("successING", name=name))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
