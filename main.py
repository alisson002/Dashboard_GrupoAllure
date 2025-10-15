import streamlit as st
from st_pages import add_page_title
from pathlib import Path


# Estrutura de navegação do sistema
# O dicionário 'pages' mapeia os nomes das páginas para suas respectivas funções, em outras palavras, organiza e categoriza as diferentes seções do sistema.
pages = {
    "":
        [st.Page(Path('paginas/inicio.py'), title="Início", icon = "🏠", default = True)],
    "Dashboards": [
        st.Page(Path('paginas/visao_geral.py'), title="Visão Geral", icon = "📊"),
        st.Page(Path(('paginas/visualizacao_unidade.py')), title="Visualização por Unidade", icon = "📈"),
        ],
    # "":
    #     [st.Page(Path(('paginas/visualizacao_unidade.py')), title="Visualização por Unidade", icon = "📈")],
}

# Criação do menu de navegação
# O método st.navigation cria um menu de navegação baseado na estrutura definida no dicionário 'pages', permitindo que os usuários naveguem entre as diferentes páginas do sistema através da criação de um menu interativo.
pg = st.navigation(pages)

# Adiciona o título personalizado para a página ativa
# Utiliza o título e o ícone definidos na estrutura de navegação para personalizar a aparência da página atual.
add_page_title(pg)

# Executa a página selecionada pelo usuário
# O método run() carrega e exibe a lógica da página correspondete no menu lateral
pg.run()