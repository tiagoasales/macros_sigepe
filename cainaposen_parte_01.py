import MacrosClasses
import pandas as pd

df = pd.read_csv('./input/cainaposen01_julho.csv', dtype=str, nrows=1)

df = df.fillna(' ')

Acesso = MacrosClasses.janela3270("Terminal 3270 - A - AWVAKJR7")

for index, row in df.iterrows():

    #Acesso.Tab(8)

    #Acesso.Digita('>cainaposen')

    #Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita(row['cpf'])

    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    # Descomentar a linha abaixo se o cpf estiver desativado
    Tela = Acesso.ViraTelaSiafiTecla('ENTER')

    retorno = Acesso.PegaTextoSiafi(Tela, 6, 3, 6, 12)

    if (retorno == 'FUNDAMENTO'):
        print('não faz nada')
        break

    # Tela de Confirmação de que o CPF não está cadastrado
    Acesso.ViraTelaSiafiTecla('ENTER')

    # Tela para preenchimento de nome social (não vai preencher nada)
    Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.Digita(row['nome'])
    Acesso.Tab(1)

    Acesso.Digita(row['sexo'])

    Acesso.Digita(row['grupo_sanguineo'])
    if len(row['grupo_sanguineo']) < 5:
        Acesso.Tab(1)

    Acesso.Digita(row['nome_pai'])
    Acesso.Tab(1)

    Acesso.Digita(row['nome_mae'])
    Acesso.Tab(1)

    Acesso.Digita(row['naturalidade'])
    Acesso.Tab(1)

    Acesso.Digita(row['naturalidade_uf'])
    #Acesso.Tab(1)

    Acesso.Digita(row['id_tipo_escolaridade'])
    #Acesso.Tab(1)

    Acesso.Digita(row['id_tipo_estado_civil'])
    #Acesso.Tab(1)

    # uniao estavel
    Acesso.Digita('N')

    Acesso.Digita(row['cor_origem'])
    #Acesso.Tab(1)

    Acesso.Digita(row['id_tipo_necessidade_especial'])
    #Acesso.Tab(1)

    qtdDependentesEcon = '00'
    Acesso.Digita(qtdDependentesEcon)
    #Acesso.Tab(1)

    Acesso.Digita(row['id_tipo_nacionalidade'])

    Acesso.Digita('N')
    #break
    
    Acesso.ViraTelaSiafiTecla('ENTER')


    ##### SEGUNDA TELA #######

    Acesso.Digita('RG')
    Acesso.Tab(1)
    
    Acesso.Digita(row['identidade'])
    Acesso.Tab(1)

    Acesso.Digita(row['rg_orgao_expedidor'])
    if len(row['rg_orgao_expedidor']) < 5:
        Acesso.Tab(1)

    Acesso.Digita(row['rg_uf'])
    #Acesso.Tab(1)

    Acesso.Digita(row['rg_data_expedicao'])
    #Acesso.Tab(1)

    Acesso.Digita(row['eleitor'])
    if len(row['eleitor']) == 1:
        Acesso.Tab(1)

    Acesso.Digita(row['el_uf'])
    if len(row['eleitor']) == 1:
        Acesso.Tab(1)

    Acesso.Digita(row['zona_eleitoral'])
    if len(row['eleitor']) == 1:
        Acesso.Tab(1)

    Acesso.Digita(row['secao_eleitoral'])
    if len(row['eleitor']) == 1:
        Acesso.Tab(1)
    
    Acesso.Digita(row['data_titulo_eleitoral'])
    if len(row['eleitor']) == 1:
        Acesso.Tab(1)
    
    Acesso.Tab(3)

    carteiraDigital = 'N'
    Acesso.Digita(carteiraDigital)
    Acesso.Tab(10)

    Acesso.Digita(row['nitpis'])
    #Acesso.Tab(11)
    #break

    Acesso.ViraTelaSiafiTecla('ENTER')

    ##### TERCEIRA TELA #######

    Acesso.Digita(row['endereco_logradouro'])
    Acesso.Tab(1)

    Acesso.Digita('01')

    Acesso.Digita(row['endereco_numero'])
    Acesso.Tab(1)

    Acesso.Digita(row['endereco_complemento'])
    Acesso.Tab(1)

    Acesso.Digita(row['bairro'])
    Acesso.Tab(1)

    Acesso.Digita(row['cidade'])
    Acesso.Tab(1)


    Acesso.Digita(row['uf'])
    if len(row['uf']) == 1:
        Acesso.Tab(1)
    
    Acesso.Digita(row['id_pais'])
    if len(row['id_pais']) != 3:        
        Acesso.Tab(1)

    Acesso.Digita(row['cep'])
    Acesso.Tab(1)

    Acesso.Digita(row['codigo_area_telefone'])
    Acesso.Tab(1)

    Acesso.Digita(row['telefone'])
    if len(row['telefone']) == 9:
        Acesso.Tab(1)
    else :
        Acesso.Tab(2)

    Acesso.Digita(row['codigo_area_celular'])
    Acesso.Tab(1)

    Acesso.Digita(row['celular'])
    if row['celular'] == ' ':
        Acesso.Tab(3)
    else :
        Acesso.Tab(2)

    Acesso.Digita(row['email'])
        
    Acesso.ViraTelaSiafiTecla('ENTER')

    ##### QUARTA TELA #######

    contaTipo = '04'
    Acesso.Digita(contaTipo)
    #Acesso.Tab(1)

    Acesso.Digita(row['banco_agencia'])
    #Acesso.Tab(2)

    Acesso.Digita(row['conta_corrente'])
    Acesso.Tab(1)

    Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.ViraTelaSiafiTecla('PF8')

    Acesso.ViraTelaSiafiTecla('ENTER')

    confirmaInclusao = 'S'
    Acesso.Digita(confirmaInclusao)

    #Acesso.ViraTelaSiafiTecla('ENTER')

    break