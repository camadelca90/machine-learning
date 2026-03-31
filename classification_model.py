import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score
)

# Load dataset and train model once
df = pd.read_csv("linearsvc_customer_purchase_dataset.csv")

X = df.drop("purchase_label", axis=1)
y = df["purchase_label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearSVC()
model.fit(X_train, y_train)


# ===============================
# FUNCTION 1: Get metrics
# ===============================
def get_model_metrics():
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    y_scores = model.decision_function(X_test)
    roc_auc = roc_auc_score(y_test, y_scores)

    conf_matrix = confusion_matrix(y_test, y_pred)

    return {
        "accuracy": round(accuracy, 3),
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "f1": round(f1, 3),
        "roc_auc": round(roc_auc, 3),
        "conf_matrix": conf_matrix.tolist()
    }


# ===============================
# FUNCTION 2: Make prediction
# ===============================
def predict_customer(data):

    input_data = [[
        data["age"],
        data["monthly_income_usd"],
        data["website_visits_30d"],
        data["avg_session_minutes"],
        data["products_viewed"],
        data["cart_additions"],
        data["previous_purchases"],
        data["discount_clicks_30d"],
        data["days_since_last_purchase"],
        data["support_tickets_6m"],
        data["email_open_rate_pct"],
        data["mobile_user"],
        data["premium_member"]
    ]]

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        return "High probability of purchase"
    else:
        return "Low probability of purchase"