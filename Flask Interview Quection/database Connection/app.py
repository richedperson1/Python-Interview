from flask import (Flask,request,render_template,redirect,session,url_for)
import sqlite3

app = Flask(__name__)

app.secret_key = "asjdfkjasndckjshdf"

connection = sqlite3.connect("first.db")
# connection.execute("DROP TABLE STUDENT")
connection.execute("CREATE TABLE IF NOT EXISTS STUDENT(email TEXT,first_name TEXT,last_name TEXT,password text)")
connection.close()

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers.add(
        'Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return response

@app.route("/")
def homePage():
    if "username" in session:
        return render_template("home_page.html")
    return redirect(url_for("loginPage"))


@app.route("/logOut")
def logOutFun():
    session.pop("username")
    return redirect(url_for("homePage"))


@app.route("/login")
def loginPage():
    return render_template("login.html")

@app.route("/authetication",methods = ["post"])
def autheticationPage():
    userEmail = request.form.get("EmailName")
    password = request.form.get("PasswordName")
    final = ""
    with sqlite3.connect("first.db") as conn:
        cursor = conn.cursor()
        query = f"select * from STUDENT where email =='{userEmail}' and password = '{password}'"
        cursor.execute(query)
        final = cursor.fetchall()
    if len(final)>0:
        session["username"] = userEmail
        return redirect(url_for("homePage"))
    
    return redirect(url_for("loginPage"))

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/showData")
def showData():
    if "username" in session:
        final = ""
        ans = []
        with sqlite3.connect("first.db") as conn:
            conn.row_factory = sqlite3.Row

            cursor = conn.cursor()

            query = "select * from STUDENT"
            cursor.execute(query)
            final1 = cursor.fetchall()
            for tt in final1:
                for t1 in tt:
                    ans.append(t1)
                print(tt)
        if ans!=[] or ans!="":
            return str(ans)
        return "Not found data yet"
    return redirect(url_for("homePage"))


@app.route("/addingData",methods = ["post"])
def addingStudent():
    if request.method=="POST":
        # try:
            emailId   = request.form.get("email")
            firstName = request.form.get("first-name")
            LastName  = request.form.get("last-name")
            password  = request.form.get("password")
            print(emailId,firstName,LastName,password)
            with sqlite3.connect("first.db") as conn:
                cursor = conn.cursor()
                query = f"""
                        INSERT INTO STUDENT 
                        (email, first_name, last_name, password) VALUES 
                        ('{emailId}', '{firstName}', '{LastName}', 
                        '{password}');
                        """
                print(query)
                cursor.execute(query)
                conn.commit()
            
            return redirect(url_for("loginPage"))
        # except:
        #     return  "not able to load data into the database"
    return "Not found"
       
if __name__=="__main__":
    app.run(debug=True,port=4000)