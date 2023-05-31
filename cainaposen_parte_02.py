import MacrosClasses
import pandas as pd

df = pd.read_csv('aposentados_02.csv', dtype=str)

df = df.fillna(' ')

Acesso = MacrosClasses.janela3270("Terminal 3270 - A - AWVAKJR7")

for index, row in df.iterrows():

    Acesso.Tab(9)

    Acesso.Digita('>cainaposen')

    Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita('02256622720')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # Fudamento Legal
    Acesso.Digita('500115')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # Inicio da Aposentadoria
    Acesso.Digita('24NOV1994')

    # Inicio do ultimo Provento -> colocar a data do cargo da pessoa
    Acesso.Digita('18SET2008')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita('617001')

    Acesso.Digita('40')

    Acesso.Digita('N')

    Acesso.Digita('030')

    Acesso.Digita('035')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita('NS')
    Acesso.Tab(1)

    Acesso.Digita('S')
    Acesso.Tab(1)

    Acesso.Digita('I')
    Acesso.Tab(1)

    Acesso.Digita('0')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')
    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita('20114')

    # A UORG 001 VAI SER A UNIDADE DOS APOSENTADOS NO SIGEPE
    Acesso.Digita('001')
    Acesso.Tab(2)

    Acesso.Digita('01180010168/1993-0')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')
    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')
    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita('PORT 92/1994 ABIN, DE 24/11/1994, DOU 227 DE 01/12/1994')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita('S')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    break