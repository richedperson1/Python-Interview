from flask import Flask, make_response


app = Flask("__main__")


@app.route("/")
def mainPage():
    headers = {
        "password": "125Rutvik"
    }

    return make_response("This response making using make_response api", 202, headers)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
