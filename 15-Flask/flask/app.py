## this is basic web framework by flask 

from flask import Flask

'''
It creates an instance of the Flask class,
which will be your WSGI(Web server Gateway interface) application.
'''

##WSGI Application 
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welecome to this flask course. This should be amazing course sanskar "

@app.route("/index")
def index():
    return "Welecome to index page"


##This is entry point of any py file
if __name__ == "__main__":
    app.run(debug=True)