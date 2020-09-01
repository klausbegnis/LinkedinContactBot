import pandas as pd
from scripts.tabela import Excel
from getpass import getpass
from scripts.sheetsapi import ApiSheets
from scripts.linkedinclass import LinkedinBot

# https://developers.google.com/sheets/api/quickstart/python?authuser=2 link para tutorial certinho sobre a "sheetsapi.py"

scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']  # não alterar, se necessitar delete antes a token.pickle
spreadsheet_id = ''  # id do url da sheets no google docs
range_name = 'Nomes!A:C'  # colunas que ele retira

if __name__ == '__main__':
    try:
        print('=============== Programa executado ===============')
        print('')
        print('Comandos: ([-s] [--start] Inicia o Scraper) ([-t] [--tabela] Cria tabela final a partir da progress.txt) ([-c] [--clear] Limpa a progress.txt)')
        print('')
        while True:
            print('=============== Esperando comando... ===============')
            print('')
            texto = input()
            comandos = ['-c', '--clear', '-s', '--start', '-t', '--tabela']
            if texto in comandos:
                if texto == '-c' or texto == '--clear':
                    colunas = ['nome', 'linkedin', 'telefone', 'email', 'trabalho']
                    df_clear = pd.DataFrame(columns=colunas)
                    df_clear.to_csv(r"./txts/progress.txt", header=True, index=False, sep=",")
                    print('')
                    print("Tabela de progresso limpa")
                    print('')
                if texto == '-s' or texto == '--start':
                    print("Retirando informações da tabela google...")
                    try:
                        api = ApiSheets(SCOPES=scopes, SPREADSHEET_ID=spreadsheet_id, RANGE_NAME=range_name)
                    except:
                        print("Um erro ocorreu ao retirar as informações da tabela do google.")
                        print('')
                        continue
                    print('Informações de login:')
                    print('')
                    print("Insira o email:")
                    user = input()
                    print('')
                    password = getpass()
                    try:
                        bot = LinkedinBot(user, password)
                    except:
                        print("Um erro ocorreu durante o scrapping de informações. Verifique a 'progress.txt' para")
                        print("descobrir até qual usuário o script funcionou corretamente.")
                    continue
                if texto == '-t' or texto == '--tabela':
                    print('Insira o nome da tabela: Utilize ([-b] [--back] para retornar se desejar retornar)')
                    print('')
                    nome = input()
                    if nome == '-b' or nome == '--back':
                        continue
                    else:
                        try:
                            excel = Excel(nome=nome)
                            print('')
                            print('Tabela criada com sucesso!')
                            print('')
                            continue
                        except:
                            print('')
                            print('[ERROR]')
                            print(f'Verifique se o arquivo {nome}.xlsx já existe e se encontra aberto.')
                            print('')
                            continue
            else:
                print("Comando não encontrado")
                continue
    finally:
        print("")
        print("Programa encerrado...")
        print("")
        print("==============================")