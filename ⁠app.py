import streamlit as st
import google.generativeai as genai

# ====================================
# CONFIGURAÇÃO DA API
# ====================================

try:
    api_key = st.secrets["GOOGLE_API_KEY"]

    genai.configure(api_key=api_key)

    # MODELO CORRETO
    model = genai.GenerativeModel(
    "models/gemini-1.5-flash"

    )

except Exception as e:

    st.error("⚠️ Erro ao carregar a API")
    st.code(str(e))

    st.stop()

# ====================================
# CONFIGURAÇÃO DA PÁGINA
# ====================================

st.set_page_config(
    page_title="🔮 Oráculo do Véu",
    page_icon="🔮",
    layout="centered"
)

# ====================================
# TÍTULO
# ====================================

st.title("🔮 O Oráculo do Véu")

st.markdown(
    """
    Bem-vindo(a) ao Véu ✨

    Escolha um cristal
    e consulte o Oráculo.
    """
)

# ====================================
# ESTILO
# ====================================

estilo = st.selectbox(
    "Como o Oráculo deve responder?",
    [
        "Sábio",
        "Enigmático",
        "Direto e Prático"
    ]
)

# ====================================
# CRISTAIS
# ====================================

cristal = st.selectbox(
    "Escolha um cristal:",
    [
        "💜 Ametista",
        "🌸 Quartzo Rosa",
        "🖤 Obsidiana",
        "✨ Citrino",
        "🌌 Labradorita"
    ]
)

# ====================================
# INPUTS
# ====================================

nome = st.text_input(
    "Como devo te chamar?"
)

pergunta = st.text_area(
    "Qual a sua dúvida para o Oráculo?"
)

# ====================================
# BOTÃO
# ====================================

if st.button("Consultar o Oráculo 🔮"):

    if nome and pergunta:

        with st.spinner("🌙 O Véu está se abrindo..."):

            try:

                prompt = f"""
                Você é um Oráculo espiritual,
                simbólico e intuitivo.

                Seu tom deve ser:
                {estilo}

                O cristal escolhido foi:
                {cristal}

                IMPORTANTE:
                - Nunca dê respostas perigosas
                - Nunca dê diagnósticos médicos
                - Nunca incentive violência
                - Responda de forma acolhedora
                - Use linguagem poética e mística
                - Faça a pessoa refletir

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
