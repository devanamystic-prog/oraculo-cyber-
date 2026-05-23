import streamlit as st
import google.generativeai as genai

# =========================
# CONFIGURAÇÃO DA API
# =========================

try:
    api_key = st.secrets["GOOGLE_API_KEY"]

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

except Exception as e:

    st.error("⚠️ Erro ao carregar a chave API:")
    st.code(str(e))

    st.stop()

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(
    page_title="🔮 Oráculo do Véu",
    page_icon="🔮"
)

# =========================
# TÍTULO
# =========================

st.title("🔮 O Oráculo do Véu")

st.markdown(
    "Escolha um cristal e consulte o Oráculo ✨"
)

# =========================
# ESTILO
# =========================

estilo = st.selectbox(
    "Como o Oráculo deve te responder?",
    [
        "Sábio",
        "Enigmático",
        "Direto e Prático"
    ]
)

# =========================
# CRISTAIS
# =========================

cristal = st.selectbox(
    "Escolha um cristal para guiar sua consulta:",
    [
        "💜 Ametista",
        "🌸 Quartzo Rosa",
        "🖤 Obsidiana",
        "✨ Citrino",
        "🌌 Labradorita"
    ]
)

# =========================
# INPUTS
# =========================

nome = st.text_input(
    "Como devo te chamar?"
)

pergunta = st.text_area(
    "Qual a sua dúvida para o Oráculo?"
)

# =========================
# BOTÃO
# =========================

if st.button("Consultar o Oráculo"):

    if nome and pergunta:

        with st.spinner("🔮 O Oráculo está consultando as estrelas..."):

            try:

                prompt = f"""
                Você é um oráculo {estilo}.

                O cristal escolhido foi:
                {cristal}

                Responda de forma profunda,
                mística e intuitiva.

                Nome:
                {nome}

                Pergunta:
                {pergunta}
                """

                resposta = model.generate_content(prompt)

                st.success("✨ O Oráculo respondeu:")

                st.write(resposta.text)

            except Exception as e:

                st.error("⚠️ Erro detectado:")

                st.code(str(e))

    else:

        st.warning(
            "Por favor, preencha seu nome e sua pergunta."
        )
