import streamlit as st
import google.generativeai as genai

# Configuração da chave
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Modelo Gemini
model = genai.GenerativeModel("gemini-pro")

# Interface
st.set_page_config(
    page_title="🔮 Oráculo do Véu",
    page_icon="🔮"
)

st.title("🔮 O Oráculo do Véu")

nome = st.text_input(
    "Bem-vindo(a), buscador(a). Como devo te chamar?"
)

pergunta = st.text_area(
    "Qual a sua dúvida para o Oráculo?"
)

if st.button("Consultar o Oráculo"):

    if nome and pergunta:

        with st.spinner("O véu se abre..."):

            prompt = f"""
            Aja como um Oráculo místico e espiritual.
            Responda de forma profunda, simbólica e intuitiva.

            Nome: {nome}

            Pergunta:
            {pergunta}
            """

            resposta = model.generate_content(prompt)

            st.success("✨ O Oráculo respondeu:")

            st.write(resposta.text)

    else:
        st.warning("Preencha seu nome e sua pergunta.")
