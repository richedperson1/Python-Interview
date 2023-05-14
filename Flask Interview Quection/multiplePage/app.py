from flask import Flask


app = Flask(__name__)


@app.route("/")
def IndexPage():
    return "First page loading"

import userData 

if __name__=="__main__":
    app.run(debug=True)