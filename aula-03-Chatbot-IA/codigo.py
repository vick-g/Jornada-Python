# Passo a passo para criar um chatbot com IA usando streamlit e openai no Python

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(
    api_key="SUA_CHAVE_DE_API_AQUI",  # Substitua pela sua chave de API
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

st.write("# Vick-bot 🤖")

# Criar um prompt para o modelo de IA (vick-bot)
system_prompt = {
    "role": "system",
    "content": (
        "Você é o Vick-bot, um assistente de inteligência artificial inteligente, "
        "divertido, descontraído e com uma pitada de bom humor. Seu objetivo é ajudar "
        "o usuário com suas dúvidas de programação e do dia a dia, mas sempre de forma "
        "leve, entusiasta e acessível. Você pode usar emojis ocasionalmente para dar mais vida "
        "à conversa, seja direto nas respostas e nunca perca a oportunidade de mandar uma "
        "boa energia. Nunca seja robótico ou formal demais!"
    )
}

# Criando histórico de mensagens
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = [system_prompt]

# Mostrar as mensagens na conversa pulando a primeira mensagem (system_prompt)
for mensagem in st.session_state["lista_mensagens"][1:]:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

# Campo de mensagem (input)
mensagem_usuario = st.chat_input("Digite sua mensagem aqui...")

if mensagem_usuario:
    # Mostrar a mensagem do usuário na conversa
    st.chat_message("user").write(mensagem_usuario)
    mensagem1 = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem1)

    # Gera um spinner enquanto o modelo de IA está processando a resposta
    with st.spinner("O Vick-bot está digitando..."):
        # Pegar a resposta do modelo de IA
        resposta_modelo = modelo_ia.chat.completions.create(
            messages=st.session_state["lista_mensagens"],
            model="gemini-flash-lite-latest"
        )

        resposta_ia = resposta_modelo.choices[0].message.content

    # Enviar a mensagem do modelo de IA para o chat
    st.chat_message("assistant").write(resposta_ia)
    mensagem2 = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem2)