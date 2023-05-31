import MacrosClasses
import pandas as pd

df = pd.read_csv('aposentados_02.csv', dtype=str)

df = df.fillna(' ')

Acesso = MacrosClasses.janela3270("Terminal 3270 - A - AWVAKJR7")

for index, row in df.iterrows():

    Acesso.Tab(9)

    Acesso.Digita('>caatdadsia')

    Acesso.ViraTelaSiafiTecla('ENTER')

    # MATRICULA SIAPECAD
    Acesso.Digita('02432499')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # DATA DE INGRESSO NO ORGAO
    Acesso.Digita('15DEZ1975')

    # OCORRENCIA DE ADMISSAO
    # 01001 - ADMISSAO POR CONCURSO PUBLICO
    # 01003 - ADMISSAO SEM CONCURSO PUBLICO
    Acesso.Digita('01003')

    # TIPO DO DIPLOMA LEGAL
    # 04 - PORTARIA
    Acesso.Digita('04')

    # NUMERO DA PORTARIA
    Acesso.Digita('252') 
    Acesso.Tab(1)   

    # DATA DA PORTARIA -> COLOCAR A MESMA DE INGRESSO NO ORGAO, POIS TEM APOSENTADO QUE ENTROU ANTES DA PORTARIA
    Acesso.Digita('15DEZ1975')

    # DATA INGRESSO NO SERVICO PUBLICO -> VAMOS COLOCAR A MESMA DO ORGAO
    Acesso.Digita('15DEZ1975')

    # OCORRENCIA DE ADMISSAO DE INGRESSO NO SERVICO PUBLICO
    # 01001 - ADMISSAO POR CONCURSO PUBLICO
    # 01003 - ADMISSAO SEM CONCURSO PUBLICO
    Acesso.Digita('01003')

    # TIPO DO DIPLOMA LEGAL
    # 04 - PORTARIA
    Acesso.Digita('04')

    # NUMERO DA PORTARIA DE INGRESSO NO SERVICO PUBLICO
    Acesso.Digita('252') 
    Acesso.Tab(1)   

    # DATA DA PORTARIA DE INGRESSO NO SERVICO PUBLICO
    Acesso.Digita('15DEZ1975')

    #Tela = Acesso.ViraTelaSiafiTecla('ENTER')
    Acesso.Enter()
    Acesso.Enter()
    Acesso.Enter()

    # CONFIRMACAO
    Acesso.Digita('S')

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    break