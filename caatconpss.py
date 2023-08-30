import pyautogui as robo
import time
import pandas as pd

robo.PAUSE = 0.5

df = pd.read_csv('29801516100.csv', dtype=str)

cpf = df.iloc[0]['CPF']

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
robo.write(cpf)
robo.press('enter')
time.sleep(1)

anos = df['ANO'].unique()
constante = 7
ultimo_ano = int(anos[-1])

contador = 1

for ano in anos:

    print('Começando o ano de ', ano)

    df_ano = df.loc[df['ANO'] == ano]

    time.sleep(1)
    robo.write(ano)
    robo.press('enter')
    time.sleep(1)

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
            robo.press('down', presses=pulos) 

        if mes in (1,2,3,4,5,6,7,8,9,10,11):
            robo.press('space')
            robo.press('down')
        else:
            robo.press('space')
            robo.press('down')
            robo.press('space')

        mes_anterior =  int(row['MES'])

    robo.press('enter')
    time.sleep(1)
        
    robo.press('down')
    time.sleep(2)

    for index, row in df_ano.iterrows():
        robo.write('1')
        robo.write(row['VALOR'])
        robo.press('tab', presses=2)
            
        if int(row['MES']) == 12:
            robo.write('1')
            robo.write(row['VALOR'])
            robo.press('tab', presses=3) 

    # Se tiver faltando meses e o último mês não for dezembro, tem que dar um tab a mais
    if len(meses) < 12 and int(meses[-1]) != 12:
        robo.press('tab')

    robo.press('enter')
    time.sleep(1)

    robo.press('enter')
    time.sleep(1)

    robo.press('enter')
    time.sleep(1)    

    robo.press('backspace', presses=4)

    contador += 1

    if contador == 4:
        contador = 0
        robo.moveTo(2260, 121, duration = 0.5)
        robo.leftClick()
        robo.moveTo(2300, 114, duration = 0.5)
        robo.leftClick()
        robo.write('CAATCONPSS')
        robo.press('enter')
        time.sleep(0.5)
        robo.press('tab', presses=3)
        robo.write(cpf)
        robo.press('enter')
        time.sleep(1)        

 