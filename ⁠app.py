import streamlit as st
import google.generativeai as genai

# Configuração da API
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Chave API não encontrada! Configure em Settings > Secrets.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

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
                st.error(f"Erro ao consultar: {e}")
    else:
        st.warning("Preencha seu nome e a pergunta.")
