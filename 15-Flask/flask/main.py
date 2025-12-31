## this is basic web framework by flask 

from flask import Flask,render_template

'''
It creates an instance of the Flask class,
which will be your WSGI(Web server Gateway interface) application.
'''

##WSGI Application 
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to flask course</h1></html>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


##This is entry point of any py file
if __name__ == "__main__":
    app.run(debug=True)