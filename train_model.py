import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_and_save_model(db_path='database.db', model_path='churn_predictor.pkl'):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM customers", conn)
    conn.close()

    print(df.head())

    # Remover colunas não numéricas e irrelevantes para o modelo
    X = df.drop(columns=['name', 'signup_date', 'last_active_date', 'is_churn'])

    # Codificar variável categórica 'gender'
    X = pd.get_dummies(X, columns=['gender'], drop_first=True)

    y = df['is_churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    print(f"Modelo treinado e salvo em {model_path}")

if __name__ == "__main__":
    train_and_save_model()

