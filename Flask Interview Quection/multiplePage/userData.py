from app import app
# from 
import sys
# print(sys.path)
# print(app)
@app.route("/hello")
def helloWord():
    return "Hello world from userData files"



@app.route("/not")
def notFound():
    return "First page loading"