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

ADDED_SHOPS = ['Nerdz']
# -------------------------------------------------------------------

#----------------------------------------------Const Variables----------------------------------------------
DECK_TYPES = ['Grass', 'Fire', 'Water', 'Eletric', 'Psychic', 'Fighting', 'Dark', 'Metal', 'Fairy', 'Dragon', 'Normal']

PLAYER_DICT = {
            "player": "",
            "win": False,
            "deck_type": "",
            "place": 0,
            "score": "",
            "drop": False
}

LEAGUE_DICT =  {
                "date" : "",
                "decks" : []
}
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

        if "data_frame" not in st.session_state:
            st.session_state.data_frame = None

        if "player" not in st.session_state:
            st.session_state.player = ""
        if "player_win" not in st.session_state:
            st.session_state.player_win = None
        if "player_deck_type" not in st.session_state:
            st.session_state.player_deck_type = ""
        if "player_place" not in st.session_state:
            st.session_state.player_place = 0
        if "player_score" not in st.session_state:
            st.session_state.player_score = ""
        if "player_drop" not in st.session_state:
            st.session_state.player_drop = None

        if "league_date" not in st.session_state:
            st.session_state.league_date = ""
        if "league_local" not in st.session_state:
            st.session_state.league_local = ""
    
    # Function for player's score validation
    def score_formatting(score):
        score_aux = score.split("/")
        
        if len(score_aux) != 3:
            return False
        
        for item in score_aux:
            if not(item.isnumeric()) or int(item) < 0:
                return False
        
        return True


    # Function for verify data from form. If all the information is correct, return True. Otherwise return False.
    def verify_data(temp_player_data):
        for key, value in temp_player_data.items():
            if key is None or (isinstance(value, str) and not value.strip()) or (isinstance(value, list)):
                if key == "place" and value == 0:
                    st.warning("A colocação do jogador deve ser maior do que zero!")
                else:
                    st.warning(f"O campo {key} está mal formatado")
                return False
            
        # Player's Score validation. (This field must be {x/x/x}, where each 'x' is a positive integer)
        if League.score_formatting(temp_player_data['score']):
            return True
        else:
            st.warning(f"O campo score está mal formatado")
            return False


    #Function for 'add' button clicked, creates data with information given by user and adds to the form.
    def group_data(temp_player_data):
        confirmation = League.verify_data(temp_player_data)
        if confirmation:
            st.session_state.form_data.append({'player': st.session_state.player,
                                               'win': st.session_state.player_win,
                                               'deck_type': st.session_state.player_deck_type,
                                               'place': st.session_state.player_place,
                                               'score': st.session_state.player_score,
                                               'drop': st.session_state.player_drop})
        else:
            print("Dados inconsistentes, revise.")


    def add_button_callback():
        # Copy all information to a temporary variable
        temp_player = PLAYER_DICT
        temp_player['player'] = st.session_state.player
        temp_player['win'] = st.session_state.player_win
        temp_player['deck_type'] = st.session_state.player_deck_type
        temp_player['place'] = st.session_state.player_place
        temp_player['score'] = st.session_state.player_score
        temp_player['drop'] = st.session_state.player_drop
        
        # Verify the information inputed from the user
        League.group_data(temp_player)
        
        # Clear widgets on screen
        st.session_state['league_name_player'] = ""
        st.session_state['league_player_win'] = False
        st.session_state['league_player_deck_type'] = None
        st.session_state['league_player_place'] = 1
        st.session_state['league_player_score'] = ""
        st.session_state['league_player_drop'] = False

    def send_results():
        print("WIP")
        for item in st.session_state.form_data:
            print(item)

        st.session_state.form_data = []
        st.session_state.data_frame = None

        sac.result(label='Liga inserida', description='A liga do dia X, foi inserida com sucesso no banco', status='success')
        
        

    #Main function of League.py
    def app(page):
        # If the page selected is "add", the 'Add Page' is displayed
        if page == "add":
            st.header("LEAGUE | ADD")

            with st.container(border=True):
                tl, tm, tr = st.columns([1,1,1])

                with tl:
                    st.session_state.player = st.text_input(label="Name", key="league_name_player")

                    st.session_state.player_win = st.checkbox(label='Win', key="league_player_win")

                with tm:
                    st.session_state.player_deck_type = st.selectbox(label="Deck Type", options=DECK_TYPES, key="league_player_deck_type", index=None)

                    st.session_state.player_place = st.number_input(label="Place", format="%d", value='min', min_value=1, step=1, key="league_player_place")

                    st.session_state.add_button_state = st.button(label="Adicionar", key="button_adicionar_liga", on_click=League.add_button_callback)

                with tr:
                    st.session_state.player_score = st.text_input(label="Score", key="league_player_score", help="Coloque o resultado do jogador no formato X/X/X, com as barras inclusas.")

                    st.session_state.player_drop = st.checkbox(label="Drop?", key="league_player_drop")


            if st.session_state.add_button_state:
                if "form_data" in st.session_state:
                    if st.session_state.form_data != None and st.session_state.form_data != 0:
                        st.session_state.data_frame = pd.DataFrame(st.session_state.form_data)

            with st.container(border=True): 
                bl, bm, br = st.columns([1,1,1])

                with bl:
                    st.session_state.league_local = st.selectbox(label="Local da Liga", key="league_local_op", options=ADDED_SHOPS, index=None)

                with br:
                    st.session_state.league_date = st.text_input(label="Data", key="league_date_op", help="Colocar a data no formato dd-mm-aaaa, com os traços entre os valores.")

                st.table(st.session_state.data_frame)
            st.button(label="Enviar", key="send_league_results", on_click=League.send_results)

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
                