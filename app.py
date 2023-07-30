# Create a simple flask application

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import logging
logging.basicConfig(filename="flaskdemo.log", level=logging.INFO)

# create the flask app
# # you can have any name to create flask app.
# app = Flask(__name__)

# create an instance of the Flask application app and name it my_flask_app
my_flask_app = Flask(__name__)


@my_flask_app.route('/')
def home():
    logging.info(
        f"#### You Requested Code to Execute Method:'GET', Received-URL:'/', function-to-run:home() ####")
    return "<h1>Hello, World!</h1>"


@my_flask_app.route('/welcome')
def welcome():
    logging.info(
        f"#### You Requested Code to Execute Method:'GET', Received-URL:'/welcome', function-to-run:welcome() ####")
    return "Welcome to the Flask Tutorials"


@my_flask_app.route('/useredirect')
def useredirect():
    logging.info(
        f"#### You Requested Code to Execute Method:'GET', Received-URL:'/useredirect', function-to-run:useredirect() ####")
    urlvariable = "success"
    logging.info(f"you are being Re-directed to {urlvariable} ")
    return redirect(url_for(urlvariable, score=75))


@my_flask_app.route('/index')
def index():
    logging.info(
        f"## You Requested Code to Execute Method:'GET', Received-URL:'/index', function-to-run:index() ##")
    return render_template('index.html')


@my_flask_app.route('/success/<int:score>')
def success(score):
    logging.info(
        f"## You Requested Code to Execute Method:'GET', Received-URL:'/success', function-to-run:success() ##")
    return "The person is passed and the score is "+str(score)


@my_flask_app.route('/fail/<int:score>')
def fail(score):
    logging.info(
        f"## You Requested Code to Execute Method:'GET', Received-URL:'/fail', function-to-run:fail() ##")
    return "The person has failed and the score is "+str(score)


@my_flask_app.route('/useofrawstring')
def useofrawstring():
    logging.info(f"## You Requested Code to Execute Method:'GET', Received-URL:'/useofrawstring', function-to-run:useofrawstring() ##")
    raw_string_variable = r"The Location of Project is -D:\Mytech\IDE_workspace\ksachin5136git\Flaskpractice\flaskineuron\app.py"
    logging.info(raw_string_variable)
    return raw_string_variable

@my_flask_app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'GET':
        logging.info(
            f"## You Requested Code to Execute Method:'GET', Received-URL:'/calculate', function-to-run:calculate() ##")
        return render_template('calculate.html')
    else:
        logging.info(
            f"## You Requested Code to Execute Method:'POST', Received-input-from-user, function-to-run:calculate() ##")
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths+science+history)/3
        result = ""
        if average_marks >= 50:
            result = "success"
        else:
            result = "fail"

        # return redirect(url_for(result,score=average_marks))

        return render_template('result.html', results=average_marks)


# Assignemnt Try for loop

if __name__ == '__main__':
    logging.info(
        f"APP_START_TIME={datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}")
    my_flask_app.run(debug=False)
