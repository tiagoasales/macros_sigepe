import MacrosClasses
import pandas as pd
from datetime import datetime

df = pd.read_csv('cainpcahis.csv', dtype=str, nrows=1)

df = df.fillna(' ')

Acesso = MacrosClasses.janela3270("Terminal 3270 - A - AWVAKJR7")

for index, row in df.iterrows():

    Acesso.Tab(9)

    Acesso.Digita('>cainpcahis')

    Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Tab(1)

    # CPF do APOSENTADO
    Acesso.Digita(row['cpf'])

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # CARGO INICIAL
    Acesso.Digita(row['cargo'])

    # JORNADA DE TRABALHO
    Acesso.Digita(row['jornada'])

    data_admissao_str = row['data_admissao']
    data_admissao_str = data_admissao_str.replace('"', '')

    dia = int(data_admissao_str.split("/")[0])
    mes = int(data_admissao_str.split("/")[1])
    ano = int(data_admissao_str.split("/")[2])

    data_admissao = datetime(ano, mes, dia).date()
    data_limite_ciclo_01 = datetime(1990, 12, 11).date()

    # Entra no ciclo 01 se a data de admissao for menor que a data limite
    if data_admissao < data_limite_ciclo_01 :
        
        regime_juridico = '01'
        data_entrada = row['data_admissao_siape']
        forma_provimento = '501'
        dl_entrada = 'CONTRATO INDIVIDUAL DE TRABALHO'
        data_vacancia = '11DEZ1990'
        forma_vacancia = '534'
        dl_vacancia = 'LEI 8112/90'

        # Regime Juridico
        Acesso.Digita(regime_juridico)
        
        Acesso.Tab(1)

        # Data de Entrada
        Acesso.Digita(data_entrada) 

        # Forma do Provimento
        Acesso.Digita(forma_provimento)

        Acesso.Tab(1)            

        # Documento Legal de Entrada
        Acesso.Digita(dl_entrada)

        Acesso.Tab(1)  

        # Data de Vacancia
        Acesso.Digita(data_vacancia) 

        # Forma do Vacancia
        Acesso.Digita(forma_vacancia)

        Acesso.Tab(1)

        # Documento Legal de Vacancia
        Acesso.Digita(dl_vacancia)

        Acesso.Tab(1)

        # Servidor com Afastamento sem Remuneração
        Acesso.Digita('N')

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    break