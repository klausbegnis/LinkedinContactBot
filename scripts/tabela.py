import xlsxwriter
import pandas as pd 
from scripts.sheetsapi import ApiSheets


class Excel():
    def __init__(self, nome, SCOPES, SPREADSHEET_ID, RANGE_NAME):
        # Leitura banco de dados

        self.scopes = SCOPES
        self.spreadsheet_id = SPREADSHEET_ID 
        self.range_name = RANGE_NAME
        try:
            api = ApiSheets(SCOPES=self.scopes, SPREADSHEET_ID=self.spreadsheet_id, RANGE_NAME=self.range_name)
            data = api.pull_sheet_data()
            nomes_df = pd.DataFrame(data[1:], columns=data[0])
            self.nomes_g = nomes_df['Nome'].tolist()
            self.linkss_g = nomes_df['Linkedin'].tolist()
            self.telefones_g = nomes_df['Telefone'].tolist()
            self.emails_g = nomes_df['Email'].tolist()
            self.enderecos_g = nomes_df['Endereço'].tolist()
            self.trabalhos_g = nomes_df['Trabalho'].tolist()
            self.state = 1
        except:
            self.state = 2
            print("Não foi possível abrir o banco de dados, salvaremos sem moficiação")
        #Leitura da Progress.txt
        self.tab = nome
        self.prgs = pd.read_csv(r"./txts/progress.txt")
        self.nomes = self.prgs['nome'].tolist()
        self.links = self.prgs['linkedin'].tolist()
        self.telefones = self.prgs['telefone'].tolist()
        self.emails = self.prgs['email'].tolist()
        self.trabalhos = self.prgs['trabalho'].tolist()
        self.enderecos = self.prgs['endereco'].tolist()

        self.faz_gráfico()


    def faz_gráfico(self):
        workbook =  xlsxwriter.Workbook(f"./Tabelas/{self.tab}.xlsx")
        worksheet = workbook.add_worksheet("Banco de Dados Alumni")
        worksheet.set_column(first_col=0, last_col=1, width=40)
        worksheet.set_column(first_col=2, last_col=2, width=20)
        worksheet.set_column(first_col=3, last_col=5, width=40)

        config_titulo = workbook.add_format({'bold': True, 'bg_color': '#C0C0C0'})
        cinza = workbook.add_format({'bg_color': '#C0C0C0'})
        branco = workbook.add_format({'bg_color': '#ffffff'})
        amarelo = workbook.add_format({'bg_color': '#FFFF00'})

        columns = [['Nome', 'A'], ['Linkedin', 'B'], ['Telefone', 'C'], ['Email', 'D'], ['Endereço', 'E'] , ['Trabalho', 'F']]

        def faz_coluna(coluna):
            for i in range(len(coluna)):
                coluna_letra = str(coluna[i][1])
                coluna_var = str(coluna[i][0])
                worksheet.write(f'{coluna_letra}1', f'{coluna_var}', config_titulo)

        if self.state == 1:

            def faz_linha(dados, letra, tipo):
                tipo = tipo
                letra_up = str(letra).upper()
                for i in range(len(dados)):

                    dado = dados[i]
                    tg = self.telefones_g[i]
                    eg = self.emails_g[i]
                    e_g = self.enderecos_g[i]
                    t_g = self.trabalhos_g[i]

                    if i == 0:
                        if tipo != 0:

                            if tipo == 'telefone':
                                if dado == tg:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)
                                else:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)
                            
                            if tipo == 'email':
                                if dado == eg:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)
                                else:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)

                            if tipo == 'endereco':
                                if dado == e_g:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)
                                else:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)

                            if tipo == 'trabalho':
                                if dado == t_g:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)
                                else:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)

                        else:
                            worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)

                    if (i % 2) == 0:
                        if i != 0:
                            if tipo != 0:
                                
                                if tipo == 'telefone':
                                    if dado == tg:
                                        worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)
                                    else:
                                        worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)
                                
                                if tipo == 'email':
                                    if dado == eg:
                                        worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)
                                    else:
                                        worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)

                                if tipo == 'endereco':
                                    if dado == e_g:
                                        worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)
                                    else:
                                        worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)

                                if tipo == 'trabalho':
                                    if dado == t_g:
                                        worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)
                                    else:
                                        worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)

                            else:
                                worksheet.write(f'{letra_up}{i + 2}', f'{dado}', branco)
                    else:
                        if tipo != 0:

                            if tipo == 'telefone':
                                if dado == tg:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', cinza)
                                else:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)
                                
                            if tipo == 'email':
                                if dado == eg:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', cinza)
                                else:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)

                            if tipo == 'endereco':
                                if dado == e_g:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', cinza)
                                else:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)

                            if tipo == 'trabalho':
                                if dado == t_g:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', cinza)
                                else:
                                    worksheet.write(f'{letra_up}{i + 2}', f'{dado}', amarelo)

                        else:
                            worksheet.write(f'{letra_up}{i + 2}', f'{dado}', cinza)
        else:
            def faz_linha(dados, letra, tipo):
                tipo = tipo
                letra_up = str(letra).upper()
                for i in range(len(dados)):
                    if i == 0:
                        worksheet.write(f'{letra_up}{i + 2}', f'{dados[i]}', branco)
                    if (i % 2) == 0:
                        if i != 0:
                            worksheet.write(f'{letra_up}{i + 2}', f'{dados[i]}', branco)
                    else:
                        worksheet.write(f'{letra_up}{i + 2}', f'{dados[i]}', cinza)


        faz_coluna(columns)
        faz_linha(self.nomes, 'a', 0)
        faz_linha(self.links, 'b', 0)
        faz_linha(self.telefones, 'c', 'telefone')
        faz_linha(self.emails, 'd', 'email')
        faz_linha(self.enderecos, 'e', 'endereco')
        faz_linha(self.trabalhos, 'f', 'trabalho')

        workbook.close()

        
