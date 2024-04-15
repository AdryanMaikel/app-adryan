"""
Utilizado para se conectar com o google Sheets e pegar os dados de
uma planilha.
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials as SA

SCOPE = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

CREDENTIALS = SA.from_json_keyfile_name("src/credentials.json", SCOPE)
GC = gspread.authorize(CREDENTIALS)

SS = GC.open_by_key("1ZqJfSMkqz2ywSmNjw_r_bTgr9QxP6IgiilMdyIim8II")

WS = SS.worksheet("informações")

WS.get_values("C:C")

OCORRENCIAS = [ocorrencia[0] for ocorrencia in WS.get_values("A:A")
               if ocorrencia]
PROBLEMAS = [problema[0] for problema in WS.get_values("B:B") if problema]
OPERADORES = [operador[0] for operador in WS.get_values("C:C") if operador]
SENTIDOS = [sentido[0] for sentido in WS.get_values("E:E") if sentido]


if __name__ == "__main__":
    print(OPERADORES)
