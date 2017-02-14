from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/birthday")
def birthday():
    return 'October 31 1989'


@app.route("/greeting/<name>")
def greeting(name):
    return 'Hello ' + name


@app.route("/sum/<one>/<two>")
def sum(one, two):
    return one + ' + ' + two + ' = ' + str(int(one) + int(two))


@app.route("/multiply/<one>/<two>")
def multiply(one, two):
    return one + ' * ' + two + ' = ' + str(int(one) * int(two))


@app.route("/subtract/<one>/<two>")
def subtract(one, two):
    return one + ' - ' + two + ' = ' + str(int(one) - int(two))


@app.route("/favoritefoods")
def favoritefoods():
    return jsonify(['French Fries', 'Soup', 'Oatmeal'])
