import streamlit as st
import subprocess
import sys
import os

# Força a instalação da biblioteca se ela não estiver instalada
if not os.path.exists("installed.txt"):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    with open("installed.txt", "w") as f:
        f.write("done")

import google.generativeai as genai

# Configuração da API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

st.title("🔮 O Oráculo do Véu")

nome = st.text_input("Bem-vindo(a), buscador(a). Como devo te chamar?")
pergunta = st.text_area("Qual a sua dúvida para o Oráculo?")

if st.button("Consultar o Oráculo"):
    if nome and pergunta:
        with st.spinner('O véu se abre...'):
            try:
                resposta = model.generate_content(f"Aja como um Oráculo místico. Responda para {nome} sobre: {pergunta}")
                st.info(f"**O Oráculo responde:**\n\n{resposta.text}")
            except Exception as e:
                st.error("Erro na consulta.")
    else:
        st.warning("Preencha seu nome e a pergunta.")
