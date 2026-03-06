from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return "hello flask"

@app.route('/firstpage')
def firstpage():
    return render_template('index.html')