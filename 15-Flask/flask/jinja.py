# Building Url Dynamically 
## Variable rule
### Jinja 2 Template Engine

## Jinga2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loop, if condition, while condition
{#...#}this is for comments


'''


from flask import Flask,render_template,request

'''
It creates an instance of the Flask class,
which will be your WSGI(Web server Gateway interface) application.
'''

##WSGI Application 
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to flask course</h1></html>"

@app.route("/index",methods=['GET'])                ## by default it is get method
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template("form.html")

# ## Variable run 
# @app.route('/success/<score>')
# def success(score):
#     return "The marks you got is " + score

# ## Variable run 
# @app.route('/success/<int:score>')
# def success(score):
#     return "The marks you got is " + str(score)


##Building url dynamically

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result.html',results = res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp={'score':score,'res':res}

    return render_template('result1.html',results = exp)


##This is entry point of any py file
if __name__ == "__main__":
    app.run(debug=True)