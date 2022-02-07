from flask import Flask, render_template
from jinja2 import defaults

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/aboutus')
def about():
    return render_template("aboutus.html")


@app.route('/login')
def login():
    return 

@app.route('/user',defaults={'name':'Guest'})
@app.route('/user/<name>')
def user(name):
    context=[
        { 'stuid': '2000042569','stuname': 'Prakash','sub1':89,'sub2':75,'sub3':69 },
        {'stuid': '2000041569', 'stuname': 'Abdul', 'sub1': 58, 'sub2': 79, 'sub3': 59},
        {'stuid': '2000040587', 'stuname': 'Revathi', 'sub1': 89, 'sub2': 87, 'sub3': 69}
    ]
    return render_template('user.html',data = name, con = context)

if __name__ == '__main__':
    app.run(debug=True)