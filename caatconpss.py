import pyautogui as robo
import time
import pandas as pd

robo.PAUSE = 0.5

df = pd.read_csv('./input/22238344004.csv', dtype=str)

cpf = df.iloc[0]['CPF']

robo.hotkey('alt', 'tab')

anos = df['ANO'].unique()
constante = 7
ultimo_ano = int(anos[-1])

contador = 1

for ano in anos:

    print('Começando o ano de ', ano)

    df_ano = df.loc[df['ANO'] == ano]

    time.sleep(1)
    robo.write(ano)
    time.sleep(0.5)
    robo.press('enter')
    time.sleep(3)

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

        if pulos > 0:
            robo.press('down', presses=pulos, interval=0.2) 

        if mes in (1,2,3,4,5,6,7,8,9,10,11):
            robo.press('space', interval=0.1)
            robo.press('down', interval=0.1)
        else:
            robo.press('space', interval=0.1)
            robo.press('down', interval=0.1)
            robo.press('space', interval=0.1)

        mes_anterior =  int(row['MES'])

    time.sleep(4)

    robo.press('enter')
    time.sleep(4)
        
    robo.press('down')
    time.sleep(4)

    for index, row in df_ano.iterrows():
        time.sleep(0.5)
        robo.write('1')
        robo.write(row['VALOR'])
        robo.press('tab', presses=2, interval=0.2)
            
        if int(row['MES']) == 12:
            robo.write('1')
            robo.write(row['VALOR'])
            robo.press('tab', presses=3, interval=0.2)

    # Se tiver faltando meses e o último mês não for dezembro, tem que dar um tab a mais
    if len(meses) < 12 and int(meses[-1]) != 12:
        robo.press('tab')

    robo.press('enter')
    time.sleep(3)

    robo.press('enter')
    time.sleep(3)

    robo.press('enter')
    time.sleep(3)

    robo.press('esc')
    time.sleep(5)

    robo.press('backspace', presses=4, interval=0.4)
