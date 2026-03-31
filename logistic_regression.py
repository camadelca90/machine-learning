import pandas as pd
from sklearn.linear_model import LogisticRegression

# cargar dataset
df = pd.read_excel("logistic_regression/logistic_regression_data.xlsx")

# variables de entrada
X = df[[
"Hours_Studied",
"Attendance_%",
"Assignments_Completed",
"Previous_Grade",
"Sleep_Hours"
]]

# variable objetivo
y = df["Result"]

# convertir texto a numero
y = y.map({
"Pass":1,
"Fail":0
})

# crear modelo
model = LogisticRegression(max_iter=1000)

# entrenar modelo
model.fit(X, y)


# funcion de prediccion

def predecir_resultado(hours, attendance, assignments, grade, sleep):

    datos = [[
    hours,
    attendance,
    assignments,
    grade,
    sleep
    ]]

    pred = model.predict(datos)[0]

    if pred == 1:
        return "The student will PASS the subject"
    else:
        return "The student will FAIL the subject"