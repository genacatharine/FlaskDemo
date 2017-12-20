from flask import Flask
from flask import render_template
app = Flask(__name__)
# console.log(Flask(__name__))
@app.route('/')
def hello_world():
    return 'Hello world hola mundo'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User {}'.format(username)

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)
