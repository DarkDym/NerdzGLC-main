import streamlit as st

class About():
    def __init__(self) -> None:
        pass

    def app():
        st.header("Sobre o Projeto NERDZGLC")

        with st.container(border=True):
            st.markdown('''
                        Este é um projeto da comunidade para a comunidade.
                        As informações aqui dispostas são de cunho público,
                        qualquer um pode ter acesso a elas pelas canais corretos.
                        Todos os direitos de construção e manutenção deste site pertencem
                        a Alleff Dymytry. Para mais informações, acesse a aba 'Contact'
                        para meios de comunicação e sugestões.Este projeto não visa fins
                        lucrativos e não tem nenhum envolvimento direto com a loja
                        Nerdz Cards, somente utiliza as informações obtidas por eles em seus eventos.
                        Caso exista algum interesse de ajudar a manter o projeto operante,
                        utilize a aba 'Contact' ou 'Buy me a Coffee' para saber como ajudar.''')

        