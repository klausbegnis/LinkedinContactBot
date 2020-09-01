import xlsxwriter
import pandas as pd 

class Excel():
    def __init__(self, nome):
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
        branco = workbook.add_format({'bold': True, 'bg_color': '#ffffff'})

        columns = [['Nome', 'A'], ['Linkedin', 'B'], ['Telefone', 'C'], ['Email', 'D'], ['Endereço', 'E'] , ['Trabalho', 'F']]

        def faz_coluna(coluna):
            for i in range(len(coluna)):
                coluna_letra = str(coluna[i][1])
                coluna_var = str(coluna[i][0])
                worksheet.write(f'{coluna_letra}1', f'{coluna_var}', config_titulo)

        def faz_linha(dados, letra):
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
        faz_linha(self.nomes, 'a')
        faz_linha(self.links, 'b')
        faz_linha(self.telefones, 'c')
        faz_linha(self.emails, 'd')
        faz_linha(self.enderecos, 'e')
        faz_linha(self.trabalhos, 'f')

        workbook.close()
