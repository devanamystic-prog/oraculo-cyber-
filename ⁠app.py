import streamlit as st
import google.generativeai as genai

# Configuração da chave de segurança
# Lembre-se: a GOOGLE_API_KEY deve estar salva nos "Secrets" do Streamlit
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

# Configuração da página
st.set_page_config(page_title="Oráculo do Véu", page_icon="🔮")
st.title("🔮 O Oráculo do Véu")
st.markdown("---")

# Interface do usuário com a linguagem inclusiva
nome = st.text_input("Bem-vindo(a), buscador(a). Como devo te chamar?")
pergunta = st.text_area("Qual a sua dúvida para o Oráculo?")

# Lógica do Oráculo
if st.button("Consultar o Oráculo"):
    if nome and pergunta:
        with st.spinner('O véu se abre...'):
            try:
                # O comando para a IA
                prompt = f"Aja como um Oráculo místico. Responda para {nome} sobre: {pergunta}"
                resposta = model.generate_content(prompt)
                
                # Exibição da resposta
                st.info(f"**O Oráculo responde:**\n\n{resposta.text}")
            except Exception as e:
                st.error("O Oráculo está em silêncio agora. Verifique sua chave de acesso (API Key) nas configurações do app.")
    else:
        st.warning("Preencha seu nome e a pergunta para ouvir o Oráculo.")

st.markdown("---")
st.caption("Oráculo de Devana Mystic | Conectado")
