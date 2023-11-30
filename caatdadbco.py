import pyautogui as robo
import time
import pandas as pd

robo.PAUSE = 0.5

df = pd.read_csv('caatdadbco.csv', dtype=str)

robo.hotkey('alt', 'tab')

for index, row in df.iterrows():

    print('-------------------------------')
    print('Iniciando: ', row['nome'])

    robo.write(row['cpf'])
    robo.press('enter')
    time.sleep(1)

    robo.moveTo(1730, 480, duration = 0.5)
    robo.leftClick()

    time.sleep(1)
    robo.typewrite('04', interval=0.25)
    robo.typewrite('enter')
    robo.press('tab')

    time.sleep(1)
    robo.typewrite(row['id_banco'], interval=0.2)
    robo.typewrite('enter')
    robo.press('tab')

    time.sleep(1)
    agencia = row['agencia_banco'].split('-')[0]
    robo.typewrite(agencia)
    robo.press('tab')

    digito = row['agencia_banco'].split('-')[1]
    robo.typewrite(digito)
    robo.press('tab')

    robo.typewrite(row['conta_corrente'])
    robo.press('tab')

    robo.press('tab', presses=3)

    robo.typewrite('01', interval=0.15)
    robo.typewrite('enter')
    robo.press('tab')

    robo.typewrite(row['id_banco'], interval=0.2)
    robo.typewrite('enter')
    robo.press('tab')

    agencia = row['agencia_banco'].split('-')[0]
    robo.typewrite(agencia)
    robo.press('tab')

    digito = row['agencia_banco'].split('-')[1]
    robo.typewrite(digito)
    robo.press('tab')

    robo.typewrite(row['conta_corrente'])
    robo.press('tab')

    robo.press('tab', presses=2, interval=0.15)
    time.sleep(1)
    robo.press('enter')

    time.sleep(2)
    robo.moveTo(1795, 617, duration = 0.5)
    robo.leftClick()

    time.sleep(2)
    robo.press('enter')

    time.sleep(2)
    robo.press('enter')

    time.sleep(1)
    robo.press('backspace', presses=11)

    print('finalizado com sucesso!')