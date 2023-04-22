"""
Route Parameter Passing 
( Dynamic Page loading )

This generally useful for those who have alot of customer and each customer need to show different different contect 
Ex. Name, Email ID, Mobile number
"""


from flask import *

app = Flask(__name__)

# Home page rendering


@app.route("/home/")
def homePageLoading():
    return "Home page of guest"


@app.route("/home/<int:age>")
def homeAgeWise(age):
    age = int(age)
    if age < 20:
        return "You are not allowed"
    return "You are welcome"


@app.route("/index/page<int:num>")
def indexPageNum(num):
    return f"This blog is for {num}"


@app.route("/get_param/")
def gettingParam():
    print(request.query_string)
    return str(request.query_string)+"Hello world"


@app.route("/homeUrl/")
def homeUrl():
    return redirect(url_for("gettingParam", first="Rutvik", Last="Jaiswal"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
