import MacrosClasses

# MUDAR O CPF AQUI!!!!!!
cpf = '13145010115'

# completa zero a esqueda
cpf = cpf.zfill(11)

Acesso = MacrosClasses.janela3270("Terminal 3270 - A - AWVAKJR7")

Acesso.Tab(1)
Acesso.Digita(cpf)
Tela = Acesso.ViraTelaSiafiTecla('ENTER')

# DIGITA OS DADOS FICTICIOS PARA CAIR NO PSS NO CAINPCAHIS
Acesso.Digita("014003")
Acesso.Digita("40")
Acesso.Digita("02")
Acesso.Tab(1)

# NO DEFINITIVO MUDAR PARA 1998
Acesso.Digita("01JAN1999") 
Acesso.Digita("534")
Acesso.Tab(1)

Acesso.Digita("PROVIMENTO")
Acesso.Tab(1)

Acesso.Digita("01JAN2014")
Acesso.Digita("534")
Acesso.Tab(1)
Acesso.Digita("VACANCIA")
Acesso.Tab(1)

Acesso.Digita("N")

Acesso.ViraTelaSiafiTecla('ENTER')

#Acesso.Tab(1)
Acesso.Digita("x")
Acesso.ViraTelaSiafiTecla('ENTER')
Acesso.ViraTelaSiafiTecla('ENTER')
Acesso.ViraTelaSiafiTecla('ENTER')

