import streamlit as st

class Login:
    def __init__(self) -> None:
        if "login" not in st.session_state:
            st.session_state.login = None
        if "logged" not in st.session_state:
            st.session_state.logged = False
        else:
            st.session_state.logged = False

    '''
    Preciso fazer os ajustes em relação ao login na plataforma.
    Para que isso seja realizado, tenho que fazer a conexão com o banco de dados.
    '''

    def app():
        with st.container(border=True):
            st.text_input(label="Username", key="player_login")

            st.text_input(label="Password", key="player_password")

            st.session_state.login = st.button(label="Login", key="button_login")

        if st.session_state.login:
            st.session_state.logged = True
            st.session_state.current_page = "Home"
