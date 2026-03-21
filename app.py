<<<<<<< Updated upstream
from flask import Flask, render_template
=======
from flask import Flask, render_template, request
import LinealRegresion
import pandas as pd
from sklearn.linear_model import LogisticRegression
>>>>>>> Stashed changes

app = Flask(__name__)
print("INICIANDO APP...")


# =========================
# MODELO LOGÍSTICO
# =========================

print("MODELO ENTRENADO")

df_log = pd.read_csv("logistic_regression/dataset_regresion_logistica.csv")

X_log = df_log[["edad", "ingreso_mensual", "visitas_web_mes", 
                "tiempo_sitio_min", "compras_previas", "descuento_usado"]]

y_log = df_log["target"]

model_log = LogisticRegression(max_iter=1000)
model_log.fit(X_log, y_log)

def predecir_compra(edad, ingreso, visitas, tiempo, compras, descuento):
    datos = [[edad, ingreso, visitas, tiempo, compras, descuento]]
    pred = model_log.predict(datos)[0]

    if pred == 1:
        return "El cliente probablemente COMPRA"
    else:
        return "El cliente probablemente NO COMPRA"


# =========================
# RUTAS
# =========================

@app.route('/')
def home():
    return "HELLO FLASK"

@app.route('/firstpage')
def firstpage():
<<<<<<< Updated upstream
    return render_template('index.html')
=======
    return render_template('index.html')




@app.route('/linealRegression', methods=["GET","POST"])
def caculateGrade():
    calculateResult = None
    if request.method == "POST":
        hours = float(request.form["hours"])
        calculateResult = LinealRegresion.calculateGrade(hours)
    return render_template("linearRegressionGRades.html", result=calculateResult)


@app.route('/logisticRegression', methods=["GET","POST"])
def logistic():
    result = None

    if request.method == "POST":
        edad = float(request.form["edad"])
        ingreso = float(request.form["ingreso"])
        visitas = float(request.form["visitas"])
        tiempo = float(request.form["tiempo"])
        compras = float(request.form["compras"])
        descuento = float(request.form["descuento"])

        result = predecir_compra(edad, ingreso, visitas, tiempo, compras, descuento)

    return render_template("logistic.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> Stashed changes
