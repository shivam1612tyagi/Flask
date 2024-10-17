''' Import the flask class from the flask, redirect & url_for module '''
from flask import Flask, redirect, url_for, render_template, request

#create the instance of the Flask class
app = Flask(__name__)
'''
{%......%} conditions, for loops
{{......}} expressions to print output
{#......#} this is for comments in flask
'''

# define the route for the home page
@app.route('/')
def welcome():
  return render_template('index.html')  # return the welcome message

#define the route for the pass page
@app.route('/sucess/<int:score>')   #Route with a dynamic integer parameter
def sucess(score):
  res = ""
  if score >= 50:
    res = "Pass" 
  else:
    res = "Fail"
  exp = {'score': score, 'resul': res}
  return render_template('result.html', result = exp)  #return a pass message with the score

#define the route for the fail page
@app.route('/fail/<int:score>')
def fail(score):
  return render_template('result.html', score = score) #return a fail message with the score

## Result Checker
@app.route('/submit',methods=['POST','GET'])
def submit():
  total_score = 0
  if request.method == 'POST':
    science = float(request.form['science'])
    maths = float(request.form['maths'])
    c = float(request.form['c'])
    datascience = float(request.form['datascience'])
    total_score = (science+maths+c+datascience)/4
    return redirect(url_for('sucess',score=total_score))

  elif request.method == 'GET':
    science = float(request.args.get('science'))
    maths = float(request.args.get('maths'))
    c = float(request.args.get('c'))
    datascience = float(request.args.get('datascience'))
    total_score = (science+maths+c+datascience)/4
    return redirect(url_for('sucess',score=total_score))

'''
  res = ""
  if total_score >= 50:
    res = "success"
  else:
    res = "fail"
  if res == "success":
    return redirect(url_for('sucess',score=total_score))
'''

#define the main entry point of the application
if __name__ == '__main__':
  app.run(debug = True) #run the falsk application the local development server with debug mode enabled.