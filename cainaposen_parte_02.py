import MacrosClasses
import pandas as pd

df = pd.read_csv('cainaposen_b_04.csv', dtype=str, nrows=1)

df = df.fillna(' ')

Acesso = MacrosClasses.janela3270("Terminal 3270 - A - AWVAKJR7")

for index, row in df.iterrows():

    Acesso.Tab(9)

    Acesso.Digita('>cainaposen')

    Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita(row['cpf'])

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # Fudamento Legal
    Acesso.Digita(row['fundamento_legal'])


    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # Inicio da Aposentadoria
    Acesso.Digita(row['inicio_aposentadoria'])

    # Inicio do ultimo Provento -> colocar a data do cargo da pessoa
    Acesso.Digita(row['inicio_aposentadoria'])


    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    #Acesso.Digita('X')

    retorno = Acesso.PegaTextoSiafi(Tela, 10, 68, 10, 77)
    if (retorno.strip() == 'CERRADAS'):
        print('As matriculas existentes nao podem ser utilizadas no momento. Para dar nova matricula para o servidor, contate o gestor do sistema')
        break

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # CODIGO DO CARGO DO APOSENTADO
    # 617001 - OFICIAL DE INTELIGENCIA
    # 617002 - AGENTE DE INTELIGENCIA
    Acesso.Digita(row['cargo'])

    # JORNADA DE TRABALHO (valor padrão)
    Acesso.Digita('40')

    # SENTENCA JUDICIAL (valor padrão)
    Acesso.Digita('N')

    # NUMERADOR PROPORCIONALIDADE
    Acesso.Digita(row['numerador'])

    # DENOMINADOR PROPORCIONALIDADE
    Acesso.Digita(row['denominador'])

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # NIVEL DA CARREIRA
    Acesso.Digita(row['nivel'])
    Acesso.Tab(1)

    # CLASSE DA CARREIRA
    Acesso.Digita(row['classe'])
    Acesso.Tab(1)

    # PADRAO DA CARREIRA
    Acesso.Digita(row['padrao'])
    Acesso.Tab(1)

    # ANUENIO
    Acesso.Digita(row['anuenio'])
    #Acesso.Digita(17)

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')
    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # CODIGO DO ORGAO
    # 20114 = ABIN
    Acesso.Digita('20114')

    # A UORG 001 VAI SER A UNIDADE DOS APOSENTADOS NO SIGEPE
    Acesso.Digita('001')
    Acesso.Tab(2)

    # NUMERO DO PROCESSO DE APOSENTADORIA
    Acesso.Digita(row['processo'])

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')
    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')
    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # TEXTO COM OS DADOS DA PORTARIA DE APOSENTADORIA
    Acesso.Digita(row['documento_legal'])

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # PERGUNTA DE CONFIRMACAO
    Acesso.Digita('S')

    #Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    break