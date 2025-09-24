import MacrosClasses
import pandas as pd

import time

df = pd.read_csv('./input/13145010115.csv', dtype=str)
df = df.fillna(' ')

Acesso = MacrosClasses.janela3270("Terminal 3270 - A - AWVAKJR7")

# AQUI EH QUE REALMENTE COMEÇA O LANÇAMENTO DO PSS
anos = df['ANO'].unique()
constante = 7
ultimo_ano = int(anos[-1])

contador = 1

for ano in anos:

    print('Começando o ano de ', ano)

    df_ano = df.loc[df['ANO'] == ano]

    Acesso.Digita(ano)
    Acesso.ViraTelaSiafiTecla('ENTER')

    meses = df_ano['MES'].unique()

    if int(ano) == 1994:
        mes_anterior = 7
    else:        
        mes_anterior = 1

    primeira_rodada = True

    # Laço para selecionar os meses que possuem contribuição
    for index, row in df_ano.iterrows():
        mes = int(row['MES'])
        
        if primeira_rodada:
            pulos = mes - (mes_anterior)
            primeira_rodada = False
        else:
            pulos = mes - (mes_anterior + 1)

        if int(ano) != 1998 and pulos > 0 :
            Acesso.Tab(pulos)

        if mes in (1,2,3,4,5,6,7,8,9,10,11):
            Acesso.Digita("X")
        else:
            Acesso.Digita("X")
            Acesso.Digita("X")            

        mes_anterior =  int(row['MES'])

    Acesso.ViraTelaSiafiTecla('ENTER')
        
    # pop-up para assinalar a opção de informar o PSS
    Acesso.Tab(1)
    Acesso.Digita("X")
    Acesso.ViraTelaSiafiTecla('ENTER')

    # interação que informa os valores mês a mês
    for index, row in df_ano.iterrows():
        Acesso.Digita('1')
        Acesso.Digita(row['VALOR'])
        Acesso.Tab(1)
            
        if int(row['MES']) == 12:
            Acesso.Digita('1')
            Acesso.Digita(row['VALOR'])
            Acesso.Tab(1)
    
    Acesso.ViraTelaSiafiTecla('ENTER')
    Acesso.Digita("C")
    Acesso.ViraTelaSiafiTecla('ENTER')
    Acesso.ViraTelaSiafiTecla('ENTER')
