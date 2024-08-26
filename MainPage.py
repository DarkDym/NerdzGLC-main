import streamlit as st
import streamlit_antd_components as sac

import Home, About, Coffee, Contact, League, Login

class MultiPageApp:
    def __init__(self) -> None:

        if "logged" not in st.session_state:
            st.session_state.logged = False
    
        self.run_main()

    def logout(self):
        st.session_state.logged = False

    def run_main(self):
        # Page configuration
        st.set_page_config(page_title="NERDZGLC", layout='wide')

        # Side bar configuration
        with st.sidebar:
            app = sac.menu([sac.MenuItem('Home', icon='house-fill'),
                            sac.MenuItem('League', icon='controller', children=[
                                sac.MenuItem('Add League', icon='floppy-fill'),
                                sac.MenuItem('View Results', icon='search')
                            ]),
                            sac.MenuItem('About', icon='person-lines-fill'),
                            sac.MenuItem('Contact', icon='briefcase-fill'),
                            sac.MenuItem('Buy Me a Coffee', icon='cup-hot-fill')
                            ], open_all=False, variant='filled')
            
            st.button(label="Logout", key="button_logout", on_click=self.logout)
        
        
        # Para cada uma das possíveis escolhas dentro do sidebar, é verificado
        # qual foi o objeto escolhido. Assim, é escolhido de forma correta qual
        # das páginas deve ser aberta.

        print(st.session_state.logged)

        if not(st.session_state.logged):
            Login.Login()
            Login.Login.app()
        else:    
            if app == "Home":
                st.session_state.current_page = "Home"
                Home.Home()
                Home.Home.app()

            if app == "About":
                st.session_state.current_page = "About"
                About.About()
                About.About.app()

            if app == "Contact":
                st.session_state.current_page = "Contact"
                Contact.Contact()
                Contact.Contact.app()

            if app == "Add League":
                st.session_state.current_page = "Add League"
                League.League()
                League.League.app("add")

            if app == "View Results":
                st.session_state.current_page = "View Results"
                League.League()
                League.League.app("view")
            
            if app == "Buy Me a Coffee":
                st.session_state.current_page = "Buy Me a Coffee"
                Coffee.Coffee()
                Coffee.Coffee.app()

if __name__ == "__main__":
    mpa = MultiPageApp()