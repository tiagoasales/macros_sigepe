import MacrosClasses
import pandas as pd

df = pd.read_csv('aposentados_07.csv', dtype=str)

df = df.fillna(' ')

Acesso = MacrosClasses.janela3270("Terminal 3270 - A - AWVAKJR7")

for index, row in df.iterrows():

    Acesso.Tab(9)

    Acesso.Digita('>cainaposen')

    Acesso.ViraTelaSiafiTecla('ENTER')

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

    sexo = 'M'
    Acesso.Digita(row['sexo'])
    #Acesso.Tab(1)

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

    escolaridade = '10'
    Acesso.Digita(row['id_tipo_escolaridade'])
    #Acesso.Tab(1)

    Acesso.Digita(row['id_tipo_estado_civil'])
    #Acesso.Tab(1)

    Acesso.Digita(row['cor_origem'])
    #Acesso.Tab(1)

    Acesso.Digita(row['id_tipo_necessidade_especial'])
    #Acesso.Tab(1)

    qtdDependentesEcon = '00'
    Acesso.Digita(qtdDependentesEcon)
    #Acesso.Tab(1)

    Acesso.Digita(row['id_tipo_nacionalidade'])
    
    Acesso.ViraTelaSiafiTecla('ENTER')

    ##### SEGUNDA TELA #######

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
    #Acesso.Tab(1)

    Acesso.Digita(row['el_uf'])
    #Acesso.Tab(1)

    Acesso.Digita(row['zona_eleitoral'])
    #Acesso.Tab(1)

    Acesso.Digita(row['secao_eleitoral'])
    #Acesso.Tab(4)
    
    Acesso.Digita(row['data_titulo_eleitoral'])
    Acesso.Tab(3)

    carteiraDigital = 'N'
    Acesso.Digita(carteiraDigital)
    Acesso.Tab(10)

    Acesso.Digita(row['nitpis'])
    #Acesso.Tab(11)

    Acesso.ViraTelaSiafiTecla('ENTER')

    ##### TERCEIRA TELA #######

    logradouro = 'RUA PROFESORA ENEIDA RABELO'
    Acesso.Digita(row['endereco_logradouro'])
    Acesso.Tab(1)

    numero = '856'
    Acesso.Digita(row['endereco_numero'])
    Acesso.Tab(1)

    complemento = 'AP 301'
    Acesso.Digita(row['endereco_complemento'])
    Acesso.Tab(1)

    bairro = 'CANDEIAS'
    Acesso.Digita(row['bairro'])
    Acesso.Tab(1)

    municipio = 'JABOATAO DOS GUARARAPES'
    Acesso.Digita(row['cidade'])
    Acesso.Tab(1)

    municipioUf = 'PE'
    Acesso.Digita(row['uf'])
    Acesso.Tab(1)

    cep = '54440310'
    Acesso.Digita(row['cep'])
    Acesso.Tab(1)

    telefoneDDD = '81'
    Acesso.Digita(row['codigo_area_telefone'])
    Acesso.Tab(1)

    telefone = '33421570'
    Acesso.Digita(row['telefone'])
    if len(row['telefone']) == 9:
        Acesso.Tab(1)
    else :
        Acesso.Tab(2)

    celularDDD = '81'
    Acesso.Digita(row['codigo_area_celular'])
    Acesso.Tab(1)

    celular = '999966051'
    Acesso.Digita(row['celular'])
    if row['celular'] == ' ':
        Acesso.Tab(3)
    else :
        Acesso.Tab(2)

    email = 'lcjatoba@hotmail.com'
    Acesso.Digita(row['email'])

    Acesso.ViraTelaSiafiTecla('ENTER')

    ##### QUARTA TELA #######

    contaTipo = '04'
    Acesso.Digita(contaTipo)
    #Acesso.Tab(1)

    bancoAgencia = '104/01580/6'
    Acesso.Digita(row['banco_agencia'])
    #Acesso.Tab(2)

    contaNumero = '0000108761'
    Acesso.Digita(row['conta_corrente'])
    Acesso.Tab(1)

    Acesso.ViraTelaSiafiTecla('ENTER')

    Acesso.ViraTelaSiafiTecla('PF8')

    Acesso.ViraTelaSiafiTecla('ENTER')

    confirmaInclusao = 'S'
    Acesso.Digita(confirmaInclusao)

    #Acesso.ViraTelaSiafiTecla('ENTER')

    break