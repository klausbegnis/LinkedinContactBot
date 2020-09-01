from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


class LinkedinBot():
    def __init__(self, user, password):
        self.username = user
        self.password = password
        self.driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver\chromedriver.exe")  # path do chromedriver.exe (baixar na mesma versão do navegador)
        self.driver.get("https://www.linkedin.com/home")  # LINK
        sleep(2)
        self.login()
        sleep(2)
        self.scrap_user_profile()

    def login(self):
        self.driver.find_element_by_id("session_key").send_keys(self.username)  # procura input de nome de usuário e digita "username"
        self.driver.find_element_by_id("session_password").send_keys(self.password)  # procura input de senha e digita "password"
        self.driver.find_element_by_xpath("//button[contains(text(), 'Entrar')]").click()  # efetua o login

    def scrap_user_profile(self,):
        df = pd.read_csv(r"./txts/nomes.txt")
        nome = df['nomes'].tolist()
        links = df['links'].tolist()
        def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
            """
            Call in a loop to create terminal progress bar
            @params:
                iteration   - Required  : current iteration (Int)
                total       - Required  : total iterations (Int)
                prefix      - Optional  : prefix string (Str)
                suffix      - Optional  : suffix string (Str)
                decimals    - Optional  : positive number of decimals in percent complete (Int)
                length      - Optional  : character length of bar (Int)
                fill        - Optional  : bar fill character (Str)
                printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
            """
            percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
            filledLength = int(length * iteration // total)
            bar = fill * filledLength + '-' * (length - filledLength)
            print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
            # Print New Line on Complete
            if iteration == total: 
                print()
        for i in range(len(links)):
            l = len(links)
            printProgressBar(i + 1 , l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            strlink = f"https://{links[i]}"
            self.driver.get(strlink)
            sleep(4)
            try:
                enderco = [self.driver.find_element_by_xpath('//li[@class = "t-16 t-black t-normal inline-block"]')]
                endereco = enderco[0].text
            except:
                endereco = '-'
            pgrs = pd.read_csv(r"./txts/progress.txt")
            """
            search_input = self.driver.find_element_by_xpath("/html/body/header/div/form/div/div/div/div/div[1]/div/input")
            search_input.clear()
            search_input.send_keys(nome[i])  # pesquisa o usuário por nome
            search_input.send_keys(Keys.ENTER)
            sleep(5) """
            try:
                #name = self.driver.find_elements_by_xpath('//span[@class = "name actor-name"]') 
                #name[0].click()  # Pega o primeiro da list
                #sleep(5)
                links_contato = self.driver.find_elements_by_xpath('//span[@class = "t-16 link-without-visited-state"]')
                for link_contato in links_contato:
                    if link_contato.text == "Informações de contato":
                        link_contato.click()  # Abre as informações de contato
                    else:
                        pass
                sleep(1)

                #BLOCO DE INFORMAÇÕES DE CONTATO
                if self.driver.find_element_by_xpath('//header[@class = "pv-contact-info__header t-16 t-black t-bold"]'):
                    """ #RETIRA LINK DO PERFIL

                    if self.driver.find_element_by_xpath('//section[@class = "pv-contact-info__contact-type ci-vanity-url"]'):
                        section_link = self.driver.find_element_by_xpath('//section[@class = "pv-contact-info__contact-type ci-vanity-url"]')
                        link_ln1 = section_link.find_element_by_xpath('//a[@class = "pv-contact-info__contact-link link-without-visited-state t-14"]')
                        link_ln = link_ln1.text """
        
                        
                    #RETIRA NÚMERO DO CELULAR (SE INFORMADO)
                    try:
                        if self.driver.find_element_by_xpath('//section[@class = "pv-contact-info__contact-type ci-phone"]'):
                            section_phone =  self.driver.find_element_by_xpath('//section[@class = "pv-contact-info__contact-type ci-phone"]')
                            list_find = [section_phone.find_element_by_xpath('//span[@class = "t-14 t-black t-normal"]')]
                            phone_number = list_find[0]
                            phone_number = phone_number.text
                    except:
                        phone_number = "-"

                    #RETIRA EMAIL (SE EXISTIR)

                    try:
                        section_email = self.driver.find_element_by_xpath('//section[@class = "pv-contact-info__contact-type ci-email"]')
                        html_in_section = [section_email.find_element_by_tag_name('a')]
                        email = html_in_section[0]
                        email = email.text
                    except:
                        email = '-'

                    # FECHAR CONTATO

                    self.driver.find_element_by_xpath('//button[@class = "artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view"]').click()
                    sleep(1)
                    # PEGA EXPERIÊNCIA TOP 1

                    experience_list = self.driver.find_element_by_xpath('//a[@class = "pv-top-card--experience-list-item"]')
                    experiencia = [experience_list.find_element_by_xpath('//span[@class = "text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view"]')]
                    trabalho = experiencia[0].text
                    pgrs = pgrs.append({"nome": nome[i],"linkedin" : links[i], "telefone" : phone_number, "email" : email, "trabalho" : trabalho, "endereco" : endereco}, ignore_index=True)
                    pgrs.to_csv(r"./txts/progress.txt", header=True, index=False, sep=",")

                sleep(2)
                i += 1
            except:
                print("Algum elemento ou perfil não foi encontrado... Continuando")
                pgrs = pgrs.append({"nome": nome[i], "linkedin": links[i], "telefone": "NOME", "email" : "NAO", "trabalho" :  "ENCONTRADO", "endereco" : endereco}, ignore_index=True)
                pgrs.to_csv(r"./txts/progress.txt", header=True, index=False, sep=",")
                i += 1
                
        self.driver.close()