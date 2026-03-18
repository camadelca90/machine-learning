from flask import Flask, render_template, request
import LinealRegresion

app=Flask(__name__)

@app.route('/')
def home():
    return "hello flask"

@app.route('/firstpage')
def firstpage():
    return render_template('index.html')

@app.route('/linealRegression',methods=["GET","POST"])
def caculateGrade():
    calculateResult = None
    if request.method == "POST":
        hours = float (request.form["hours"])
        calculateResult = LinealRegresion.calculateGrade(hours)
    return render_template ("linearRegressionGRades.html", result = calculateResult)
