import streamlit as st
import google.generativeai as genai

# Configuração da chave de API
# Configuração da chave de API
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro ao ler a chave API: {e}")
    st.stop()

st.title("🔮 O Oráculo do Véu")

# Criando opções para o usuário
estilo = st.selectbox("Como o Oráculo deve te responder?", ["Sábio", "Enigmático", "Direto e Prático"])

nome = st.text_input("Como devo te chamar?")
pergunta = st.text_area("Qual a sua dúvida para o Oráculo?")

if st.button("Consultar o Oráculo"):
    if nome and pergunta:
        with st.spinner('O Oráculo está consultando as estrelas...'):
            try:
                # Prompt místico
                prompt = f"Você é um oráculo {estilo}. Responda para {nome} sobre: {pergunta}"
                resposta = model.generate_content(prompt)
                st.info(f"**Resposta do Oráculo:**\n\n{resposta.text}")
            except Exception as e:
                st.error("O Oráculo está em silêncio no momento. Verifique sua chave de API.")
    else:
        st.warning("Por favor, preencha seu nome e a pergunta.")
