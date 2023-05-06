from flask import render_template,redirect,Flask


app = Flask(__name__)

@app.route("/home")
def homePage():
    return "Hello world"

"""
Only error status alloweb in error handler if we put 2xx,1xx,3xx series it will raise the error

only 4xx or 5xx series is allowed in error handler
"""
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404


if __name__=="__main__":
    app.run(debug=False)