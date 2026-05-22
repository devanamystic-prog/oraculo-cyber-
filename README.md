import streamlit as st

st.title("🌌 Oráculo Cyber da Devana")
st.write("Bem-vindo ao meu Oráculo!")

pergunta = st.text_input("Faça sua pergunta ao Oráculo:")

if st.button("Consultar"):
    if pergunta:
        st.write("O Oráculo diz: Confie na sua intuição e siga o caminho que sua alma escolheu.")
    else:
        st.warning("Por favor, digite uma pergunta.")
