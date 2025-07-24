import sqlite3
import pandas as pd

def create_connection(db_file='database.db'):
    conn = sqlite3.connect(db_file)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            gender TEXT,
            age INTEGER,
            tenure INTEGER,
            balance REAL,
            products_number INTEGER,
            credit_score INTEGER,
            is_active_member INTEGER,
            estimated_salary REAL,
            churn INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_sample_data():
    df = pd.read_csv("data/sample_data.csv")
    conn = create_connection()
    df.to_sql("customers", conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_sample_data()
