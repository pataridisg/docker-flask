from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, RadioField, SelectField,
                    TextField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'mysecretkey'

# Pat says: These three lines is for reload the html template files every time.
# Otherwise Jinja load them from cache. The result? Not displaying current sensor value!!!
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.cache = {}
app.jinja_env.auto_reload = True


@app.route('/')
def index():
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
	
@app.route('/display')
def display():
	return render_template('display.html')

@app.route('/<sensor>=<value>')
def display_sensor(sensor, value):
	html_creation = '{% extends "base.html" %} {% block content %} <div class="container"> <div class="jumbotron"> <h1>This is the ' + sensor + ' page</h1> <h2>The value is ' + value + '</h2> </div> </div> {% endblock %}'
	file_path = "./templates/"
	f = open(file_path + "display.html", "w")
	f.write(html_creation) 
	f.close()
	return "<h1>{} for {} written in Display.html </h1>".format(value, sensor)

	
if __name__ == '__main__':
	app.run(debug=False, host="0.0.0.0")
