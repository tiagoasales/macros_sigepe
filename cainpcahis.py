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

    data_admissao_str = row['data_admissao']
    data_admissao_str = data_admissao_str.replace('"', '')

    data_aposentadoria_str = row['data_aposentadoria']
    data_aposentadoria_str = data_aposentadoria_str.replace('"', '')

    dia = int(data_admissao_str.split("/")[0])
    mes = int(data_admissao_str.split("/")[1])
    ano = int(data_admissao_str.split("/")[2])

    data_admissao = datetime(ano, mes, dia).date()

    data_limite_ciclo_01 = datetime(1990, 12, 11).date()

    data_limite_ciclo_02 = datetime(2008, 9, 17).date()

    dia_apo = int(data_aposentadoria_str.split("/")[0])
    mes_apo = int(data_aposentadoria_str.split("/")[1])
    ano_apo = int(data_aposentadoria_str.split("/")[2])

    data_aposentadoria = datetime(ano_apo, mes_apo, dia_apo).date()

    data_limite_ciclo_03 = data_aposentadoria

    # Entra no ciclo 01 se a data de admissao for menor que a data limite
    if False and data_admissao < data_limite_ciclo_01 :
        
        # CARGO INICIAL
        Acesso.Digita(row['cargo'])

        # JORNADA DE TRABALHO
        Acesso.Digita(row['jornada'])

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

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

        # Tabela do Cargo
        Acesso.Digita('001')

        # Nível do Cargo
        Acesso.Digita(row['nivel_cargo_inicial']) 

        Acesso.Tab(1)       

        # Classe do Cargo
        Acesso.Digita('3')

        Acesso.Tab(1)

        # Referência/Padrão do Cargo
        Acesso.Digita('I') 

        Acesso.Tab(1)          

        # Data Fim do Cargo
        Acesso.Digita(data_vacancia) 

        # Forma de entrada
        Acesso.Digita(forma_provimento)

        # Documento Legal de Entrada
        Acesso.Digita(dl_entrada)

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

        # UORG de Lotacao
        Acesso.Digita('3')

        Acesso.Tab(2)

        # UORG de Exercício
        Acesso.Digita('3')         

        Acesso.Tab(2)

        # Data Fim do Cargo
        Acesso.Digita(data_vacancia)

        # Forma Saída
        Acesso.Digita(forma_vacancia)        

        # Documento Legal Vacancia
        Acesso.Digita(dl_vacancia)

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    if False and data_admissao < data_limite_ciclo_02 and data_aposentadoria > data_limite_ciclo_01:

        # CARGO INICIAL
        Acesso.Digita(row['cargo'])

        # JORNADA DE TRABALHO
        Acesso.Digita(row['jornada'])

        regime_juridico = '02'
        data_entrada = '12DEZ1990'
        forma_provimento = '534'
        dl_entrada = 'LEI 8112/90'
        data_vacancia = '17SET2008'
        forma_vacancia = '534'
        dl_vacancia = 'LEI 11776/2008'

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

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

        # Tabela do Cargo
        Acesso.Digita('001')

        # Nível do Cargo
        Acesso.Digita(row['nivel_cargo_inicial']) 

        Acesso.Tab(1)       

        # Classe do Cargo
        Acesso.Digita(row['classe_cargo_intermediario'])

        Acesso.Tab(1)

        # Referência/Padrão do Cargo
        Acesso.Digita(row['padrao_cargo_intermediario']) 

        Acesso.Tab(1)          

        # Data Fim do Cargo
        Acesso.Digita(data_vacancia) 

        # Forma de entrada
        Acesso.Digita(forma_provimento)

        # Documento Legal de Entrada
        Acesso.Digita(dl_entrada)

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

        # UORG de Lotacao
        Acesso.Digita('3')

        Acesso.Tab(2)

        # UORG de Exercício
        Acesso.Digita('3')         

        Acesso.Tab(2)

        # Data Fim do Cargo
        Acesso.Digita(data_vacancia)

        # Forma Saída
        Acesso.Digita(forma_vacancia)        

        # Documento Legal Vacancia
        Acesso.Digita(dl_vacancia)

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')  

    if data_aposentadoria > data_limite_ciclo_02 :

        # CARGO INICIAL
        Acesso.Digita(row['cargo_final'])

        # JORNADA DE TRABALHO
        Acesso.Digita(row['jornada'])

        regime_juridico = '02'
        data_entrada = '18SET2008'
        forma_provimento = '534'
        dl_entrada = 'LEI 11776/08'
        data_vacancia = row['data_aposentadoria_siape']
        forma_vacancia = '043'
        dl_vacancia = row['portaria_aposentadoria']

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

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

        # Tabela do Cargo
        Acesso.Digita('001')

        # Nível do Cargo
        Acesso.Digita(row['nivel_cargo']) 

        Acesso.Tab(1)       

        # Classe do Cargo
        Acesso.Digita(row['classe_cargo_final'])

        Acesso.Tab(1)

        # Referência/Padrão do Cargo
        Acesso.Digita(row['padrao_cargo_final']) 

        Acesso.Tab(1)          

        # Data Fim do Cargo
        Acesso.Digita(data_vacancia) 

        # Forma de entrada
        Acesso.Digita(forma_provimento)

        # Documento Legal de Entrada
        Acesso.Digita(dl_entrada)

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')

        # UORG de Lotacao
        Acesso.Digita('3')

        Acesso.Tab(2)

        # UORG de Exercício
        Acesso.Digita('3')         

        Acesso.Tab(2)

        # Data Fim do Cargo
        Acesso.Digita(data_vacancia)

        # Forma Saída
        Acesso.Digita(forma_vacancia)        

        # Documento Legal Vacancia
        Acesso.Digita(dl_vacancia)

        Tela = Acesso.ViraTelaSiafiTecla('ENTER')  

    break