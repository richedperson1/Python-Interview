"""
Getting know about jinja templates

1. templates engine : 

    a. These are the files that contain static data along with placeholder 
    for dynamic data.
    b. It's rendered HTML file with specific data

    Example of templates
        i.   Chameleon
        ii.  Cheetah     
        iii. Jinja
        iv.  Juno     
"""


"""
Jinja Templates

1. It look like python only
2. Special delimiters are present in jinja so that every expression writen in right way

    a. {{}}  : Expression for output [act as placeholder for value].
    b. {% %} : Expression for control flow statement like [if ,else, for].
    c. {# #} : Adding comment in the jinja template it will not visible in user side 
               only visible at programmers side.
"""


from flask import *
app = Flask("__main__")


@app.route("/")
def startPage():
    return render_template("index.html")


@app.route("/table", methods=["post"])
def printTable():
    if request.method == "POST":
        tableNum = int(request.form["tableNum"])
        return render_template("table.html", number=tableNum)
    return "Nope"


app.run(debug=True)
