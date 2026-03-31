
from flask import Flask, render_template, request
import house_price
import logistic_regression

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/case1')
def case1():
    return render_template('case1.html')

@app.route('/case2')
def case2():
    return render_template('case2.html')

@app.route('/case3')
def case3():
    return render_template('case3.html')

@app.route('/case4')
def case4():
    return render_template('case4.html')


@app.route('/concepts')
def concepts():
    return render_template('concepts.html')
    
@app.route('/con_logistic')
def con_logistic():
    return render_template('con_logistic.html')

    
@app.route('/concepts_Sup')
def concepts_Sup():
    return render_template('concepts_Sup.html')


@app.route('/application_linear', methods=["GET","POST"])
def application_linear():

    result = None

    if request.method == "POST":

        area = float(request.form["area"])
        rooms = float(request.form["habitaciones"])
        bathrooms = float(request.form["banos"])
        floors = float(request.form["pisos"])
        garage = float(request.form["garaje"])
        age = float(request.form["antiguedad"])
        distance = float(request.form["distancia"])

        result = house_price.predict_price(
            area,
            rooms,
            bathrooms,
            floors,
            garage,
            age,
            distance
        )

    return render_template(
        'linear_regre_app.html',
        result=result
    )

@app.route('/logistic_app', methods=["GET", "POST"])

def logistic_app():

    prediction = None

    if request.method == "POST":

        hours = float(request.form["hours"])

        attendance = float(request.form["attendance"])

        assignments = float(request.form["assignments"])

        grade = float(request.form["grade"])

        sleep = float(request.form["sleep"])


        prediction = logistic_regression.predecir_resultado(

        hours,
        attendance,
        assignments,
        grade,
        sleep

        )


    return render_template(

    "logistic.html",

    prediction=prediction,

    accuracy="0.95",
    precision="0.94",
    recall="0.93",
    f1="0.94",
    roc_auc="0.96"

    )


if __name__ == "__main__":
    app.run(debug=True)

