import MacrosClasses
import pandas as pd
from datetime import datetime

df = pd.read_csv('cainpcahis.csv', dtype=str, nrows=1)

df = df.fillna('')

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
    Acesso.Digita(row['cod_cargo'])

    # JORNADA DE TRABALHO
    Acesso.Digita(row['jornada'])

    regime_juridico = row['regime_juridico']
    data_entrada = row['data_entrada']
    forma_provimento = row['forma_provimento']
    dl_entrada = row['documento_legal_entrada']
    data_vacancia = row['data_vacancia']
    forma_vacancia = row['forma_vacancia']
    dl_vacancia = row['documento_legal_vacancia']

    # Regime Juridico
    Acesso.Digita(regime_juridico)

    # Regime Juridico
    Acesso.Digita(row['indice_correcao'])
    Acesso.Tab(1)

    # Data de Entrada
    Acesso.Digita(data_entrada) 

    # Forma do Provimento
    Acesso.Digita(forma_provimento)

    # Orgao de Origem
    Acesso.Digita(row['orgao_origem'])
    Acesso.Tab(1)            

    # Documento Legal de Entrada
    Acesso.Digita(dl_entrada)

    Acesso.Tab(1)  

    # Data de Vacancia
    Acesso.Digita(data_vacancia) 

    # Forma do Vacancia
    Acesso.Digita(forma_vacancia)

    # Orgao de Destino
    Acesso.Digita(row['orgao_destino'])
    Acesso.Tab(1) 

    # Documento Legal de Vacancia
    Acesso.Digita(dl_vacancia)

    Acesso.Tab(1)

    # Servidor com Afastamento sem Remuneração
    Acesso.Digita('N')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita('x')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # Tabela do Cargo
    Acesso.Digita(row['tabela_cargo'])

    # Nível do Cargo
    Acesso.Digita(row['nivel']) 
    Acesso.Tab(1)       

    # Classe do Cargo
    Acesso.Digita(row['classe'])
    Acesso.Tab(1)

    # Referência/Padrão do Cargo
    Acesso.Digita(row['referencia_padrao']) 
    Acesso.Tab(1)          

    # Data Fim do Cargo
    Acesso.Digita(row['data_fim_cargo']) 

    # Forma de entrada
    Acesso.Digita(row['forma_entrada'])

    # Documento Legal de Entrada
    Acesso.Digita(dl_entrada)

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # UORG de Lotacao
    Acesso.Digita(row['uorg_lotacao'])

    Acesso.Tab(2)

    # UORG de Exercício
    Acesso.Digita(row['uorg_exercicio'])         

    Acesso.Tab(2)

    # Data Fim do Cargo
    Acesso.Digita(data_vacancia)

    # Forma Saída
    Acesso.Digita(row['forma_saida'])        

    # Documento Legal Vacancia
    Acesso.Digita(dl_vacancia)

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    break