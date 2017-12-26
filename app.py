from flask import Flask
from flask import render_template, redirect, flash, request, session, abort
app = Flask(__name__, template_folder="../capstone_react/src/components/")
# console.log(Flask(__name__))
# @app.route('/')
# def hello_world():
#     return 'Hello world hola mundo'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('Login.js')
    else:
        return "Hello Boss!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username']=='admin':
        session['logged_in']= True
    else:
        flash('wrong password!')
        return home()


# from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)
