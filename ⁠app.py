import streamlit as st
import google.generativeai as genai
from PIL import Image

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception:
    st.error("🌙 O Véu não conseguiu despertar...")
    st.stop()

st.set_page_config(
    page_title="Oráculo do Véu",
    page_icon="🔮",
    layout="centered"
)

st.title("🔮 O Oráculo do Véu")
st.markdown("""
✨ Bem-vindo(a) ao Véu ✨

Escolha um cristal, revele sua dúvida e permita que o Oráculo interprete os sinais do seu caminho.
""")

estilo = st.selectbox(
    "🌙 Como o Oráculo deve responder?",
    ["Sábio", "Enigmático", "Direto e Prático"]
)

cristal = st.selectbox(
    "💎 Escolha um cristal:",
    ["💜 Ametista", "🌸 Quartzo Rosa", "🖤 Obsidiana", "✨ Citrino", "🌌 Labradorita"]
)

categoria = st.selectbox(
    "🌙 Que área deseja consultar?",
    ["💜 Amor", "🌙 Espiritualidade", "💰 Caminhos Financeiros", "🕯️ Intuição", "🌌 Destino", "🔮 Conselho do Dia"]
)

nome = st.text_input("✨ Como devo te chamar?")
pergunta = st.text_area("🌙 O que deseja revelar ao Véu?")

imagem = st.file_uploader(
    "🖼️ Envie uma imagem para o Oráculo interpretar (opcional)",
    type=["png", "jpg", "jpeg"]
)

if st.button("🔮 Consultar o Oráculo"):
    if nome and pergunta:
        with st.spinner("🌙 O Véu está se abrindo..."):
            try:
                prompt = (
                    "Você é um Oráculo espiritual, simbólico e intuitivo.\n\n"
                    f"Seu tom deve ser: {estilo}\n"
                    f"O cristal escolhido foi: {cristal}\n"
                    f"A área escolhida foi: {categoria}\n\n"
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

                if imagem:
                    img = Image.open(imagem)
                    st.image(img, caption="Imagem enviada ao Oráculo", use_column_width=True)
                    resposta = model.generate_content([prompt, img])
                else:
                    resposta = model.generate_content(prompt)

                st.success("✨ O Oráculo respondeu:")
                st.write(resposta.text)

            except Exception:
                st.warning(
                    "🌙 O Véu entrou em repouso...\n\n"
                    "As energias estão se reorganizando.\n"
                    "Tente novamente mais tarde ✨"
                )
    else:
        st.warning("🌙 O Véu precisa do seu nome e da sua pergunta para revelar os sinais ✨")






