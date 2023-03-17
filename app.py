from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    age = request.form['age']
    return render_template('result.html', name=name, age=age)
