import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pandas as pd


class ApiSheets():
    def __init__(self, SCOPES, SPREADSHEET_ID, RANGE_NAME):
        self.SCOPES = SCOPES
        self.SPREADSHEET_ID = SPREADSHEET_ID
        self.RANGE_NAME = RANGE_NAME
        self.make_dataframe()

    def gsheet_api_check(self):
        creds = None
        if os.path.exists('scripts/token.pickle'):
            with open('scripts/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('scripts/token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def pull_sheet_data(self):
        creds = self.gsheet_api_check()
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=self.SPREADSHEET_ID,
            range=self.RANGE_NAME).execute()
        values = result.get('values', [])
        
        if not values:
            print('')
            print('Dados não encontrados')
        else:
            rows = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                    range=self.RANGE_NAME).execute()
            data = rows.get('values')
            print('')
            print("Dados copiados.")
            return data

    def make_dataframe(self):
        data = self.pull_sheet_data()
        nomes_df = pd.DataFrame(data[1:], columns=data[0])
        nomes = nomes_df['Nome'].tolist()
        permissao = nomes_df['Permissão'].tolist()
        links = nomes_df['Link'].tolist()
        nomes_permitidos = [nome for nome in nomes if permissao[nomes.index(nome)] == "Sim"]
        links_permitidos = [link for link in links if permissao[link.index(link) == "Sim"]]
        columns = ['nomes', 'links']
        data = {
            'nomes' : nomes_permitidos,
            'links' : links_permitidos
        }
        df_nomes = pd.DataFrame(data=data, columns=columns)
        df_nomes.to_csv(r"./txts/nomes.txt", header=True, index=False, sep=",")
        print('')
        print("Nomes salvos")
        print('')

if __name__ == '__main__':
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']  # do not change this
    spreadsheet_id = ''  # url id from google sheets data
    range_name = 'Nomes!A:C'  # columns to retrieve data
    api = ApiSheets(SCOPES=scopes, SPREADSHEET_ID=spreadsheet_id, RANGE_NAME=range_name)