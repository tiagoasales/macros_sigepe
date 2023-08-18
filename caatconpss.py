import pyautogui as robo
import time
import pandas as pd

robo.PAUSE = 0.5


#robo.press("winleft")
#robo.write("chrome")
#robo.press("enter")
#robo.write("https://esiape.sigepe.gov.br/")
#robo.press("enter")

robo.hotkey('alt', 'tab')
robo.write('CAATCONPSS')
robo.press('enter')
time.sleep(0.5)
robo.press('tab', presses=3)
robo.write('34967222749')
robo.press('enter')
time.sleep(1)

df = pd.read_csv('contribuicoes.csv', dtype=str)

#mes_inicio = int(df.iloc[0]['mes'])
#ano_inicio = int(df.iloc[0]['ano'])

anos = df['ano'].unique()
constante = 7
ultimo_ano = int(anos[-1])

for ano in anos:

    print('Começando o ano de ', ano)

    df_ano = df.loc[df['ano'] == ano]

    robo.write(ano)
    robo.press('enter')
    time.sleep(1)

    mes = 0

    if int(ano) == 1994:
        mes_anterior = 7
    else:        
        mes_anterior = 1

    primeira_rodada = True

    # Laço para selecionar os meses que possuem contribuição
    for index, row in df_ano.iterrows():
        mes = int(row['mes'])
        
        if primeira_rodada:
            pulos = mes - (mes_anterior)
            primeira_rodada = False
        else:
            pulos = mes - (mes_anterior + 1)

        if pulos > 0:
            robo.press('down', presses=pulos) 

        if mes in (1,2,3,4,5,6,7,8,9,10,11):
            robo.press('space')
            robo.press('down')
        else:
            robo.press('space')
            robo.press('down')
            robo.press('space')

        mes_anterior =  int(row['mes'])

    robo.press('enter')
    time.sleep(1)
        
    robo.press('down')
    time.sleep(2)

    for index, row in df_ano.iterrows():
        mes = int(row['mes'])


        robo.write('1')
        robo.write(row['valor'])
        robo.press('tab', presses=2)
            
        if int(row['mes']) == 12:
            robo.write('1')
            robo.write(row['valor'])
            robo.press('tab', presses=3) 

    if int(ano) == ultimo_ano and mes != 12:
        robo.press('tab')

    robo.press('enter')
    time.sleep(1)

    robo.press('enter')
    time.sleep(1)

    robo.press('enter')
    time.sleep(1)    

    robo.press('backspace', presses=4)

 