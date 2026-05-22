import streamlit as st
import google.generativeai as genai

# Configuração da API
# Certifique-se de que a chave está nos "Secrets" do app
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

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
