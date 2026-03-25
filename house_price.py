from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset 
df = pd.read_excel("logistic_regression/dataset_precios_inmuebles.xlsx")

# Input data
X = df[[
    "area_m2",
    "habitaciones",
    "baños",
    "pisos",
    "garaje",
    "antiguedad",
    "distancia_centro_km"
]]

# Output data 
y = df["precio"]

#  model
model = LinearRegression()

# Train model
model.fit(X, y)

# Prediction
def predict_price(area, rooms, bathrooms, floors, garage, age, distance):

    data = [[
        area,
        rooms,
        bathrooms,
        floors,
        garage,
        age,
        distance
    ]]

    prediction = model.predict(data)[0]

    # Colombian pesos 
    formatted_price = "${:,.0f} COP".format(prediction)

    return "Estimated price: " + formatted_price


@app.route("/", methods=["GET","POST"])
def home():

    result = None

    if request.method == "POST":

        area = float(request.form["area"])
        rooms = float(request.form["rooms"])
        bathrooms = float(request.form["bathrooms"])
        floors = float(request.form["floors"])
        garage = float(request.form["garage"])
        age = float(request.form["age"])
        distance = float(request.form["distance"])

        result = predict_price(
            area,
            rooms,
            bathrooms,
            floors,
            garage,
            age,
            distance
        )

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
