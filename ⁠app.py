import streamlit as st
import random

st.set_page_config(page_title="Oráculo do Véu", page_icon="🔮", layout="centered")

st.title("🔮 O Oráculo do Véu")

st.image("sua_foto_do_avatar.png", caption="Sua Oráculo Cyberpunk pronta para a leitura")

st.markdown("---")

nome = st.text_input("Me diga, como se chama e o que te trouxe aqui?")

if nome:
    st.markdown(f"### Seja bem-vinda, **{nome}**.")
    
    categoria = st.selectbox(
        "Qual caminho você deseja consultar no véu?", 
        ["Selecione uma opção...", "Amor e Relacionamentos", "Trabalho e Finanças", "Destino e Espiritualidade", "Energia do Dia"]
    )
    
    if categoria != "Selecione uma opção...":
        st.write("---")
        st.subheader("✨ Escolha um cristal e sintonize sua energia...")
        
        col1, col2, col3 = st.columns(3)
        
        escolha_cristal = None
        with col1:
            if st.button("🔮 Cristal Roxo", use_container_width=True):
                escolha_cristal = "Roxo"
        with col2:
            if st.button("🔷 Cristal Azul", use_container_width=True):
                escolha_cristal = "Azul"
        with col3:
            if st.button("🔶 Cristal Âmbar", use_container_width=True):
                escolha_cristal = "Âmbar"

        if escolha_cristal:
            st.markdown("---")
            st.write(f"🔹 *Você sintonizou com as vibrações do **Cristal {escolha_cristal}**.*")
            
            st.info("💬 *\"Agora, vamos ver o que o véu irá revelar...\"*")
            
            misterios_veu = [
                ("O Despertar de Ísis", "✨ Asas da Magia", "A névoa se dissipa para trazer cura e renascimento. É hora de usar sua sabedoria interior para reconstruir o que foi quebrado e retomar o seu poder."),
                ("A Encruzilhada de Hécate", "🔑 As Chaves do Destino", "O véu mostra caminhos abertos. Uma escolha importante está diante de você. Confie na sua intuição profunda para guiar seus passos na escuridão."),
                ("O Clã de Morrígan", "🦅 As Asas da Vitória", "Sua força de guerreira foi convocada pelo véu. Mudanças drásticas e necessárias estão acontecendo. Proteja sua energia e encare os desafios de frente."),
                ("A Estrela do Destino", "🌌 Luz na Penumbra", "Um sinal de esperança e direcionamento espiritual. O véu revela que você está protegida e que as respostas que busca chegarão com o tempo."),
                ("O Silêncio da Noite", "🌙 Intuição Ativa", "Nem tudo deve ser revelado agora. O véu pede recolhimento, silêncio e observação. Olhe para dentro antes de dar o próximo grande passo.")
            ]
            
            revelacao = random.choice(misterios_veu)
            
            st.success(f"### 👁️ O Véu se abre: {revelacao[0]}")
            st.write(f"**Preságio:** *{revelacao[1]}*")
            st.write(f"🔮 {revelacao[2]}")
            
            st.markdown("---")
            
            st.subheader("🔮 Você quer decifrar o segredo completo?")
            resposta_final = st.radio("Selecione sua resposta para continuar:", ["Sim, mística oráculo. Revele tudo!", "Não, prefiro meditar sobre o preságio por hoje."])
            
            if resposta_final == "Sim, mística oráculo. Revele tudo!":
                st.write("🌌 *Os mistérios mais profundos do véu pertencem às deusas... Continue acompanhando o canal para a leitura completa e diária!*")
