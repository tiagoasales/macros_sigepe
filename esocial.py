from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import traceback

# Configurações para se conectar ao navegador já aberto
chrome_options = Options()
chrome_options.debugger_address = "127.0.0.1:9222"  # Porta do Chrome iniciado com debugging

# Cria a instância do driver conectando ao navegador aberto
driver = webdriver.Chrome(options=chrome_options)

# Espera a página carregar
time.sleep(2)


df = pd.read_csv('./input/beneficios_08.csv', dtype=str) 

print("-----------------------------------------------------------------------------")

cpf = df.iloc[0]['CPF']
nome = df.iloc[0]['NOME']

print(cpf, ' - ',nome)

for index, row in df.iterrows():

    try:

        if cpf != row['CPF']:
            print("QTD DE RUBRICAS:", index)
            break

        btnRubrica = driver.find_element(By.ID,'controle-incluir-rubrica')
        btnRubrica.send_keys(Keys.ENTER)
        time.sleep(0.2)

        comboBeneficio = driver.find_element(By.ID,'EventoAcessorio_NumeroBeneficio')
        select = Select(comboBeneficio)
        select.select_by_index(1)
        time.sleep(0.2)

        txtCNPJ = driver.find_element(By.ID,'EventoAcessorio_DemonstrativosValoresDevidos_0__InformacaoPeriodoApuracao_ListaIdeEstabelecimentoLotacao_0__NumeroInscricao')
        txtCNPJ.send_keys('01.175.497/0001-41')
        txtCNPJ.send_keys(Keys.TAB)
        time.sleep(0.2)

        txtTabela = driver.find_element(By.ID,'RubricaAcessoria_Rubrica_IdeTabelaRubrica')
        txtTabela.clear()
        txtTabela.send_keys(row['TIPO'])
        time.sleep(0.2)

        txtRubrica = driver.find_element(By.ID,'RubricaAcessoria_Rubrica_CodigoRubrica')
        txtRubrica.send_keys(row['RUB_SIGEPE'])
        txtRubrica.send_keys(Keys.TAB)
        time.sleep(0.2)

        txtValor = driver.find_element(By.ID,'RubricaAcessoria_Rubrica_ValorRubrica')
        txtValor.send_keys(row['VALOR'])
        time.sleep(0.2)

        comboIndicativo = driver.find_element(By.ID,'RubricaAcessoria_Rubrica_IndicativoApuracaoIR')
        select = Select(comboIndicativo)
        select.select_by_value("0")
        time.sleep(0.2)

        btnIncluirRubrica = driver.find_element(By.ID,'incluir-rubrica')
        btnIncluirRubrica.send_keys(Keys.ENTER)
        time.sleep(1.5)

    except Exception as e:
        traceback.print_exc()

print("RUBRICAS INSERIDAS COM SUCESSO!!!")
print("-----------------------------------------------------------------------------")