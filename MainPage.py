import streamlit as st
import streamlit_antd_components as sac

import Home, About, Coffee, Contact, League, Login, Connection

class MultiPageApp:
    def __init__(self) -> None:

        if "logged" not in st.session_state:
            st.session_state.logged = False

        if "registered" not in st.session_state:
            st.session_state.registered = False

        if "mongo_connection" not in st.session_state:
            st.session_state.mongo_connection = ""

        if "current_page" not in st.session_state:
            st.session_state.current_page = "Login"

        Connection.Connection()

        self.run_main()

    def logout(self):
        st.session_state.logged = False
        st.session_state.registered = False
        st.session_state.current_page = "Login"

    def run_main(self):
        # Page configuration
        st.set_page_config(page_title="GLCLiga", layout='wide')

        # Side bar configuration
        with st.sidebar:

            if st.session_state.logged:
                app = sac.menu([sac.MenuItem('Home', icon='house-fill'),
                                sac.MenuItem('Liga', icon='controller', children=[
                                    sac.MenuItem('Adicionar Liga', icon='floppy-fill'),
                                    sac.MenuItem('Ver Resultados', icon='search')
                                ]),
                                sac.MenuItem('Sobre', icon='person-lines-fill'),
                                sac.MenuItem('Contato', icon='briefcase-fill'),
                                sac.MenuItem('Buy Me a Coffee', icon='cup-hot-fill')
                                ], open_all=False, variant='filled')
                if st.session_state.logged:
                    st.button(label="Logout", key="button_logout", on_click=self.logout)
            else:
                app = sac.menu([sac.MenuItem('Login', icon='house-fill'),
                                sac.MenuItem('Esqueci a Senha', icon='house-fill'),
                                sac.MenuItem('Criar Conta', icon='person-lines-fill')
                                ], open_all=False, variant='filled')
        
        
        # Para cada uma das possíveis escolhas dentro do sidebar, é verificado
        # qual foi o objeto escolhido. Assim, é escolhido de forma correta qual
        # das páginas deve ser aberta.

        print(st.session_state.logged)

        if not(st.session_state.logged):
            Login.Login()
            if app == "Criar Conta" and not(st.session_state.registered):
                st.session_state.current_page = "Criar Conta"
                Login.Login.register()
            elif app == "Esqueci a Senha":
                st.session_state.current_page = "Esqueci a Senha"
                Login.Login.forgotten()
            elif app == "Login" or st.session_state.current_page == "Login":
                st.session_state.current_page = "Login"
                Login.Login.app()
        else:    
            if app == "Home":
                st.session_state.current_page = "Home"
                Home.Home()
                Home.Home.app()

            if app == "Sobre":
                st.session_state.current_page = "About"
                About.About()
                About.About.app()

            if app == "Contato":
                st.session_state.current_page = "Contact"
                Contact.Contact()
                Contact.Contact.app()

            if app == "Adicionar Liga":
                st.session_state.current_page = "Add League"
                League.League()
                League.League.app("add")

            if app == "Ver Resultados":
                st.session_state.current_page = "View Results"
                League.League()
                League.League.app("view")
            
            if app == "Buy Me a Coffee":
                st.session_state.current_page = "Buy Me a Coffee"
                Coffee.Coffee()
                Coffee.Coffee.app()

if __name__ == "__main__":
    mpa = MultiPageApp()