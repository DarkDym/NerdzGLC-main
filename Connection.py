import streamlit as st

import pymongo
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure, InvalidName

class Connection:
    def __init__(self) -> None:
        self.MONGO_URI =  st.secrets['MONGO_URI']

        if 'mongo_users' and 'mongo_liga' not in st.session_state:

            try:
                # Conectar ao MongoDB
                client = pymongo.MongoClient(self.MONGO_URI, serverSelectionTimeoutMS=5000)
                db = client['data']
                mongo_users = db['Users']
                mongo_liga = db['Liga']

                
                # Verificar se a conexão foi bem-sucedida
                client.admin.command('ping')
                print("Conectado ao MongoDB Atlas com sucesso!")
                st.session_state.mongo_users = mongo_users
                st.session_state.mongo_liga = mongo_liga

                # TESTE
                print(f"TESTE DO QUE VEIO NA CONEXÃO USERS: {st.session_state.mongo_users}")
                print(f"TESTE DO QUE VEIO NA CONEXÃO LIGA: {st.session_state.mongo_liga}")

            except ServerSelectionTimeoutError as e:
                print(f"Erro de conexão: {e}")
                exit(1)
            except InvalidName as e:
                print(f"Nome de banco de dados ou collection inválido: {e}")
                exit(1)
            except OperationFailure as e:
                print(f"Falha de operação: {e}")
                exit(1)