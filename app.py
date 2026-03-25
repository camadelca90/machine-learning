
from flask import Flask, render_template, request
import house_price

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

@app.route('/application', methods=["GET","POST"])
def application():
    resultado = None

    if request.method == "POST":
        hours = float(request.form["hours"])
        resultado = LinealRegresion.calculateGrade(hours)

    return render_template('application.html', resultado=resultado)

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


if __name__ == "__main__":
    app.run(debug=True)

