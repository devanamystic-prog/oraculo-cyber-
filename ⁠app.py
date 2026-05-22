import streamlit as st
import subprocess
import sys

# Força a instalação da biblioteca se ela não existir
try:
    import google.generativeai as genai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai

# Agora o código normal
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Oráculo do Véu", page_icon="🔮")
st.title("🔮 O Oráculo do Véu")

nome = st.text_input("Bem-vindo(a), buscador(a). Como devo te chamar?")
pergunta = st.text_area("Qual a sua dúvida para o Oráculo?")

if st.button("Consultar o Oráculo"):
    if nome and pergunta:
        with st.spinner('O véu se abre...'):
            resposta = model.generate_content(f"Aja como um Oráculo místico. Responda para {nome} sobre: {pergunta}")
            st.info(f"**O Oráculo responde:**\n\n{resposta.text}")
    else:
        st.warning("Preencha seu nome e a pergunta.")
