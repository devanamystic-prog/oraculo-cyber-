import streamlit as st
import google.generativeai as genai

# ==================== CONFIGURAÇÃO ====================
st.set_page_config(
    page_title="Oráculo do Véu",
    page_icon="🔮",
    layout="centered"
)

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-3.5-flash")
except Exception:
    st.error("🌙 O Véu não conseguiu despertar... Tente novamente mais tarde.")
    st.stop()

# ==================== INTERFACE ====================
st.image("logo.PNG", width=280)

st.title("🔮 O Oráculo do Véu")
st.markdown("""
✨ Bem-vindo(a) ao Véu ✨

Escolha um cristal, revele sua dúvida e permita que o Oráculo interprete os sinais do seu caminho.
""")

estilo = st.selectbox(
    "🌙 Como o Oráculo deve responder?",
    ["Sábio e acolhedor", "Enigmático e poético", "Direto e prático"]
)

cristal = st.selectbox(
    "💎 Escolha um cristal:",
    [
        "💜 Ametista",
        "🌸 Quartzo Rosa",
        "🖤 Obsidiana",
        "✨ Citrino",
        "🌌 Labradorita",
        "🌕 Pedra da Lua",
        "💚 Jade"
    ]
)

categoria = st.selectbox(
    "🌙 Que área deseja consultar?",
    ["💜 Amor", "🌙 Espiritualidade", "💰 Caminhos Financeiros", "🕯️ Intuição", "🌌 Destino", "🔮 Conselho do Dia"]
)

perguntas = {
    "💜 Amor": ["💜 Como está o seu coração agora?", "💜 O que você busca em uma conexão?", "💜 Há algo que te impede de amar?"],
    "🌙 Espiritualidade": ["🌙 Como está sua conexão interior?", "🌙 O que você busca espiritualmente?", "🌙 Há algo bloqueando seu crescimento espiritual?"],
    "💰 Caminhos Financeiros": ["💰 Como está sua relação com o dinheiro?", "💰 O que você deseja conquistar financeiramente?", "💰 Há algo que te impede de prosperar?"],
    "🕯️ Intuição": ["🕯️ Você tem ouvido sua intuição?", "🕯️ Há um sinal que você está ignorando?", "🕯️ O que seu interior está tentando te dizer?"],
    "🌌 Destino": ["🌌 Você sente que está no caminho certo?", "🌌 O que você deseja para o seu futuro?", "🌌 Há algo que precisa mudar na sua jornada?"],
    "🔮 Conselho do Dia": ["🔮 Como você está se sentindo hoje?", "🔮 Qual é o seu maior desafio agora?", "🔮 O que você precisa ouvir hoje?"]
}

nome = st.text_input("✨ Como devo te chamar?")

st.markdown("---")
st.markdown("🌙 **Responda às perguntas do Véu:**")

p = perguntas[categoria]
r1 = st.text_area(p[0], height=100, max_chars=450)
r2 = st.text_area(p[1], height=100, max_chars=450)
r3 = st.text_area(p[2], height=100, max_chars=450)

if st.button("🔮 Consultar o Oráculo", type="primary"):
    if nome and r1 and r2 and r3:
        with st.spinner("🌙 O Véu está se abrindo..."):
            try:
                prompt = (
                    f"Você é o Oráculo do Véu.\n"
                    f"Seu tom deve ser: {estilo}\n"
                    f"O cristal escolhido foi: {cristal}\n"
                    f"A área escolhida foi: {categoria}\n\n"
                    f"Nome da pessoa: {nome}\n"
                    f"Pergunta 1: {p[0]} — {r1}\n"
                    f"Pergunta 2: {p[1]} — {r2}\n"
                    f"Pergunta 3: {p[2]} — {r3}\n\n"
                    "Responda de forma poética, acolhedora e mística."
                )

                resposta = model.generate_content(prompt)
                st.success("✨ O Oráculo respondeu:")
                st.markdown(resposta.text)

                # AVISO SÓ EM CASOS EXTREMOS
                if any(frase in (r1 + r2 + r3).lower() for frase in ["quero morrer", "quero me matar", "não quero mais viver", "vou me matar"]):
                    st.markdown("---")
                    st.markdown("💙 Quando a alma pede ajuda, é um sinal sagrado. Você não está só. Permitir que alguém humano te acompanhe nessa travessia pode trazer alívio e força.")

            except Exception as e:
                if "quota" in str(e).lower() or "limit" in str(e).lower() or "429" in str(e):
                    st.error("🎟️ Ops! Hoje o limite de consultas foi atingido.\nTente novamente amanhã!")
                else:
                    st.warning("🌙 O Véu entrou em repouso... Tente novamente mais tarde ✨")
    else:
        st.warning("🌙 O Véu precisa do seu nome e das respostas para revelar os sinais ✨")

if st.button("🔄 Limpar tudo"):
    st.rerun()

# ==================== RODAPÉ FINAL ====================
st.markdown("---")
st.markdown("""
🌙 **O Oráculo do Véu não revela destinos absolutos.**  
Ele reflete emoções, ciclos e movimentos internos por meio de interpretações simbólicas e atmosferas intuitivas.
""")
