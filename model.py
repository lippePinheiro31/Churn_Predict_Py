import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import sqlite3

def train_model():
    conn = sqlite3.connect("database.db")
    df = pd.read_sql("SELECT * FROM customers", conn)
    conn.close()

    X = df.drop(columns=["id", "churn"])
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    with open("churn_predictor.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_model()
