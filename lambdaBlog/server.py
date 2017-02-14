from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/enternew')
def enter_new():
    return render_template('food.html')


@app.route('/favorite')
def favorite():
    return render_template('food.html')


@app.route('/addfood', methods=['POST'])
def add_food():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        title = request.form['title']
        post = request.form['post']
        cursor.execute('INSERT INTO posts (name,calories,cuisine,is_vegetarian,is_gluten_free) VALUES (?,?,?,?,?)', (name,calories,cuisine,is_vegetarian,is_gluten_free))
        connection.commit()
        message = 'Record successfully added'
    finally:
        return render_template('food.html', message=message)
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
