import streamlit as st
import pandas as pd
import pickle
from database import create_table, insert_sample_data
import sqlite3

# Inicialização do banco
create_table()
insert_sample_data()

# Carregar modelo
model = pickle.load(open("churn_predictor.pkl", "rb"))

st.title("🔮 Previsor de Churn de Clientes")

st.markdown("Preencha os dados abaixo para prever se o cliente vai sair:")

gender = st.selectbox("Gênero", ["Male", "Female"])
age = st.slider("Idade", 18, 100)
tenure = st.slider("Tempo como cliente (anos)", 0, 10)
balance = st.number_input("Saldo em conta", value=0.0)
products = st.slider("Número de Produtos", 1, 4)
credit_score = st.slider("Score de Crédito", 300, 850)
active_member = st.selectbox("É cliente ativo?", [1, 0])
salary = st.number_input("Salário estimado", value=0.0)

if st.button("Prever Churn"):
    input_data = pd.DataFrame({
        "gender": [gender],
        "age": [age],
        "tenure": [tenure],
        "balance": [balance],
        "products_number": [products],
        "credit_score": [credit_score],
        "is_active_member": [active_member],
        "estimated_salary": [salary]
    })

    prediction = model.predict(input_data)[0]
    st.subheader("Resultado:")
    if prediction == 1:
        st.error("⚠️ Cliente com ALTA chance de sair!")
    else:
        st.success("✅ Cliente com BAIXA chance de sair.")
