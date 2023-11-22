import pyautogui as robo
import time
import pandas as pd

robo.PAUSE = 0.5

df = pd.read_csv('caatdadbco.csv', dtype=str, nrows=1)

cpf = df.iloc[0]['cpf']

#robo.press("winleft")
#robo.write("chrome")
#robo.press("enter")
#robo.write("https://esiape.sigepe.gov.br/")
#robo.press("enter")

robo.hotkey('alt', 'tab')
# robo.write('CAATDADBCO')
# robo.press('enter')
# time.sleep(0.5)
robo.write(cpf)
robo.press('enter')
time.sleep(1)

robo.moveTo(1730, 480, duration = 0.5)
robo.leftClick()

for index, row in df.iterrows():

    # apenas pra inicializar a combo inicial (sem isso não dá certo)
    time.sleep(1)
    robo.typewrite('01')

    time.sleep(1)
    robo.typewrite('04')
    robo.typewrite('enter')
    robo.press('tab')

    robo.typewrite(row['id_banco'])
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

    robo.press('tab', presses=3)

    robo.typewrite('01')
    robo.typewrite('enter')
    robo.press('tab')

    robo.typewrite(row['id_banco'])
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

    robo.press('tab', presses=2)
    time.sleep(1)
    robo.press('enter')

    time.sleep(1)
    robo.moveTo(1795, 617, duration = 0.5)
    robo.leftClick()

    time.sleep(1)
    robo.press('enter')

    time.sleep(1)
    robo.press('enter')

    time.sleep(1)
    robo.press('backspace', presses=11)