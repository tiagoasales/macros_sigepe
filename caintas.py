import pyautogui as robo
import time
import pandas as pd
import pyperclip

robo.PAUSE = 0.5

df = pd.read_csv('./input/caintas.csv', dtype=str, nrows=1)

# troca todos os valores NaN por vazio
df = df.fillna('')

matricula = df.iloc[0]['matricula']

#robo.press("winleft")
#robo.write("chrome")
#robo.press("enter")
#robo.write("https://esiape.sigepe.gov.br/")
#robo.press("enter")

robo.hotkey('alt', 'tab')
# robo.write('CAINTAS', interval=0.1)
# robo.press('enter')
# time.sleep(0.5)
robo.press('backspace', presses=8)
robo.write(matricula, interval=0.1)
robo.press('enter')
time.sleep(1)

for index, row in df.iterrows():

    # inicio do Período Trabalhado
    robo.write(row['data_inicio'], interval=0.1)
    robo.press('tab')

    # fim do Período Trabalhado
    robo.write(row['data_fim'], interval=0.1)
    robo.press('tab')

    # código do órgão / nome empresa
    robo.write(row['cod_empregador'])
    robo.press('tab')

    # preenche o nome da empresa, se existir
    if len(row['nome_empresa']) > 1:
        robo.press('tab')
        robo.write(row['nome_empresa'])
        robo.press('tab')

    # seleciona na combo o tipo de averbação bruta
    robo.press('down')
    robo.press('tab')

    # preenche o campo observaçoes usando ctrl + c ctrl + v
    # porque o PyAutoGui não tem suporte a UTF-8
    pyperclip.copy('Conforme Certidão de Tempo de Serviço')
    robo.hotkey("ctrl", "v")
    robo.press('tab', presses=5)
    robo.press('enter')

    # a tela seguinte não inicia no primeiro campo
    # por isso é dado um tab após o carregamento da pagina
    time.sleep(1)
    robo.press('tab')

    # seleciona a Natureza Jurídica
    time.sleep(1)
    robo.write(row['cod_natureza_juridica'], interval=0.15)
    robo.press('tab')
    time.sleep(1)
    robo.press('tab')

    # seleciona o Regime Juridico
    time.sleep(0.2)
    robo.write(row['cod_regime_juridico'], interval=0.25)
    robo.press('tab')
    time.sleep(1)
    robo.press('tab', presses=2, interval=0.25)

    # seleciona a Atividade Externa
    time.sleep(1)
    robo.write(row['cod_atividade_externa'], interval=0.25)
    robo.press('tab')

    # seleciona Regime Previdênciario
    # esse campo só aparece quando não é militar
    if row['cod_regime_previdenciario'] != "3":
        # tive que usar click do mouse pq tab num tava indo
        time.sleep(0.2)
        robo.moveTo(1810, 745, duration = 0.25)
        robo.leftClick()
        robo.write(row['cod_regime_previdenciario'], interval=0.25)
        time.sleep(0.15)
        robo.typewrite('enter')
        robo.moveTo(1810, 745, duration = 0.1)
        robo.leftClick()

#    if row['cargo_efetivo'] == "S" or row['cargo_efetivo'] == "N":
#        time.sleep(0.2)
#        robo.moveTo(1435, 812, duration = 0.25)
#        robo.leftClick()
#        
#        if row['cargo_efetivo'] == 'S':
#            robo.press('down')
#        else:
#            robo.press('down', presses=2) 
#        
#        robo.typewrite('enter')
#        
#        robo.moveTo(1435, 812, duration = 0.1)
#        robo.leftClick()        

    if row['nit'] != '':
        print('entrou nit')
        time.sleep(0.2)
        robo.moveTo(1548, 812, duration = 0.25)
        robo.leftClick()
        
        robo.write(row['nit'], interval=0.15)
        time.sleep(0.15)

    # informa o numero do processo
    time.sleep(0.2)
    robo.moveTo(1205, 817, duration = 0.25)
    robo.leftClick()
    robo.write(row['numero_processo'])

    if row['uf'] != '':
        time.sleep(0.2)
        robo.moveTo(1435, 880, duration = 0.25)
        robo.leftClick()
        
        robo.write(row['uf'], interval=0.15)
        time.sleep(0.15)
        robo.press('enter')

    robo.press('enter')
    
    # time.sleep(2)
    # robo.press('enter')

