# LinkedinContactBot

Descrição: Script de coleta de dados automatizado, via Linkedin, baseado em um banco de dados, que retorna uma tabela com informações atuais sinalizando possíveis diferenças.

Passo a passo:

 1) Instalação do chromedriver ou algum driver de sua preferência:
      Link do chromedriver: https://chromedriver.chromium.org/downloads  // NOTA: baixar versão condizente ao do navegador instalado.
      Adcionar no script em linkedinclass.py Linha 11 em self.driver = webdriver.Chrome(r"PATH DO EXECUTÁVEL")

2) Download da credentials.json:
      https://developers.google.com/sheets/api/quickstart/python Fazer o primeiro passo descrito STEP 1 (Passo 1)
      1 - Enable the Google Sheets API (clicar)
      2 - Coloque o nome do projeto (não interfere) - Next
      3 - Desktop App - Create
      4 - Arrastar o arquivo baixado para a pasta scripts do projeto.

3) Instale os requirements (bibliotecas):
      Entre no terminal de preferêcia e execute o comando:
          pip install -r requirements.txt
          (caso deseje criar uma venv pro projeto RECOMENDADO, crie a venv ative-a e execute o comando)

4) Entre na tabela salva no googledrive como referência e copie o ID exemplo: 
      https://docs.google.com/spreadsheets/d/1Xe1xgAKAL5YdQ7rxpP8mcC_rz3dhtOZAkFDJQAmqQBQ/edit#gid=0
      id = 1Xe1xgAKAL5YdQ7rxpP8mcC_rz3dhtOZAkFDJQAmqQBQ
      cole o id em sheetsapi.py na linha 85 e execute esse script
      Caso tudo ocorra devidamente, erros podem aparecer já que a tabela não estava igual ou parecida com a de exemplo.
      EXEPLO: https://docs.google.com/spreadsheets/d/1Xe1xgAKAL5YdQ7rxpP8mcC_rz3dhtOZAkFDJQAmqQBQ/edit#gid=0
   
5) Copie o ID na main.py na linha 10 e execute a main.py
      Inicie a coleta por -s ou --start, após isso crie uma tabela com -t ou --tabela

NOTAS:
      Após a coleta de nomes eles serão preenchidos na nomes.txt, após o start caso queira remover nomes antes de inserir as informações de login,
      remova as linhas completas no txt. Ao longo do tempo as informações serão armazenadas na progress.txt, que será a base para a criação da tabela
      pelo comando -t ou --tabela. Ao longo do código existem alguns times.sleep que server para esperar algumas páginas carregarem, adeque-os para a velocidade
      da internet conectada (já estao com uma boa margem de tempo) - Suas localizações: linkedinclass.py linha 13, 15 e 52, os das linhas 75 e 110 nao precisam
      ser alterados.
    
