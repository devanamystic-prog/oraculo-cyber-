import streamlit as st
import google.generativeai as genai

# Configuração da chave (Certifique-se de adicioná-la nos Secrets do app)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# Configuração da página
st.set_page_config(page_title="Oráculo do Véu", page_icon="🔮")
st.title("🔮 O Oráculo do Véu")

# Interface do usuário
nome = st.text_input("Bem-vindo(a), buscador(a). Como devo te chamar?")
pergunta = st.text_area("Qual a sua dúvida para o Oráculo?")

# Lógica
if st.button("Consultar o Oráculo"):
    if nome and pergunta:
        with st.spinner('O véu se abre...'):
            try:
                resposta = model.generate_content(f"Aja como um Oráculo místico. Responda para {nome} sobre: {pergunta}")
                st.info(f"**O Oráculo responde:**\n\n{resposta.text}")
            except Exception as e:
                st.error("O Oráculo está em silêncio. Verifique sua chave API.")
    else:
        st.warning("Preencha seu nome e a pergunta.")
