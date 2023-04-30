from flask import *

import requests
app = Flask("__main__")


@app.route("/")
def requestDemo():
    rquest = request.__dict__
    # print("----->", rquest["query_string"])
    print("----->", request.args)
    return f"{request.args}"


@app.route("/form")
def requestForm():
    return render_template("inputData.html")
    # print("----->", rquest["query_string"])


# JSON File
@app.route("/jsoninput")
def jsonInput():
    person = {
        "name": "Rutvik",
        "lastName": "Jaiswal",
        "Mobile No.": 9673062604,
        "skills": ["python", "JS", "CSS/HTML", "MySQL"]
    }
    final = requests.post("http://127.0.0.1:5000/jsonProcedure", json=person)
    return str(final.text)+"Hello world"


@app.route("/jsonProcedure", methods=["post"])
def jsonProcedure():
    if request.is_json:
        print("Json found")
        return f"Hello world {request.json}"
    else:
        return "Data not founds"


if __name__ == "__main__":
    app.run(debug=True)
