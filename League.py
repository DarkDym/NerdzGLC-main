#---------------------Stremlit imports--------------------------------
import streamlit as st
import streamlit_antd_components as sac
import streamlit_echarts as ste
#----------------------------------------------------------------------

#----------------------Data imports------------------------------------
import pandas as pd
#----------------------------------------------------------------------

# Para prototipagem, pode ser excluida depois caso não mais utilizada
import json
import matplotlib.pyplot as plt
import numpy as np
# -------------------------------------------------------------------

#----------------------------------------------Const Variables----------------------------------------------
DECK_TYPES = ['Grass', 'Fire', 'Water', 'Eletric', 'Psichic', 'Fighting', 'Dark', 'Metal', 'Fairy', 'Dragon', 'Normal']
#-----------------------------------------------------------------------------------------------------------

class League():
    def __init__(self) -> None:
        # Session State initializer
        print("Initializing state variables!")
        if "form_state" not in st.session_state:
            st.session_state.form_state = None
        else:
            st.session_state.form_state = None

        if "add_button_state" not in st.session_state:
            st.session_state.add_button_state = None
        else:
            st.session_state.add_button_state = None

        if "form_data" not in st.session_state:
            st.session_state.form_data = []

        if "player" not in st.session_state:
            st.session_state.player = {
                                        "name": "",
                                        "win": False,
                                        "deck_type": "",
                                        "place": 0,
                                        "score": "",
                                        "drop": False
                                    }

    
    # Function for verify data from form. If all the information is correct, return True. Otherwise return False.
    def verify_data(temp_player_data):
        for key, value in temp_player_data.items():
            if key is None or (isinstance(value, str) and not value.strip()) or (isinstance(value, list)):
                if key == "place" and value == 0:
                    st.warning("A colocação do jogador deve ser maior do que zero!")
                else:
                    st.warning(f"O campo {key} está mal formatado")
                return False
        return True


    #Function for 'add' button clicked, creates data with information given by user and adds to the form.
    def group_data(temp_player_data):
        confirmation = League.verify_data(temp_player_data)
        if confirmation:
            print("yes")
            st.session_state.form_data.append(temp_player_data)
        else:
            print("Dados inconsistentes, revise.")
        

    #Main function of League.py
    def app(page):
        # If the page selected is "add", the 'Add Page' is displayed
        if page == "add":
            st.header("LEAGUE | ADD")

            with st.container(border=True):
                tl, tm, tr = st.columns([1,1,1])

                with tl:
                    st.session_state.player['name'] = st.text_input(label="Name", key="name_player")

                    st.session_state.player['win'] = st.checkbox(label='Win', key="player_win")

                with tm:
                    st.session_state.player['deck_type'] = st.selectbox(label="Deck Type", options=DECK_TYPES, key="player_deck_type", index=None)

                    st.session_state.player['place'] = st.number_input(label="Place", format="%d", value='min', min_value=1, step=1, key="player_place")

                    st.session_state.add_button_state = st.button("Add")

                with tr:
                    st.session_state.player['score'] = st.text_input(label="Score", key="player_score", help="Coloque o resultado do jogador no formato X/X/X, com as barras inclusas.")

                    st.session_state.player['drop'] = st.checkbox(label="Drop?", key="player_drop")

            
            # Add button verification
            if st.session_state.add_button_state:                

                League.group_data(st.session_state.player)

            if st.session_state.add_button_state:
                if "form_data" in st.session_state:
                    if st.session_state.form_data != None and st.session_state.form_data != 0:
                        df = pd.DataFrame(st.session_state.form_data)
                        st.table(df)

        # If the page selected is "view", the 'View Page' is displayed
        elif page == "view":
            st.header("LEAGUE | VIEW")

            with st.container(border=True):
                st.selectbox(label="Data", options=[], key="glc_league_date")

            tl, tm, tr = st.columns([1,1,1])

            # This part of the code is a prototype for data display.
            # In the future, will be replaced for a function. This function will search the league's date in database. 
            with open('statistics_glc.json', 'r') as file:
                data = json.load(file)

            counted_deck_types = {deck_type: 0 for deck_type in DECK_TYPES}
            types = [x['type'] for x in data[0]['decks']]
            for card_type in types:
                if card_type in counted_deck_types:
                    counted_deck_types[card_type] += 1
            # -----------------------------------------------------------------------------------

            decks_data = []
            for card_type in DECK_TYPES:
                decks_data.append({"value": counted_deck_types[card_type], "name":card_type})
                    

            with tm:
                # Pie Chart Options
                options = {
                    "tooltip": {"trigger": "item"},
                    "legend": {"orient": "vertical",
                                "left": "left",
                                "color":"#fff",
                                # Deck types for legend in the chart will always be the same.
                                "data": DECK_TYPES},
                    "series": [
                        {
                            "name": f"LIGA GLC {data[0]['date']}",
                            "type": "pie",
                            "radius": ["40%", "70%"],
                            "avoidLabelOverlap": True,
                            "itemStyle": {
                                "borderRadius": 10,
                                "borderColor": "#000",
                                "borderWidth": 2,
                            },
                            "label": {"show": True, "color":"#fff"},
                            "emphasis": {
                                "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                            },
                            "labelLine": {"show": True},
                            "data": decks_data,
                            "colorBy": "data",
                            "stillShowZeroSum": True,
                        }
                    ]
                }
            # Pie Chart display
            ste.st_echarts(
                options=options, height="500px",
            )
                