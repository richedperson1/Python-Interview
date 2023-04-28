from flask import *


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


if __name__ == "__main__":
    app.run(debug=True)
