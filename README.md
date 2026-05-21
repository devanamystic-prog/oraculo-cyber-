# oraculo-cyber-
Meu oráculo de cristais e runas⁠.
import streamlit as st

st.title("🔮 Oráculo do Véu")
st.write("Bem-vinda, buscadora. O que deseja saber?")

# Caixa para o usuário digitar
pergunta = st.text_input("Faça sua pergunta ao Oráculo:")

# Botão para consultar
if st.button("Consultar"):
    if pergunta:
        st.write("---")
        st.subheader("A resposta do Véu:")
        # Aqui você pode colocar a lógica da sua IA ou uma resposta simples
        st.write("O véu se abre... (Aqui entrará a resposta da sua inteligência artificial)")
    else:
        st.warning("Por favor, digite algo antes de consultar.")
        st.text_input
