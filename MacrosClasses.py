# Video sobre PyAutoGui: https://www.youtube.com/watch?v=MeOUl7ZjJRM

# PARA MAC EXCLUIR ESSAS LINHAS
# (EXCLUIR AS DE WINDOWS)

from pywinauto.application import Application
from pywinauto import keyboard
from pywinauto import mouse
from pywinauto import clipboard
import pywinauto.keyboard as tc

import sqlite3

import time

##############################################
#              JANELA INTERNET               #
##############################################
class janelaInternet:

  def __init__(self, TituloJanela):
    global app, dlg, ListaTeclasComando, ListaDigitaTeclasComando
    self.Tela = ''
    ListaTeclasComando       = ('ENTER'  ,     'ESC'   ,     'HOME',    'END' ,    'UP',    'DOWN')
    ListaDigitaTeclasComando = ('{ENTER}','{VK_ESCAPE}','{VK_HOME}','{VK_END}','{VK_UP}','{VK_DOWN}')
    app = Application().connect(title=TituloJanela)
    dlg = app.top_window()

  def SelecionaJanela(self):
    global app, dlg
    dlg = app.top_window()
    time.sleep(1)

  def SalvaTelaArqTexto(self,Arquivo):
    global app, dlg
    dlg.type_keys('^S')
    time.sleep(1) 
    tc.send_keys(Arquivo)
    time.sleep(1)
    tc.send_keys('{ENTER}')

  def VaiParaBarraDeEndereco(self):
    global dlg
    dlg.type_keys('{F6}') #vai para a barra de endereco
    time.sleep(1)

  def EnderecoWeb(self,Endereco):
    global dlg
    dlg.type_keys('{F6}') #vai para a barra de endereco
    time.sleep(1)
    dlg.type_keys('{DELETE 1000}')
    dlg.type_keys(Endereco)
    dlg.type_keys('{ENTER}')
    time.sleep(5)       

  def MouseClk(self, botao, x, y):
    if botao == 'esquerdo':
      mouse.click(button='left', coords=(x, y))
 
  def Tab(self,N):
    global dlg
    n_tabs = N
    if N < 0:
      dlg.type_keys('{VK_SHIFT down}')
      n_tabs = abs(N)
    argumento = "{TAB " + str(n_tabs) + "}"
    dlg.type_keys(argumento)
    if N < 0:
      dlg.type_keys('{VK_SHIFT up}')

  def Digita(self, texto):
    global dlg
    time.sleep(1)
    dlg.type_keys(texto, with_spaces=True)
    time.sleep(1)

  def DigitaComCtrl(self, texto):
    global dlg
    dlg.type_keys('{VK_LCONTROL down}')
    time.sleep(1)
    dlg.type_keys(texto)
    time.sleep(1)
    dlg.type_keys('{VK_LCONTROL up}')
    time.sleep(1)

  def DigitaComShift(self, texto):
    global dlg
    dlg.type_keys('{VK_SHIFT down}')
    time.sleep(1)
    dlg.type_keys(texto)
    time.sleep(1)
    dlg.type_keys('{VK_SHIFT up}')
    time.sleep(1)

  def DigitaNumKeyPad(self,N):
    global dlg
    for digito in N:
      if digito == '0':
         dlg.type_keys('{VK_NUMPAD0}')
      if digito == '1':
         dlg.type_keys('{VK_NUMPAD1}')
      if digito == '2':
         dlg.type_keys('{VK_NUMPAD2}')
      if digito == '3':
         dlg.type_keys('{VK_NUMPAD3}')
      if digito == '4':
         dlg.type_keys('{VK_NUMPAD4}')
      if digito == '5':
         dlg.type_keys('{VK_NUMPAD5}')
      if digito == '6':
         dlg.type_keys('{VK_NUMPAD6}')
      if digito == '7':
         dlg.type_keys('{VK_NUMPAD7}')
      if digito == '8':
         dlg.type_keys('{VK_NUMPAD8}')
      if digito == '9':
         dlg.type_keys('{VK_NUMPAD9}')

  def Enter(self):
    global dlg
    time.sleep(1)
    dlg.type_keys('{ENTER}')
    time.sleep(1)

  def CopiaTela(self):
    global dlg
    dlg.type_keys('^a')
    time.sleep(1)
    dlg.type_keys('^c')
    time.sleep(1)
    return clipboard.GetData()

  def DetectaTela(self,TextoProcurado):
    global dlg
    dlg.type_keys('^a')
    time.sleep(1)
    dlg.type_keys('^c')
    time.sleep(1)
    if TextoProcurado in clipboard.GetData():
      return True
    else:
      return False

  def CopiaSelecao(self):
    global dlg
    dlg.type_keys('^c')
    time.sleep(1)
    return clipboard.GetData()

  def Colar(self):
    global dlg
    dlg.type_keys('^v')
    time.sleep(1)
    return clipboard.GetData()

  def VoltarPaginaAnterior(self):
    global dlg
    dlg.type_keys('%{VK_LEFT}')
    time.sleep(1)

  def RecarregaTela(self):
    global dlg
    dlg.type_keys('^r')
    time.sleep(1)
    dlg.type_keys('{Enter}')
    time.sleep(1)

  def FechaJanela(self):
    global dlg
    dlg.type_keys('^{F4}') # control-F4, fecha a janela
    time.sleep(1)
  
  def FechaGuia(self):
    global dlg
    dlg.type_keys('^w') # control-F4, fecha a guia
    time.sleep(1)

  def ProximaGuia(self):
    global dlg
    dlg.type_keys('^{TAB}')
    time.sleep(1)

  def PaginaAnterior(self):
    global dlg
    dlg.type_keys('%{LEFT}') #alt-seta pra esquerda, volta para a pagina anterior
    time.sleep(1)

  def __TeclaComando__(self,Tecla):
    global dlg, ListaTeclasComando, ListaDigitaTeclasComando
    Posicao = ListaTeclasComando.index(Tecla)
    TeclaComando = ListaDigitaTeclasComando[Posicao]
    dlg.type_keys(TeclaComando)
    time.sleep(0.5)

  def DigitaTeclaComando(self,Tecla):
    # essa rotina aperta a Tecla
    # que nao e uma letra. Tipo seta para baixo e tal
    global dlg
    dlg = app.top_window()
    self.__TeclaComando__(Tecla)


##############################################
#              JANELA 3270 (WINDOWS)         #
##############################################
class janela3270:
  def __init__(self, TituloJanela):
    global app,dlg, ListaTeclasComando, ListaDigitaTeclasComando
    self.Tela = ''
    self.delay = 0.1
    app = Application().connect(title=TituloJanela)
    dlg = app.top_window()
    ListaTeclasComando = ('ENTER','PF1','PF2','PF3','PF4','PF5','PF6','PF7',
                          'PF8','PF9','PF10','PF11','PF12','PA1','PA2','END',
                          'HOME')
    ListaDigitaTeclasComando = ('{ENTER}','{F1}','{F2}','{F3}','{F4}','{F5}','{F6}','{F7}',
                                '{F8}','{F9}','{F10}','{F11}','{F12}','{PGUP}','{PGDN}','{END}',
                                '{HOME}')

  def SelecionaJanela(self):
    global app, dlg
    dlg = app.top_window()
    time.sleep(1)

  def Espaco(self,N):
    global dlg
    n_espacos = N
    argumento = "{SPACE " + str(n_espacos) + "}"
    dlg.type_keys(argumento)
  
  def Tab(self,N):
    global dlg
    n_tabs = N
    if N < 0:
      dlg.type_keys('{VK_SHIFT down}')
      n_tabs = abs(N)
    argumento = "{TAB " + str(n_tabs) + "}"
    dlg.type_keys(argumento)
    if N < 0:
      dlg.type_keys('{VK_SHIFT up}')

  def PosicionaCursorNaLinhaSiafi(self, tabs):
    # Vai para o primeiro campo digitavel e aperta TAB tabs vezes
    global dlg
    dlg.type_keys('{HOME}')
    self.Tab(tabs)

  def Digita(self, texto):
    global dlg
    time.sleep(self.delay)
    dlg.type_keys(texto, with_spaces=True)
    time.sleep(self.delay)

  def __Enter__(self):
    global dlg
    time.sleep(self.delay)
    dlg.type_keys('{ENTER}')
    time.sleep(self.delay)

  def __TeclaComando__(self,Tecla):
    global dlg, ListaTeclasComando, ListaDigitaTeclasComando
    Posicao = ListaTeclasComando.index(Tecla)
    time.sleep(self.delay)
    dlg.type_keys(ListaDigitaTeclasComando[Posicao])
    time.sleep(self.delay)

  def CopiaTela(self):
    global dlg
    dlg.type_keys('^a')
    time.sleep(self.delay)
    dlg.type_keys('^c')
    time.sleep(self.delay)
    self.Tela = clipboard.GetData() 
    return clipboard.GetData()

  def ViraTelaSiafiTecla(self,Tecla):
    # essa rotina aperta a Tecla
    # e fica esperando a tela mudar
    global dlg
    dlg = app.top_window()
    TelaInicial = self.CopiaTela()
    Tela = TelaInicial   
    self.__TeclaComando__(Tecla)
    while Tela == TelaInicial:
      time.sleep(self.delay)
      Tela = self.CopiaTela()
    return Tela

  def PegaTextoSiafi(self,Tela,L1,C1,L2,C2):
   # pegar um trecho do texto da tela que vai das coordenadas L1,C1 a L2,C2
   # tem que converter...achar o digito sequencial que equivale à coordenada
   D1 = (L1-1) * 82 + C1 - 1
   D2 = (L2-1) * 82 + C2
   return Tela [D1:D2]

  def EsperaTelaSiafiTextoLocalizacao(self,L1,C1,L2,C2,Texto,tecla_comando):
   # essa rotina serve para verificar se a tela da Rede Serpro mudou. 
   # Ela espera o texto
   # Por exemplo, da linha tal ate coluna tal uma certa palavra OU
   # de outra linha tal e outra coluna tal outra palavra e assim por
   # diante, ate que um dos requisitos seja aceito
    global dlg
    TelaEncontrada = 0
    while TelaEncontrada == 0:
      time.sleep(self.delay)
      Tela = self.CopiaTela()
      if self.PegaTextoSiafi(Tela,L1,C1,L2,C2)==Texto:
        TelaEncontrada = 1
      else:
        self.ViraTelaSiafiTecla(tecla_comando)

  def EsperaTelaSiafiTextoQualquerLugar(self,tuple_Texto,tecla_comando):
    # essa rotina serve para verificar se a tela da Rede Serpro mudou. 
    # Ela espera o texto, so que diferentemente da funcao logo acima,
    # esta checa a existencia de varias possibilidades de texto.
    global dlg
    global D1, D2, L, C1, C2, Encontrou, CoordenadasTexto
    D1 = 0
    D2 = 0
    L  = 0
    C1 = 0
    C2 = 0
    Encontrou = False

    def buscaTextos():
      global D1, D2, L, C1, C2, Encontrou, CoordenadasTexto
      for Texto in tuple_Texto:
        if Texto in Tela:
          D1 = Tela.find(Texto) + 1 # somando um porque o string comeca de zero
          D2 = D1 + len(Texto)
          L = D1 // 82 + 1 # so a parte inteira
          C1 = D1 % 82
          C2 = C1 + len(Texto) - 1
          CoordenadasTexto = (L,C1,L,C2,tuple_Texto.index(Texto))
          Encontrou = True 
          return  

    Tela = self.CopiaTela()
    buscaTextos()
    while not(Encontrou):      
      Tela = self.ViraTelaSiafiTecla(tecla_comando) 
      buscaTextos() 
    return CoordenadasTexto

  def AcessaSistemaDepoisDaPrimeiraSenha(self, Sistema):
    global dlg
    IdentificaTela = 'NOME'
    while IdentificaTela == 'NOME':
      self.Digita(Sistema)
      self.ViraTelaSiafiTecla('ENTER')
      time.sleep(20)
      Tela = self.CopiaTela()
      IdentificaTela = self.PegaTextoSiafi(self.Tela, 8, 10, 8, 13)  
    Sistema = Sistema.upper()
    if Sistema == 'SIASG':
      self.Digita('x')
      self.ViraTelaSiafiTecla('ENTER')
      self.ViraTelaSiafiTecla('ENTER')
    if Sistema == 'SIAFI':
      self.Digita('x')
      self.ViraTelaSiafiTecla('ENTER')

##############################################
#              JANELA 3270 (MAC - PYAUTOGUI) #
##############################################
class janela3270PyAutoGui:
  def __init__(self, NaoServeParaNada): # esse nao serve para nada e apenas para ficar igual ao outro objeto
    global ListaTeclasComando, ListaDigitaTeclasComando
    self.Tela = ''
    self.delay = 0.1
    ListaTeclasComando = ('ENTER','PF1','PF2','PF3','PF4','PF5','PF6','PF7',
                          'PF8','PF9','PF10','PF11','PF12','PA1','PA2','END',
                          'HOME')
    ListaDigitaTeclasComando = ('enter','f1','f2','f3','f4','f5','f6f','f7',
                                'f8','f9','f10','f11','f12','pgup}','pgdn','end',
                                'home')
    # Pagui.alert('Selecione a janela do HOD.\nO script vai comecar em 5 segundos.')
    time.sleep(5)
    # Pagui.pause = 0.1

  def Espaco(self,N):
    for n_espacos in range(1,N+1):
      Pagui.press('space')

  def Tab(self,N):
    for n_tabs in range(1,abs(N)+1):
      if N < 0:
        Pagui.hotkey('shift','tab')
      else:
        Pagui.press('tab')

  def PosicionaCursorNaLinhaSiafi(self, tabs):
    # Vai para o primeiro campo digitavel e aperta TAB tabs vezes
    Pagui.press('home')
    self.Tab(tabs)

  def Digita(self, texto):
    time.sleep(self.delay)
    Pagui.write(texto)
    time.sleep(self.delay)

  def __Enter__(self):
    time.sleep(self.delay)
    Pagui.press('enter')
    time.sleep(self.delay)

  def __TeclaComando__(self,Tecla):
    global ListaTeclasComando, ListaDigitaTeclasComando
    Posicao = ListaTeclasComando.index(Tecla)
    time.sleep(self.delay)
    Pagui.press(ListaDigitaTeclasComando[Posicao])
    time.sleep(self.delay)

  def CopiaTela(self):
    Pagui.hotkey('ctrl','a')
    time.sleep(self.delay)
    Pagui.hotkey('ctrl','c')
    time.sleep(self.delay)
    self.Tela = clipboard.paste()
    return self.Tela

  def ViraTelaSiafiTecla(self,Tecla):
    # essa rotina aperta a Tecla
    # e fica esperando a tela mudar
    TelaInicial = self.CopiaTela()
    Tela = TelaInicial   
    self.__TeclaComando__(Tecla)
    while Tela == TelaInicial:
      time.sleep(self.delay)
      Tela = self.CopiaTela()
    return Tela

  def PegaTextoSiafi(self,Tela,L1,C1,L2,C2):
   # pegar um trecho do texto da tela que vai das coordenadas L1,C1 a L2,C2
   # tem que converter...achar o digito sequencial que equivale à coordenada
   Tela = Tela.replace('\n', '')
   D1 = (L1-1) * 80 + C1 - 1
   D2 = (L2-1) * 80 + C2
   return Tela [D1:D2]

  def EsperaTelaSiafiTextoLocalizacao(self,L1,C1,L2,C2,Texto,tecla_comando):
   # essa rotina serve para verificar se a tela da Rede Serpro mudou. 
   # Ela espera o texto
   # Por exemplo, da linha tal ate coluna tal uma certa palavra OU
   # de outra linha tal e outra coluna tal outra palavra e assim por
   # diante, ate que um dos requisitos seja aceito
    TelaEncontrada = 0
    while TelaEncontrada == 0:
      time.sleep(self.delay)
      Tela = self.CopiaTela()
      if self.PegaTextoSiafi(Tela,L1,C1,L2,C2)==Texto:
        TelaEncontrada = 1
      else:
        self.ViraTelaSiafiTecla(tecla_comando)

  def EsperaTelaSiafiTextoQualquerLugar(self,tuple_Texto,tecla_comando):
    # essa rotina serve para verificar se a tela da Rede Serpro mudou. 
    # Ela espera o texto, so que diferentemente da funcao logo acima,
    # esta checa a existencia de varias possibilidades de texto.
    global dlg
    global D1, D2, L, C1, C2, Encontrou, CoordenadasTexto
    D1 = 0
    D2 = 0
    L  = 0
    C1 = 0
    C2 = 0
    Encontrou = False

    def buscaTextos():
      global D1, D2, L, C1, C2, Encontrou, CoordenadasTexto
      for Texto in tuple_Texto:
        if Texto in Tela:
          D1 = Tela.find(Texto) + 1 # somando um porque o string comeca de zero
          D2 = D1 + len(Texto)
          L = D1 // 82 + 1 # so a parte inteira
          C1 = D1 % 82
          C2 = C1 + len(Texto) - 1
          CoordenadasTexto = (L,C1,L,C2,tuple_Texto.index(Texto))
          Encontrou = True 
          return  

    Tela = self.CopiaTela()
    buscaTextos()
    while not(Encontrou):      
      Tela = self.ViraTelaSiafiTecla(tecla_comando) 
      buscaTextos() 
    return CoordenadasTexto

  def AcessaSistemaDepoisDaPrimeiraSenha(self, Sistema):
    global dlg
    IdentificaTela = 'NOME'
    while IdentificaTela == 'NOME':
      self.Digita(Sistema)
      self.ViraTelaSiafiTecla('ENTER')
      time.sleep(20)
      Tela = self.CopiaTela()
      IdentificaTela = self.PegaTextoSiafi(self.Tela, 8, 10, 8, 13)  
    Sistema = Sistema.upper()
    if Sistema == 'SIASG':
      self.Digita('x')
      self.ViraTelaSiafiTecla('ENTER')
      self.ViraTelaSiafiTecla('ENTER')
    if Sistema == 'SIAFI':
      self.Digita('x')
      self.ViraTelaSiafiTecla('ENTER')
    
##############################################
#              SQLite - Bando de Dados       #
##############################################
class ObjetoBancoDados:
  
  def __init__(self, ArqBancoDados):
    self.BancoDados = sqlite3.connect(ArqBancoDados)

  def Create (self, NomeTabela, Estrutura: str):
    # A Estrutura e uma lista de listas.
    # [NomeCampo,   TipoCampo,     Tamanho,     se pode ser nulo,    se e indice]
    # TipoCampo pode ser: 'A', 'I', 'N' - (string, inteiro, float)
    # Por exemplo
    # [DataEmp, 'a', 10, True  , True]
    # [Valor  , 'N',  0, False, False]
    # Fica fácil fazer a estrutura da tabela no Excel, e ai substituir alguns caracteres no Notepad para fazer a lista
    global BD, BancoDados
    sql = 'CREATE TABLE "'  + NomeTabela + '" (\n'
    Indice = ''
    for Campo in Estrutura:
      # Nome do Campo
      linha = '  "' + Campo[0] + '"            '
      # Tipo do Campo
      TipoCampo = Campo[1].upper()
      if TipoCampo == 'A':
        linha = linha + 'VARCHAR(' + str(Campo[2]) + ')'
      if TipoCampo == 'I':
        linha = linha + 'INTEGER'
      if TipoCampo == 'N':
        linha = linha + 'REAL'
      # Se pode ser nulo
      if Campo[3] == True:
        linha = linha + ' NOT NULL'
      # se e indice
      if Campo[4] == True:
        Indice = Indice + '"' + Campo[0] + '",'
      # Finalizando a linha
      linha = linha + ',\n'
      sql = sql + linha

    if len(Indice) > 0:
      Indice = Indice[0:len(Indice)-1]
      Indice = '  CONSTRAINT "INDICE" PRIMARY KEY(' + Indice + ')\n'
      sql = sql + Indice
    else:
      sql = sql[0:len(sql)-2]
    sql = sql + '\n)'
    print(sql)
    try:
      BD = self.BancoDados.cursor()
      BD.execute(sql)
      self.BancoDados.commit()
    except sqlite3.Error as erro:
      print("Erro ao criar tabela: ", erro)

  # # # # # # # # # # # # # # # # # # # # # # # # # #

class ObjetoTabela:

  def __init__(self, ObjetoBancoDados, NomeTabela):
    global BancoDados, BD, Tabela
    BancoDados = ObjetoBancoDados
    Tabela = NomeTabela
    BD = BancoDados.cursor()
    # TipoCampo = []
    # BD.execute("pragma table_info('"+NomeTabela+"')")
    ## Pragma = BD.fetchall()
    #for row in Pragma:
    #  TpCampo = row[2]
    #  TpCampo = TpCampo.upper()
    #  if TpCampo[0:7] == 'VARCHAR':
    #    TipoCampo.append('STRING')
    #  else:
    #    TpCampo = row[2]
    #    TpCampo = TpCampo.upper()
    #    TipoCampo.append(TpCampo)
       # endif
    # next
  
  def Select(self, ListaCampos: list, ListaCamposOrdem: list, ListaAscOuDesc: list, CondicaoWhere: str):
    # ListaCampos é sao os campos que devem retornar
    # CondicaoWhere é um STRING
    # Entre os campos que devem retornar,
    # ListaCamposOrdem e a lista dos que vai vir em ordem
    # ListaAscOuDesc e uma lista correspondente (evidentemente com a mesma quantidade) que
    # diz se a ordem de cada um desses campos e ascendente ou descendente.

    global Tabela, BD
    sql = 'select ' + ','.join(ListaCampos) + ' from ' + Tabela + '\n'
    if CondicaoWhere == None:
      CondicaoWhere = ''
    CondicaoWhere = CondicaoWhere.strip()
    if CondicaoWhere != '':
      sql = sql + 'Where ' + CondicaoWhere + '\n'
    if ListaCamposOrdem == None:
      ListaCamposOrdem = []
    if len(ListaCamposOrdem) > 0:
      sql = sql + 'ORDER BY '
      i = 0
      for CampoOrdem in ListaCamposOrdem:
        sql = sql + CampoOrdem + ' '
        if ListaAscOuDesc[i]==True:
          sql = sql + 'Asc,'
        else:
          sql = sql +'DESC,'
        i = i + 1
      sql = sql[:len(sql)-1]
    try:
      BD.execute(sql)
      Resultado = BD.fetchall()
    except sqlite3.Error as erro:
      print("Erro ao pesquisar: ", erro)
    return Resultado

  def Delete (self, CondicaoWhere: str):
    global Tabela, BD, BancoDados
    sql = 'DELETE FROM ' + Tabela + '\n'
    CondicaoWhere = CondicaoWhere.strip()
    if CondicaoWhere != '':
      sql = sql + 'Where ' + CondicaoWhere
    try:
      BD.execute(sql)
      BancoDados.commit()
    except sqlite3.Error as erro:
      print("Erro ao excluir: ", erro)

  def Insert (self, ListaInclusoes: list):
    # Aqui e o mais complicado
    # A lista de entrada e uma LISTA DE LISTAS
    # Ou seja uma lista de todos os registros a serem incluidos
    # Sendo que cada registro e uma lista de dados a serem incluidos,
    #  na mesma quantidade de campos existentes (isso é ESSENCIAL)
    global Tabela, BD, BancoDados
    for Registro in ListaInclusoes:
      try:
        sql = 'INSERT INTO ' + Tabela + ' VALUES('
        for Campo in Registro:
          if type(Campo) is str:
            sql = sql + '"' + Campo + '",'
          else:
            sql = sql + str(Campo) + ','
        sql = sql[:len(sql)-1] + ')'
        BD.execute(sql)
      except sqlite3.Error as erro:
        print("Erro ao inserir: ", erro)
        print(ListaInclusoes)
        print(sql)
      BancoDados.commit()

  def Update (self, ListaNomeCampos: list, ListaValoresCampos: list, CondicaoWhere: str):
    # Aqui chega a lista dos campos a serem atualizados e a lista
    # dos novos valores que receberao. Obviamente precisam ter o mesmo tamanho.
    # Tambem vem a condicao da alteracao
    global Tabela, BD, BancoDados
    sql = 'UPDATE ' + Tabela + ' SET '
    indice = 0
    for Campo in ListaNomeCampos:
      sql = sql + Campo + '='
      Valor = ListaValoresCampos[indice]
      if type(Valor) is str:
        sql = sql + '"' + Valor + '",'
      else:
        sql = sql + str(Valor) + ','
      indice = indice + 1
    sql = sql[:len(sql)-1]
    sql = sql + ' WHERE ' + CondicaoWhere
    try:
      BD.execute(sql)
    except sqlite3.Error as erro:
      print("Erro ao alterar: ", erro)
    BancoDados.commit()
