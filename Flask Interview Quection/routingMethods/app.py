from flask import Flask, make_response, render_template


app = Flask("__main__")


@app.route("/")
def mainPage():
    headers = {
        "password": "125Rutvik"
    }

    return make_response("This response making using make_response api", 202, headers)


# If we are giving post method then user need to give only post method
# for routing
@app.route("/helloworld", methods=["post", "get"])
def startUsingHello():
    return "<h1>Hello world</h1>"
# By default get method is present in the API


@app.route("/home")
def homePage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
