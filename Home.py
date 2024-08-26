import streamlit as st
import streamlit_antd_components as sac

class Home():
    def __init__(self) -> None:
        pass

    def app():
        st.header("NERDZGLC - Gym Leader Challenge")

        tl, tm, tr = st.columns([1,1,1])

        with tr:
            sac.alert(label='Season:', description='2024/2025', banner=False, size='lg', variant='filled', color='success', icon='controller')
        with tm:
            sac.alert(label='Data:', description='Terça 19:30',banner=False, size='lg', variant='filled', color='success', icon='controller')
        with tl:
            sac.alert(label='Local:', description='Nerdz Cards',banner=False, size='lg', variant='filled', color='success', icon='controller')

