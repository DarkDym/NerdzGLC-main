import streamlit as st
import streamlit_antd_components as sac

class Contact():
    def __init__(self) -> None:
        pass

    def app():
        st.header("Meus Contatos")

        sac.segmented(
            items=[
                sac.SegmentedItem(label="alleff_dymytry@outlook.com", icon="envelope-at-fill"),
                sac.SegmentedItem(label='https://github.com/DarkDym', icon='github')
            ], color='red', use_container_width=True, readonly=True, index=None)
        
        sac.segmented(
            items=[
                sac.SegmentedItem(label="(00) 00000-0000", icon="whatsapp"),
                sac.SegmentedItem(label='www.linkedin.com/in/alleff-dymytry', icon='linkedin')
            ], color='red', use_container_width=True, readonly=True, index=None)