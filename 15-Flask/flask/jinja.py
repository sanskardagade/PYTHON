# Building Url Dynamically 
## Variable rule
### Jinja 2 Template Engine

## Jinga2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loop, if condition, while condition
{#...#}this is for comments


'''


from flask import Flask,render_template,request,redirect,url_for

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


# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method == 'POST':
#         name=request.form['name']
#         return f'Hello {name}!'
#     return render_template("form.html")

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


## if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',result=score)

    


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',result=score)



@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))



##This is entry point of any py file
if __name__ == "__main__":
    app.run(debug=True)