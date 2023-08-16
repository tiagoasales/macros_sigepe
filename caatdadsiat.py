import MacrosClasses
import pandas as pd

df = pd.read_csv('caatdadsia_mar.csv', dtype=str, nrows=1)

df = df.fillna(' ')

Acesso = MacrosClasses.janela3270("Terminal 3270 - A - AWVAKJR7")

for index, row in df.iterrows():

    Acesso.Tab(9)

    Acesso.Digita('>caatdadsia')

    Acesso.ViraTelaSiafiTecla('ENTER')

    # MATRICULA SIAPECAD
    Acesso.Digita(row['matricula_siapecad'])

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # DATA DE INGRESSO NO ORGAO
    Acesso.Digita(row['adminissao'])

    # OCORRENCIA DE ADMISSAO
    # 01001 - ADMISSAO POR CONCURSO PUBLICO
    # 01003 - ADMISSAO SEM CONCURSO PUBLICO
    Acesso.Digita(row['ocorrencia_admissao'])

    # TIPO DO DIPLOMA LEGAL
    # 04 - PORTARIA
    Acesso.Digita(row['diploma_legal'])

    # NUMERO DA PORTARIA
    Acesso.Digita(row['numero_portaria']) 
    Acesso.Tab(1)   

    # DATA DA PORTARIA -> COLOCAR A MESMA DE INGRESSO NO ORGAO, POIS TEM APOSENTADO QUE ENTROU ANTES DA PORTARIA
    Acesso.Digita(row['adminissao'])

    # DATA INGRESSO NO SERVICO PUBLICO -> VAMOS COLOCAR A MESMA DO ORGAO
    Acesso.Digita(row['ingresso_publico'])

    # OCORRENCIA DE ADMISSAO DE INGRESSO NO SERVICO PUBLICO
    # 01001 - ADMISSAO POR CONCURSO PUBLICO
    # 01003 - ADMISSAO SEM CONCURSO PUBLICO
    Acesso.Digita(row['ocorrencia_admissao'])

    # TIPO DO DIPLOMA LEGAL
    # 04 - PORTARIA
    Acesso.Digita(row['diploma_legal'])

    # NUMERO DA PORTARIA DE INGRESSO NO SERVICO PUBLICO
    Acesso.Digita(row['numero_portaria']) 
    Acesso.Tab(1)   

    # DATA DA PORTARIA DE INGRESSO NO SERVICO PUBLICO
    Acesso.Digita(row['ingresso_publico'])

    #Tela = Acesso.ViraTelaSiafiTecla('ENTER')
    Acesso.Enter()
    Acesso.Enter()
    Acesso.Enter()

    # CONFIRMACAO
    Acesso.Digita('S')

    #Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    break