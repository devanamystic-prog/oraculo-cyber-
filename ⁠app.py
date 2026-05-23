import streamlit as st
import google.generativeai as genai

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    st.error("Erro ao carregar a API")
    st.code(str(e))
    st.stop()

st.set_page_config(
    page_title="Oraculo do Veu",
    page_icon="🔮",
    layout="centered"
)

st.title("🔮 O Oráculo do Véu")
st.markdown("Bem-vindo(a) ao Véu ✨\n\nEscolha um cristal e consulte o Oráculo.")

estilo = st.selectbox(
    "Como o Oráculo deve responder?",
    ["Sábio", "Enigmático", "Direto e Prático"]
)

cristal = st.selectbox(
    "Escolha um cristal:",
    ["💜 Ametista", "🌸 Quartzo Rosa", "🖤 Obsidiana", "✨ Citrino", "🌌 Labradorita"]
)

nome = st.text_input("Como devo te chamar?")
pergunta = st.text_area("Qual a sua dúvida para o Oráculo?")

if st.button("Consultar o Oráculo 🔮"):
    if nome and pergunta:
        with st.spinner("🌙 O Véu está se abrindo..."):
            try:
                prompt = (
                    "Você é um Oráculo espiritual, simbólico e intuitivo.\n\n"
                    f"Seu tom deve ser: {estilo}\n"
                    f"O cristal escolhido foi: {cristal}\n\n"
                    "IMPORTANTE:\n"
                    "- Nunca dê respostas perigosas\n"
                    "- Nunca dê diagnósticos médicos\n"
                    "- Nunca incentive violência\n"
                    "- Responda de forma acolhedora\n"
                    "- Use linguagem poética e mística\n"
                    "- Faça a pessoa refletir\n\n"
                    f"Nome: {nome}\n"
                    f"Pergunta: {pergunta}"
                )
                resposta = model.generate_content(prompt)
                st.success("✨ O Oráculo respondeu:")
                st.write(resposta.text)
            except Exception as e:
                st.error("Erro detectado:")
                st.code(str(e))
    else:
        st.warning("Por favor, preencha seu nome e sua pergunta.")



