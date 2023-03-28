import MacrosClasses
Acesso    = MacrosClasses.janela3270("Terminal 3270 - A - AWV38731")

Saida     = open("c:/RobosDados/Saida.txt" , 'w')
Cabecalho = '"Restricao' + '"'+'\t'+'"' + 'Titulo' + '"'+'\t'+'"' + 'Grupo' + '"'+'\t'+'"' + 'Descricao"' + '\n'
Saida.write(Cabecalho)
Saida.close()

Continua = 'CONTINUA'
while Continua == 'CONTINUA':
  i=0
  for L in range(6,22):
    Acesso.Tab(i)
    TelaDescricao=Acesso.ViraTelaSiafiTecla('PF2')
    Restricao = Acesso.PegaTextoSiafi(TelaDescricao, 5, 15, 5, 17)
    Titulo    = Acesso.PegaTextoSiafi(TelaDescricao, 6, 15, 6, 80)
    Titulo    = Titulo.strip()
    Grupo     = Acesso.PegaTextoSiafi(TelaDescricao, 7, 15, 7, 80)
    Grupo     = Grupo.strip()
    Descricao     = Acesso.PegaTextoSiafi(TelaDescricao, 8, 15, 8, 69)
    Descricao     = Descricao.strip() + ' '
    for L_Desc in range(9,22):
      UmaLinhaDescricao = Acesso.PegaTextoSiafi(TelaDescricao, L_Desc, 15, L_Desc, 69)
      UmaLinhaDescricao = UmaLinhaDescricao.strip()
      if UmaLinhaDescricao == '':
        break
      if UmaLinhaDescricao[len(UmaLinhaDescricao)-1]=='-':
        UmaLinhaDescricao=UmaLinhaDescricao[0:len(UmaLinhaDescricao)-2]
      Descricao = Descricao + UmaLinhaDescricao
    Acesso.ViraTelaSiafiTecla('PF12')
    i=i+1  

    Saida     = open("c:/RobosDados/Saida.txt" , 'a')
    Saida.write('"' + Restricao + '"'+'\t'+'"' + Titulo + '"'+'\t'+'"' + Grupo + '"'+'\t'+'"'+ Descricao +'"')
    Saida.write('\n')
    Saida.close()

  Tela=Acesso.ViraTelaSiafiTecla('ENTER')
  Continua = Acesso.PegaTextoSiafi(Tela, 22, 61, 22, 68)