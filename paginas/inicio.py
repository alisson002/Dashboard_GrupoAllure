import streamlit as st
from st_pages import Page, add_page_title, Section, get_nav_from_toml #, show_pages
import pandas as pd
from PIL import Image
from functions.manipulacao_de_imagem import img_to_base64 # Importa a função para manipulação de imagens, que será usada para centralizar a imagem do Grupo Allure.

# Faz com que a opção "[] Wide Mode" fique sempre selecionada, ou seja, a página sempre abrirá em modo wide. Sendo assim, as informações ficarão mais distribuídas na tela.
# st.set_page_config(layout="wide", initial_sidebar_state="collapsed") # A sidebar já está colapsada por padrão.
# st.set_page_config(layout="wide", initial_sidebar_state="expanded") # A sidebar vem expandida por padrão.
st.set_page_config(
    layout="wide", 
    initial_sidebar_state="auto", 
    menu_items={
        'Get Help': 'mailto:am.analistadedados@gmail.com',
        'Report a bug': 'mailto:am.analistadedados@gmail.com',
        'About': "Aplicação feita com Streamlit para visualização de dados financeiros do Grupo Allure. \n\n Entre em contato: am.analistadedados@gmail.com"
        }
)

imagem_placeholder = st.empty() # Placeholder para a imagem

# É feito dessa forma para evitar que a imagem seja recarregada toda vez que a página for atualizada
# Image.open abre a imagem e a carrega na memória
GrupoAllure_imagePath = Image.open('imagens/GrupoAllure.jpg') # Carrega a imagem do Grupo Allure


# Fazendo dessa forma a imagem não estava ficando centralizada
# col1, col2, col3 = st.columns(3) # Cria uma coluna para centralizar a imagem

# with col2: # Centraliza a imagem na coluna
    
#     # Recebe o caminho da imagem e a exibe no placeholder, ajustando a largura para se adequar à coluna
#     # Dá no mesmo que usar st.image(GrupoAllure_imagePath), pois o placeholder está ocupando toda a largura disponível, além disso ele já recebe o objeto st.empty() que é um espaço reservado para a imagem.
#     imagem_placeholder.image(GrupoAllure_imagePath, width=600) # Exibe a imagem no placeholder

# Converter a imagem
# A função img_to_base64 converte a imagem para base64, que é um formato que pode ser embutido diretamente no HTML, permitindo a centralização da imagem.
# Recebe a imagem e retorna a string em base64.
img_base64 = img_to_base64(GrupoAllure_imagePath)

# Exibir com HTML
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{img_base64}" width="300" />
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .nav-bar {
        font-size: 12px;
        text-align: justify;
    }
    .nav-item {
        text-align: Right;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#<p>Este sistema foi desenvolvido para um projeto de pesquisa de TCC com o objetivo de realizar um estudo com base nos dados da unidade SIASS da UFRN acerca dos afastamentos dos servidores atendidos, com a finalidade de gerar indicadores visando auxiliar na melhoria da saúde do servidor e/ou no trabalho interno do administrativo do setor em questão.</p>
#<p>Bem como gerar informações relevantes a respeito dos afastamentos em cada setor e, diante disso, influenciar na melhoria da qualidade de saúde dos trabalhadores, mediante a criação de políticas públicas, gestão e/ou chefia ou através da atuação de grupos de servidores que buscam essas melhorias contudo não tem os indicadores necessários para saber onde e de qual forma agir.</p>
st.markdown(
    """
    <div class="nav-bar">
        <p>Este sistema foi desenvolvido para o Grupo Allure, com o objetivo de consolidar e analisar informações financeiras de forma clara, interativa e acessível. A finalidade é disponibilizar indicadores que auxiliem na gestão estratégica da empresa, contribuindo para a tomada de decisões baseada em dados.</p>
        <p>Além disso, a dashboard visa gerar informações relevantes sobre o desempenho financeiro, possibilitando identificar tendências, oportunidades e riscos, bem como apoiar na criação de estratégias que promovam maior eficiência, sustentabilidade e crescimento para o Grupo Allure.</p>
        <p class="nav-item"><b>Criado por:</b> Alisson Moreira.</p>
    </div>
    """,
    unsafe_allow_html=True
)

with st.expander("O que é o Grupo Allure?"):
    st.write("...")
with st.expander("Quais serviços prestamos?"):
    st.write("...")
with st.expander("Onde fica?"):
    st.write("...")

