import streamlit as st

# Configuração da página
st.set_page_config(page_title="Oráculo do Véu", page_icon="🔮", layout="centered")

# Título e Introdução
st.title("🔮 O Oráculo do Véu")
st.markdown("---")

nome = st.text_input("Bem-vinda, buscadora. Como devo te chamar?")

if nome:
    st.success(f"É uma honra te receber, {nome}.")
    
    categoria = st.selectbox(
        "Qual dimensão você deseja consultar hoje?",
        ["Selecione uma opção...", "Caminhos do Amor", "Jornada Profissional", "Revelações Espirituais"]
    )

    if categoria != "Selecione uma opção...":
        st.write("---")
        st.subheader(f"✨ Conexão: {categoria}")
        st.write("Sinta a energia da sua pergunta e escolha um caminho:")
        
        # Criando colunas para os cristais
        col1, col2, col3 = st.columns(3)
        
        # Usando botões simples que não quebram o fluxo
        if col1.button("🔮 Ametista"):
            st.info("Ametista: O equilíbrio está no silêncio. A resposta que busca reside na sua intuição mais profunda.")
            
        if col2.button("💎 Safira"):
            st.info("Safira: A verdade se revela através da clareza mental. Observe os sinais ao seu redor nos próximos dias.")
            
        if col3.button("🔶 Âmbar"):
            st.info("Âmbar: A energia do passado se integra ao seu presente. Deixe ir o que não serve mais para abrir espaço ao novo.")

# Rodapé
st.markdown("---")
st.caption("Oráculo desenvolvido por Devana Mystic | Conecte-se com o invisível.")
