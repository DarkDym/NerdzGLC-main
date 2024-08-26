import streamlit as st
import streamlit_antd_components as sac

class Coffee():
    def __init__(self) -> None:
        pass

    def app():
        st.header("Buy me a Coffee")

        tl, tm, tr = st.columns([1,1,1])

        with tl:
            sac.alert(label='Pix:', description=':D', banner=False, size='lg', variant='filled', color='success', icon='controller')
        with tm:
            sac.alert(label='Paypal:', description=':D',banner=False, size='lg', variant='filled', color='success', icon='controller')
        with tr:
            sac.alert(label='Cartinhas:', description=':D',banner=False, size='lg', variant='filled', color='success', icon='controller')
