import streamlit as st
import random

# Configuração da página
st.set_page_config(
    page_title="Feliz Dia dos Namorados ❤️",
    page_icon="❤️",
    layout="centered"
)

# Injeção de CSS personalizado para criar uma interface romântica e elegante
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f6;
    }
    .main-container {
        text-align: center;
        padding: 20px;
    }
    .title {
        color: #b8324f;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 2.8rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        color: #7d6368;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 40px;
    }
    .reason-box {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 35px;
        box-shadow: 0 10px 25px rgba(184, 50, 79, 0.1);
        text-align: center;
        margin: 20px auto;
        max-width: 550px;
        border: 1px solid #f0d5da;
        min-height: 120px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .reason-text {
        color: #5c1d24;
        font-family: 'Georgia', serif;
        font-size: 1.5rem;
        font-style: italic;
        line-height: 1.6;
        margin: 0;
    }
    div.stButton > button:first-child {
        background-color: #e84a5f;
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        border-radius: 30px;
        padding: 12px 35px;
        border: none;
        box-shadow: 0 5px 15px rgba(232, 74, 95, 0.3);
        transition: all 0.3s ease;
        display: block;
        margin: 30px auto;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff2e63;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(232, 74, 95, 0.4);
        border: none;
        color: white;
    }
    div.stButton > button:first-child:active {
        transform: translateY(1px);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<p class="title">Por que eu te amo? (De Kesley para Talita)❤️</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Um pequeno espaço para te lembrar do quanto você é especial para mim.</p>', unsafe_allow_html=True)

# Lista de motivos personalizáveis
motivos = [
    "Eu amo o fato de ao simplesmente olhar seu sorriso o dia ficar muito mais bonito",
    "Amo o jeito que voce me apoia até mesmo em algumas loucuras",
    "Amo a forma como nos entendemos apenas com um olhar, mesmo quando estamos em silêncio, ainda que eu seja ruim em entender sinais",
    "Até horas ao seu lado parecem apenas segundos e tudo que eu mais queria era congelar o tempo para ficar mais tempo com você.",
    "Amo nossas conversas sobre doramas e o jeito que você se interressa até pelas séries e animes aleatórias que eu gosto",
    "Cada momento contigo, até o mais simples no sofá ou mexendo com massinha, torna-se especial.",
    "Eu te amo por que sempre que penso em futuro já não consigo imaginar um em que você não esteja ao meu lado.",
    "Faz eu me sentir a pessoa mais amada e sortuda do universo.",
    "Amo a nossa história, tô ansioso para contar pros nossos filhos sobre ela, desde as células até o ataque ao zumbi no Coleguium, até o dia 24",
    "És a minha melhor companhia, o meu porto seguro e o meu melhor par.",
    "Amo a paciência com que ouves as minhas explicações sobre coisas aleátoria.",
    "Transformas qualquer rotina numa aventura inesquecível."
]

# Inicializa o estado do motivo se não existir
if 'motivo_atual' not in st.session_state:
    st.session_state.motivo_atual = "Clica no botão abaixo para descobrir..."

# Caixa de exibição do motivo
st.markdown(f'<div class="reason-box"><p class="reason-text">“{st.session_state.motivo_atual}”</p></div>', unsafe_allow_html=True)

# Botão interativo
if st.button("❤️ Mostrar motivo ❤️"):
    # Evita repetir o mesmo motivo consecutivamente se houver mais de um
    opcoes = [m for m in motivos if m != st.session_state.motivo_atual]
    st.session_state.motivo_atual = random.choice(opcoes if opcoes else motivos)
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
