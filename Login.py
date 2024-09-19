import streamlit as st
import streamlit_antd_components as sac

class Login:
    def __init__(self) -> None:
        if "login" not in st.session_state:
            st.session_state.login = None
        if "register" not in st.session_state:
            st.session_state.register = None
        if "logged" not in st.session_state:
            st.session_state.logged = False
        else:
            st.session_state.logged = False

    def verify_login(user,password):

        q_user = st.session_state.mongo_users.find({})

        flag_login = True

        for users in q_user:
            if (users['user'] == user and users['password'] == password):
                sac.result(label='Login', description='Realizado com Sucesso', status='success')
                st.session_state.logged = True
                st.session_state.current_page = "Home"
                flag_login = False
        
        if flag_login:
            sac.result(label='Usuário ou Senha', description='Incorretos', status='error')

    def login_button(user, password):

        '''
            Colocar nesta parte a chamada da função qu irá fazer a verificação do usuário no banco.
            Utilizar uma flag para dizer se o usuário possui os direitos de ADMIN;
        '''

        Login.verify_login(user,password)

    def regigister_button(user,pass1, pass2):
        if pass1 != pass2:
            sac.result(label='Senhas', description='Diferentes', status='error')
            return False
        else:
            data = {"user": user, "password":pass1, "type":"normal"}

            result = st.session_state.mongo_users.insert_one(data)
            print(f"Documento inserido com o ID: {result.inserted_id}")
            sac.result(label='Conta', description='Criada com Sucesso', status='success')
            st.session_state.current_page = "Login"
            st.session_state.registered = True
            
        
        return True

    def app():
        with st.container(border=True):
            user = st.text_input(label="Username", key="player_login")

            password = st.text_input(label="Password", key="player_password", type="password")

            st.session_state.login = st.button(label="Login", key="button_login", on_click=Login.login_button, args=(user,password,))

    def register():
        with st.container(border=True):
            user = st.text_input(label="Username", key="create_player_login")

            password = st.text_input(label="Password", key="create_player_password", type="password")

            c_password = st.text_input(label="Confirm Password", key="create_player_confirm_password", type="password")

            '''
                Adicionar nesta região a verificação se o usuário está logado ou não, para que esta opção
                esteja disponível; Isto somente é válido caso seja um usuário ADMIN.
            '''

            st.session_state.register = st.button(label="Criar Conta", key="button_register", on_click=Login.regigister_button, args=(user,password,c_password,))

    def forgotten():
        st.header("WIP")
        print("WIP")


