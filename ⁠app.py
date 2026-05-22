import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

st.title("🔮 O Oráculo do Véu")
nome = st.text_input("Bem-vindo(a), buscador(a). Como devo te chamar?")
pergunta = st.text_area("Qual a sua dúvida para o Oráculo?")

if st.button("Consultar o Oráculo"):
    if nome and pergunta:
        resposta = model.generate_content(f"Responda como um Oráculo: {pergunta}")
        st.info(resposta.text)
