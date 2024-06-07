#   GLOBAL
#   SOLUTION
'''
Junho/2024
'''
# 556030	- Caio Venancio
# 557538	- David Cordeiro
# 555619	- Tiago Morais
'''
DESCRITIVO:
Disciplina: Computational Thinking With Python

De acordo com o escopo levantado na disciplina de Software & Total Experience
Design e Storytelling e Inspiração Empreendedora, desenvolva um protótipo
funcional em Python que aborde o tema.

Na entrega do protótipo você deve demonstrar conhecimento dos seguintes requisitos:

• Conhecimentos básicos em Python: Os alunos devem possuir conhecimentos
básicos em Python, incluindo variáveis, tipos de dados, estruturas de controle (if,
elif, else, while, for);
• Manipulação de Listas e Strings: Capacidade de manipular listas e strings,
incluindo operações como adição, remoção, concatenação e iteração sobre os elementos;
• Conhecimento em Funções: Habilidade para criar e utilizar funções, incluindo
a definição de funções com parâmetros e retorno de valores.

→ Entrega 1 - Documentação Técnica em Python (10 pontos)
Elaborar um arquivo README contendo nome e RM do aluno, descrevendo detalhes
do projeto, instruções de uso, requisitos, dependências e demais informações
relevantes ao projeto. Será avaliada a clareza e organização do conteúdo apresentado.

→ Entrega 2 - Vídeo Explicativo (10 pontos)
Produzir um vídeo explicativo de até 5 minutos, abordando os seguintes pontos:
Identificação do Problema: Apresentar motivação e solução para o problema;
Solução Proposta: Explicar como a solução irá abordar o problema.
Demonstração da Solução: demonstrar o funcionamento do programa, com
gravação de tela e narração do aluno, destacando as funcionalidades
implementadas e demonstrando onde foram aplicadas as estruturas de programação.

→ Entrega 3 - Protótipo Funcional em Python (70 pontos)
Código Fonte em Python, desenvolvido em conformidade com as
boas práticas de programação, incluindo comentários
explicativos, estruturação lógica do código e atendendo aos prérequisitos supracitados.
'''

# INSTRUÇÕES:
# Para rodar o software, execute "código.py";
# Para uma experiência melhor, redimensione a altura do terminal para caber apenas 7 linhas de output;
# Navegue pelos menus digitando o número do menu que quer acessar e clique <enter>

# DEPENCÊNCIAS:
# Bibliotecas "time" e "datetime"
# Terminal/Output console que suporte "ANSI escape codes", para formatar a saída em terminais de texto (Recomendado: Microsoft VSCode)
# Terminal/Outpur console que suporte Unicode 

# REPOSITÓRIO REMOTO: 
# https://github.com/dev-tiago-neto/prototipo_app_de_denuncias

''' 
ÁRVORE DE MENUS:
Menu de login/cadastro:
  - usuário
  - cadastro
Menu logado:
    Menu de reports:
    - Create
    - Read
    Meu perfil:
    - Meus dados
    - Meus reports
    Menu quero contribuir:
    - PF: Redirecionar para ONG
    - PJ: Preenche formulário
'''
# ==============================================================================================================================================
# Bibliotecas:

import time     # Para adicionar delays ao código
import datetime # Para comparar datas e fazer busca de denuncias por filtro de tempo

# ==============================================================================================================================================
# Funções:

def init():                                 # Animação de entrada
    print()     
    print(f'∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~  \n'
          f'                               \n'
          f'       SAVE                    \n'
          f'         ⏇he Oceans           \n'
          f'                               \n'
          f'∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~')
    time.sleep(1.2)
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  \n'
          f'   ﹡               ﹡         \n'
          f'       SAVE              ⚹    \n'
          f' ٭       ⏇he Oceans           \n'
          f'     *                 ✧      \n'
          f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(0.7)
    print(f'∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~  \n'
          f'  ﹡                 ﹡        \n'
          f'       SAVE               ⚹   \n'
          f'٭        ⏇he Oceans           \n'
          f'    *                   ✧     \n'
          f'∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~')
    time.sleep(0.7)
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  \n'
          f'   ﹡               ﹡         \n'
          f'       SAVE              ⚹    \n'
          f' ٭       ⏇he Oceans           \n'
          f'     *                 ✧      \n'
          f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(2.2)
    print(f'\n\n\n\n\n')

def respostaUsuario(msg):                   # Pedir inputs (2 casos: msg padrao ou personalizada)
    # print(' Entrou resposta usuario')         #[DEBUG]
    if msg == '':
        resposta = input(' → ')         # Caso 1: Input padrão
    else:
        resposta = input(msg)           # Caso 2: Input customizado
    return resposta

def printarLista(listaOpcoes):              # Imprime todos os elementos de lista
    for elemento in listaOpcoes:
        if listaOpcoes == allReports:                           # Caso Debug do banco de dados de denúncias: quebra de linha
            print(f'{elemento}', end = '\n')
        else:                                                   # Caso genérico: lado a lado
            print(f'{elemento}', end = ' ')

def pegarIndice(elem, listaAnalisada):      # Pega o índice de um elemento em uma lista
    for i in range(len(listaAnalisada)):
        if elem == listaAnalisada[i]:
            return i

def naLista(listaOpcoes, resposta):         # Varre lista procurando elemento; Out: true/false
    for opcao in listaOpcoes:
        if resposta == opcao:
            return True
    return False

def repetirPedido(resposta,listaOpcoes):    # Pede outro input se input não é opção válida
    # print(' Entrou repetir pedido')                           #[DEBUG]
    while not (naLista(listaOpcoes, resposta)):         # Repete até o input ser válido
        # print(' Entrou no while')                             #[DEBUG]
        print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  \n'
              f'      SAVE ⏇he Oceans          \n'
              f'                                \n'
              f'      Opção Inválida!           \n'
              f'   Escolha uma: ',end='')                           # Indica a lista de opções válidas
        if listaOpcoes == listaSiglas:
            print(' ex: AL',end='')         # Caso siglas de estados: texto grande, não listar
        else:
            printarLista(listaOpcoes)       # Caso padrão: listar opções válidas
        print(f'\n~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿ ')
        resposta = respostaUsuario('')
        if resposta.isnumeric():            # Caso lista de números: usado para navegar, string vira int
            resposta = int(resposta)
    return resposta

def validarOpcao(listaOpcoes, resposta):    # Função para validar se input é válido
    # print(' Entrou validar opcoes')                           #[DEBUG]
    if resposta == '':
        resposta = respostaUsuario('')
    if resposta.isnumeric():            # Checa se é numérico para validarOpcao()
        resposta = int(resposta)
    resposta = repetirPedido(resposta, listaOpcoes)
    # print(f' Saiu repetirPedido com resposta = {resposta}')   #[DEBUG]
    return resposta                     # Retorna uma resposta válida (pertencente à lista de opções recebida)

def imprimirMenu(tela, listaOpcoes, flag):  # Função genérica para gerar menus
    # print(' Entrou Menu')                 #[DEBUG]
    print(tela)         
    if flag == '' and listaOpcoes == []:                        # Caso 1: menu sem opções (ex: login), só pega o input
        # print(' Entrou caso 1')           #[DEBUG]
        variavel = respostaUsuario('')
        return variavel
    # print(' Entrou Caso 2')               #[DEBUG]
    resposta = validarOpcao(listaOpcoes,'')                     # Caso 2: menu com várias opções, pede o input até ser válido
    # print(f'respposta pos validaropcao(): {resposta} {type(resposta)}')       #[DEBUG]
    # print(' Saiu validar opcao, de volta pra menu')                           #[DEBUG]
    # print(f' flag = {flag}')                                                  #[DEBUG]
    opcoesMenu(resposta,flag)

def tentaLogin(userTentativa,pwTentativa):  # Cruza [user,senha] de input com a base
    tentativa = []          
    tentativa.append(userTentativa)
    tentativa.append(pwTentativa)
    copiaLista = usuariosCadastrados           # Clona lista de usuários cadastrados
    for usuario in copiaLista:              #    user    senha   nome
        if len(usuario) == 3:               # [['admin','admin','administrador']]
            usuario.pop()                   # Apaga 'nome' dos cadastros clonados
    for i in range(len(copiaLista)):
        if tentativa == copiaLista[i]:            # Compara par ['user','senha'] de input com a base de dados
            historicoUserSenhaLogados.append(tentativa)
            return True                     # Valida Log-in
    return False                            # Barra Log-in

def tryUserNotFoundOrLogin(loginRealizado): # Avança se login válido ou Imprime tela e volta se login inválido 
    if not(loginRealizado):             # Login inválido: imprime mensagem de erro e regride ao menu anterior
            print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                    f'       SAVE ⏇he Oceans         \n'
                    f'                                \n'
                    f'   Usuário não encontrado!      \n'
                    f'                                \n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  ')
            time.sleep(2)
            menuInicial()
    if (loginRealizado):                # Login válido: progride ao próximo menu
        bemVindo()
        menuLogado()

def logout():                               # Animação de logout
    time.sleep(1.2)
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
            f'       SAVE ⏇he Oceans       \n'
            f'                              \n'
            f'      Deslogando              \n'
            f'                              \n'
            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  ')
    time.sleep(0.7)
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
            f'       SAVE ⏇he Oceans       \n'
            f'                              \n'
            f'      Deslogando .            \n'
            f'                              \n'
            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  ')
    time.sleep(0.7)
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
            f'       SAVE ⏇he Oceans       \n'
            f'                              \n'
            f'      Deslogando . o          \n'
            f'                              \n'
            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  ')
    time.sleep(0.7)
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
            f'       SAVE ⏇he Oceans       \n'
            f'                              \n'
            f'      Deslogando . o O        \n'
            f'                              \n'
            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  ')
    time.sleep(1.2)
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
            f'       SAVE ⏇he Oceans       \n'
            f'                              \n'
            f'      Logout Efetuado!        \n'
            f'                              \n'
            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  ')
    time.sleep(2.2)

def notNull(resposta, msg):                 # Imprime "obrigatório" ao enviar input vazio
    while resposta == '':
        resposta = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                                f'       SAVE ⏇he Oceans         \n'
                                f'                                \n'
                                f'{msg}'
                                f'                                \n'
                                f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    return resposta

def loading():                              # Animação de carregamento entre transições de tela
    time.sleep(0.5)
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
          f'       SAVE ⏇he Oceans       \n'
          f'                              \n'
          f'          Loading...          \n'
          f'                              \n'
          f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(0.7)

def bemVindo():                             # Tela transitória após login validado
    time.sleep(0.5)
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
          f'       SAVE ⏇he Oceans       \n'
          f'                              \n'
          f' Bem-vindo, {historicoDeNomesLogados[-1]}\n'
          f'                              \n'
          f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(3.5)

def opcoesMenu(opcaoEscolhida, flag):       # Índice de menus: orquestra a troca entre telas
    # print(' Entrou opcoes menu')                                              #[DEBUG]
    # print(f' opcaoEscolhida ={opcaoEscolhida} {type(opcaoEscolhida)}')        #[DEBUG]
    if opcaoEscolhida == None: return
    loading()
    # print(f' opcaoEscolhida ={opcaoEscolhida} {type(opcaoEscolhida)}')        #[DEBUG]
    match flag:
        case 1:
            # print(' entrou flag = 1')                                         #[DEBUG]
            opcaoEscolhida += 10
        case 2:
            # print(' entrou flag = 2')                                         #[DEBUG]
            opcaoEscolhida += 20
        case 3:
            # print(' entrou flag = 3')                                         #[DEBUG]
            opcaoEscolhida += 210
        case 4:
            opcaoEscolhida += 2120
        case 5:
            opcaoEscolhida += 220
        case 6:
            opcaoEscolhida += 230
    # print(f' opcaoEscolhida ={opcaoEscolhida} {type(opcaoEscolhida)}')        #[DEBUG]
    match opcaoEscolhida:
        case 10:                                    # Menu inicial > <end>
            # print(' entrou case = 10')                                        #[DEBUG]
            print('\n\n\n\n\n Até a Próxima!')
            return  # Encerra o software
        case 11:
            # print(' entrou login')                                            #[DEBUG]
            loginRealizado = menuLogin()
            tryUserNotFoundOrLogin(loginRealizado)  # Menu inicial > Menu Logado
        case 12:
            # print(' entrou cadastro')                                         #[DEBUG]
            menuCadastro()                  # Menu inicial > Cadastro
            menuInicial()                   # Cadastro > Menu inicial
        case 20:
            logout()                        # Animação de logout
            menuInicial()                   # Menu logado > Menu inicial
        case 21:
            menuReport()                    # Menu logado > Menu de Denúncias
        case 210:
            menuLogado()                    # Menu de Denúncias > Menu inicial
        case 211:
            menuNovoReport()                # Menu de Denúncias > Menu Nova Denúncia
        case 212:
            menuLerReport()                 # Menu de Denúncias > Menu Ver Denúncias (global)
        case 2121:
            menuLerPorSigla()               # Menu Ver Denúncias (global) > Buscar por sigla
        case 2122:
            menuLerPorTipo()                # Menu Ver Denúncias (global) > Buscar por tipo
        case 2123:
            menuLerPorAntesDe()             # Menu Ver Denúncias (global) > Buscar por antes de tal data
        case 2124:
            menuLerPorDepoisDe()            # Menu Ver Denúncias (global) > Buscar por depois de tal data
        case 22:
            menuContribuir()                # Menu Logado > Menu Quero Contribuir
        case 220:
            menuLogado()                    # Menu Quero Contribuir > Menu Logado
        case 221:
            menuSouPF()                     # Menu Quero Contribuir > Menu Sou PF
        case 222:
            menuSouPJ()                     # Menu Quero Contribuir > Menu Sou PJ
        case 23:
            menuMeuPerfil()                 # Menu Logado > Menu Meu perfil
        case 230:
            menuLogado()                    # Menu Meu perfil > Menu Logado
        case 231:
            menuMeusDados()                 # Menu Meu perfil > Menu Meus Dados
        case 232:
            menuMinhasDenuncias()                 # Menu Meu perfil > Menu Minhas Denúncias
        case _:
            print("Opção não cadastrada")   # Caso de erro
    # print(' saiu do 2º switch case')                                          #[DEBUG]

def menuInicial():
    # print(' Entrou Menu inicial')
    resposta = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                            f'       SAVE ⏇he Oceans       \n'
                            f' Escolha:              0. ✖  \n'
                            f' 1. Login                     \n'
                            f' 2. Cadastro                  \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',codigoSubmenus[1][0],flag = 1)
    opcoesMenu(resposta,flag = 1)   # Recebe flag para fazer o handle change em opcoesMenu()

def menuLogin():                            # Tela de login
    user = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                        f'       SAVE ⏇he Oceans       \n'
                        f'                              \n'
                        f' Insira seu usuário:          \n'
                        f'                              \n'
                        f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    pw = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                      f'       SAVE ⏇he Oceans       \n'
                      f'                              \n'
                      f' Insira sua senha:            \n'
                      f'                              \n'
                      f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    acesso = tentaLogin(user,pw)           # Retorna True/False
    return acesso
    
def menuCadastro():                         # Cadastra novo usuário
    respNome = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Pede um nome
                            f'       SAVE ⏇he Oceans         \n'
                            f'                                \n'
                            f' Qual o seu nome?               \n'
                            f'                                \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿   ',[],'')
    respUser = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Pede um usuário
                            f'       SAVE ⏇he Oceans       \n'
                            f'                              \n'
                            f' Crie um usuário:             \n'
                            f'                              \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    respPw = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'       # Pede uma senha
                          f'       SAVE ⏇he Oceans       \n'
                          f'                              \n'
                          f' Crie uma senha:              \n'
                          f'                              \n'
                          f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    confPw = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                          f'       SAVE ⏇he Oceans       \n'
                          f'                              \n'
                          f' Confirme sua senha:          \n'
                          f'                              \n'
                          f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    while confPw != respPw:         # Se a confirmação não for igual, pede até ser igual
        confPw = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                              f'       SAVE ⏇he Oceans       \n'
                              f'                              \n'
                              f' \033[4mRepita\033[0m a senha:            \n'
                              f' {respPw}                     \n'
                              f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    novoCadastro = [respUser,respPw,respNome.title()]
    usuariosCadastrados.append(novoCadastro)    # Adiciona o cadastro na lista de contas cadastradas
    historicoDeNomesLogados.append(respNome.title())
    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  \n'
            f'      SAVE ⏇he Oceans          \n'
            f'                                \n'
            f'     Cadastro Realizado!        \n'
            f'    Bem-vindo, {respNome.title()}!      \n'
            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(2.2)
    
def menuLogado():
    resposta = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                            f'       SAVE ⏇he Oceans       \n'
                            f' 1. Denúncias                 \n'
                            f' 2. Quero fazer a diferença!  \n'
                            f' 3. Meu perfil     0. Logout  \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿  ',codigoSubmenus[4][0],2)
    opcoesMenu(resposta,flag = 2)

def menuReport():
    resposta = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                            f'       SAVE ⏇he Oceans       \n'
                            f' 1. Quero denunciar           \n'
                            f' 2. Ler ocorrências           \n'
                            f' 0. Voltar                    \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',codigoSubmenus[5][0],flag = 3)
    # print(f' resposta: {resposta} {type(resposta)}')
    opcoesMenu(resposta,flag = 3)

def listarTiposReports():                   # Lista os tipos pré-cadastrados possíveis de serem denunciados
    print          (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Lista tipos 1-3
                    f'       SAVE ⏇he Oceans         \n'
                    f'{tiposReport[0][0]}. {tiposReport[0][1]}\n'
                    f'{tiposReport[1][0]}. {tiposReport[1][1]}\n'
                    f'{tiposReport[2][0]}. {tiposReport[2][1]}\n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(5.5)
    print          (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Lista tipos 4-6
                    f'       SAVE ⏇he Oceans         \n'
                    f'{tiposReport[3][0]}. {tiposReport[3][1]}\n'
                    f'{tiposReport[4][0]}. {tiposReport[4][1]}\n'
                    f'{tiposReport[5][0]}. {tiposReport[5][1]}\n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')

def menuNovoReport():                       # Faz denúncia
    respEstado = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Pede o estado
                              f'       SAVE ⏇he Oceans         \n'
                              f'                                \n'
                              f' Em que estado ocorreu?         \n'
                              f' ex: SP                         \n'
                              f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    while not(naLista(listaSiglas,respEstado)):
        respEstado = repetirPedido(respEstado,listaSiglas)
    respCidade = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Pede a cidade
                              f'       SAVE ⏇he Oceans         \n'
                              f'                                \n'
                              f' Em qual cidade?                \n'
                              f'                                \n'
                              f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    respCidade = notNull(respCidade,' Em qual cidade? (Obrigatório)\n')           # Valida se vazio
    respLocal = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Pede o local
                             f'       SAVE ⏇he Oceans        \n'
                             f'                               \n'
                             f' E qual era o nome do lugar?   \n'
                             f'                               \n'
                             f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿   ',[],'')
    respLocal = notNull(respLocal,' E qual era o nome do lugar? (Obrigatório)\n') # Valida se vazio
    print          (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Pede o tipo
                    f'       SAVE ⏇he Oceans       \n'
                    f'                              \n'
                    f' Escolha um tipo a seguir:    \n'
                    f'                              \n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(3.5)
    listarTiposReports()
    respTipo = respostaUsuario('[-] Voltar | → ')
    while respTipo == '-':
        listarTiposReports()
        respTipo = respostaUsuario('[-] Voltar | → ')
    respTipo = validarOpcao(codigoSubmenus[8][0], respTipo)
    respData = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Pede a data
                            f'       SAVE ⏇he Oceans       \n'
                            f'                              \n'
                            f' Quando aconteceu?            \n'
                            f' ex: 01/01/2024               \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    respData = notNull(respData,' Quando aconteceu? (Obrigatório)\n')           # Valida se vazio
    time.sleep(1.2)
    print       (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                f'       SAVE ⏇he Oceans       \n'
                f'                              \n'
                f'          Obrigado!           \n'
                f' Sua denúncia fará a diferença!\n'
                f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(3.5)
    novoReport = [respEstado, respCidade, respLocal, respTipo, respData]
    allReports.append(novoReport)
    meusReports.append(novoReport)
    opcoesMenu(1,flag = 2)

def PegaOLabelDoTipoPeloNumero(num):              # A partir do número do tipo, pega a string associada a ele
    for tipo in tiposReport:    # Sublista: [num,label]
        if tipo[0] == num:      # Pinça qual sublista tem o número do tipo desejado
            return tipo[1]      # Da sublista, retorna o label

def triarReportPorSigla(filtroDigitado, indexSigla): # Busca denúncias pelo filtro de Tipo de denúncia, adicionando-as em uma lista
    denunciasFiltradas = []
    qnt = 0
    for i in range(len(allReports)):
        if allReports[i][indexSigla] == filtroDigitado:
            denunciasFiltradas.append(allReports[i])
            qnt += 1
    quantidadeFiltradas.append(qnt)
    return denunciasFiltradas

def triarReportPorTipo(filtroDigitado, indexTipo): # Busca denúncias pelo filtro de Tipo de denúncia, adicionando-as em uma lista
    denunciasFiltradas = []
    qnt = 0
    print(f'allreports = {allReports}')
    for i in range(len(allReports)):
        if allReports[i][indexTipo] == filtroDigitado:
            denunciasFiltradas.append(allReports[i])
            qnt += 1
    quantidadeFiltradas.append(qnt)
    return denunciasFiltradas

def triarReportPorAntesDe(filtroDigitado, indexData): # Busca denúncias pelo filtro de Tipo de denúncia, adicionando-as em uma lista
    print() # FIX!

def triarReportPorDepoisDe(filtroDigitado, indexData): # Busca denúncias pelo filtro de Tipo de denúncia, adicionando-as em uma lista
    print() # FIX!

def ImprimeReportsBuscados(d):
    for i in range(len(d)):
                    t = PegaOLabelDoTipoPeloNumero(d[i][3])
                    print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿ \n'
                          f'       SAVE ⏇he Oceans       \n'
                          f' {t}, {d[i][4]}\n'                 # meusReports = [Estado, Cidade, Local, Tipo, Data]
                          f' {d[i][2]}\n'
                          f' {d[i][0]} - {d[i][1]}    {i+1}/{quantidadeFiltradas[-1]}\n'
                          f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
                    time.sleep(3.5)


""" allReports =  [['PE','Ipojuca','Praia de Porto de Galinhas',1,'02/09/2019'],
                   ['RN','Tibau do Sul','Praia da Pipa',1,'10/09/2019'],
                   ['AL','Marechal Deodoro','Praia do Francês',1,'18/09/2019'],
                   ['PE','Ipojuca','Praia de Porto de Galinhas',1,'04/11/2019'],
                   ['AL','Roteiro','Praia do Gunga',1,'13/11/2019'],
                   ['AL','Roteiro','Praia do Gunga',1,'25/11/2019'],
                   ['RN','Natal','Praia de Miami',2,'07/04/2024'],
                   ['RJ','Rio de Janeiro','Praia de São Conrado',3,'30/01/2024'],
                   ['PE','Tamandaré','Praia de Carneiros',3,'08/04/2024'],
                   ['PB','João Pessoa','Hotel Nord Easy',3,'10/05/2024'],
                   ['PR','Porecatu','Rio Paranapanema',4,'01/06/2024'],
                   ['MS','Bonito','Rio Formoso',4,'03/06/2024'],
                   ['BA','São Francisco do Conde','Baía de Todos-os-Santos',5,'25/08/2023'],
                   ['BA','Ilha de Itaparica','Praia da Ponta do Mocambo',5,'18/12/2023'],
                   ['SP','Lucélia','Rio Aguapeí',6,'30/11/2023'],
                   ['RJ','Maricá','Litoral de Maricá',6,'28/02/2024'],
                   ['SP','Guarujá','Rio do Meio',6,'27/05/2024']
                   ] """

def casosFiltroBusca(filtroDigitado, tipoFiltro):           # Imprime as denúncias filtradas pelo filtro escolhido
    match tipoFiltro:
        case 'sigla':       # indice de Sigla em allReports: 0
            dEncontradas = triarReportPorSigla(filtroDigitado, indexSigla=0)    # Tria a lista de denúncias e retorna lista só com denúncias com o filtro
        case 'tipo':        # indice de Tipo em allReports: 3
            dEncontradas = triarReportPorTipo(filtroDigitado,indexTipo=3)
            ImprimeReportsBuscados(dEncontradas)
        case 'antesDe':     # indice de Data em allReports: 4
            dEncontradas = triarReportPorAntesDe(filtroDigitado, indexData=4)
        case 'depoisDe':    # indice de Data em allReports: 4
            dEncontradas = triarReportPorDepoisDe(filtroDigitado, indexData=4)

    # pedir filtro
    # cai no case daquele filtro
    # triar allReports buscando sublistas com aquele ou < ou > filtro
    # dá append nessa denuncia em uma lista
    # imprime essa lista[

"""  print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿ \n'
           f'       SAVE ⏇he Oceans        \n'
           f' Pesca com explosivos, 25/08/2023\n'
           f' Baía de Todos-os-Santos       \n'
           f' BA - São Francisco do Conde   \n'
           f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',) """

def menuLerReport(): #fix # Pede o filtro de busca
    print            (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                      f'       SAVE ⏇he Oceans       \n'
                      f'                              \n'
                      f' Escolha um filtro a seguir:  \n'
                      f'                              \n'
                      f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(3.5)
    respFiltro = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿ \n'      # Lista os filtros
                              f'       SAVE ⏇he Oceans        \n'
                              f' 1. Por Sigla                  \n'
                              f' 2. Por Tipo                   \n'
                              f' 3. Antes de.. 4. Depois de..\n'
                              f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',codigoSubmenus[9][0],flag = 4)
    opcoesMenu(respFiltro,flag = 4)

def menuLerPorSigla():
    respFiltro = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿ \n'      # Lista os filtros
                              f'       SAVE ⏇he Oceans        \n'
                              f'                               \n'
                              f' Digite a sigla desejada:      \n'
                              f'                               \n'
                              f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',listaSiglas,'')
    time.sleep(3.5)
    casosFiltroBusca(respFiltro, tipoFiltro='sigla')
    menuReport()
    
def menuLerPorTipo(): #fix
    print          (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'     # Pede o tipo
                    f'       SAVE ⏇he Oceans     \n'
                    f'                            \n'
                    f' Escolha um tipo a seguir:  \n'
                    f'                            \n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(3.5)
    listarTiposReports()
    respTipo = respostaUsuario('[-] Voltar | → ')
    while respTipo == '-':
        listarTiposReports()
        respTipo = respostaUsuario('[-] Voltar | → ')
    respTipo = validarOpcao(codigoSubmenus[8][0], respTipo)
    casosFiltroBusca(respTipo, tipoFiltro='tipo')
    menuReport()
    
def menuLerPorAntesDe(): #fix
    print('Entrou menuLerPorAntesDe')
    menuReport()
    
def menuLerPorDepoisDe(): #fix
    print('Entrou menuLerPorDepoisDe')
    menuReport()
    
def menuContribuir():
    resposta = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                            f'       SAVE ⏇he Oceans       \n'
                            f' 1. Sou uma pessoa            \n'
                            f' 2. Represento uma Empresa    \n'
                            f' 0. Voltar                    \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',codigoSubmenus[7][0],flag = 5)
    opcoesMenu(resposta,flag = 5)
    
def menuSouPF():                            # Fornece link de ONG 
    print          (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                    f'       SAVE ⏇he Oceans       \n'
                    f'      Seja \033[4mVoluntário\033[0m:       \n'
                    f'   Faça parte da luta por    \n'
                    f'      um \033[4mmundo melhor\033[0m!       \n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(5.5)
    print          (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                    f'       SAVE ⏇he Oceans       \n'
                    f' Para mais informações, acesse:\n'
                    f' https://parceirosdomar.org/  \n'
                    f'   Seja um \033[4mParceiro do Mar!\033[0m   \n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(5.5)
    menuLogado()
    
def menuSouPJ():                            # Pede dados da empresa para fazer parceria (apenas visual)
    print          (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                    f'       SAVE ⏇he Oceans       \n'
                    f'  Sua empresa quer construir  \n'
                    f'      um mundo melhor?        \n'
                    f'    \033[4mSeja nosso parceiro\033[0m!      \n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(5.5)
    resposta = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                            f'       SAVE ⏇he Oceans       \n'
                            f' \033[4mFormulário de Parceria\033[0m:      \n'
                            f' 1. Nome da empresa?          \n'
                            f'                              \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    resposta = notNull(resposta,' 1. Nome da empresa? (obrigatório)\n')           # Valida se vazio
    imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                 f'       SAVE ⏇he Oceans       \n'
                 f' \033[4mFormulário de Parceria\033[0m:      \n'
                 f' 2. Setor de mercado?         \n'
                 f'                              \n'
                 f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    resposta = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                            f'       SAVE ⏇he Oceans       \n'
                            f' \033[4mFormulário de Parceria\033[0m:      \n'
                            f' 3. Contato? (email/fone)     \n'
                            f'                              \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',[],'')
    resposta = notNull(resposta,' 3. Contato? (obrigatório)\n')           # Valida se vazio
    time.sleep(0.7)
    print          (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                    f'       SAVE ⏇he Oceans       \n'
                    f'                              \n'
                    f'    \033[4mFormulário recebido!\033[0m      \n'
                    f'        Agradecemos!          \n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(5.5)         # Dados: são descartados ao término do formulário
    menuLogado()
    
def menuMeuPerfil():
    resposta = imprimirMenu(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                            f'       SAVE ⏇he Oceans       \n'
                            f' 1. Meus dados                \n'
                            f' 2. Minhas denúncias          \n'
                            f' 0. Voltar                    \n'
                            f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿',codigoSubmenus[6][0],flag = 6)
    opcoesMenu(resposta,flag = 6)
    
def menuMeusDados():                        # Imprime os dados cadastrais do usuário
    print          (f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿\n'
                    f'       SAVE ⏇he Oceans       \n'
                    f' Nome: {historicoDeNomesLogados[-1]}\n'
                    f' Usuário: {historicoUserSenhaLogados[-1][0]}\n'
                    f' Senha: {historicoUserSenhaLogados[-1][1]}\n'
                    f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
    time.sleep(5.5)
    menuMeuPerfil()
    
def menuMinhasDenuncias():                  # Lista as denúncias que o usuário fez
    if meusReports == []:                               # Caso 1: Ainda não fez denúncias
        print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿ \n'
               f'       SAVE ⏇he Oceans       \n'
               f'   Você ainda não fez uma     \n'
               f' denúncia. Fique à vontade    \n'
               f'  para contribuir conosco!    \n'
               f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
        time.sleep(5.5)
    else:
        for r in meusReports:                           # Caso 2: Denunciou, lista ela(s)
            for t in tiposReport:
                if r[3] == t[0]:
                    tempTipo = t[1]
            print(f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿ \n'
                   f'       SAVE ⏇he Oceans       \n'
                   f' {tempTipo}, {r[4]}\n'                 # meusReports = [Estado, Cidade, Local, Tipo, Data]
                   f' {r[2]}\n'
                   f' {r[0]} - {r[1]}\n'
                   f'~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿~∿')
            time.sleep(5.5)
    menuMeuPerfil()

# ==============================================================================================================================================
# Listas/Dicionários Pré-Cadastrados:

# Para cada menu disponível foi atribuído um número, acessado via flag em codigoSubmenus na função opcoesMenu() ao somar com a opção escolhida na tela:
"""
[1          ,11       ,12          ,20        ,21         ,211       ,212       ,2121       ,2122      ,2123          ,2124          ,22            ,221    ,222    ,23        ,231            ,2311           ,2312           ,2313           ,232]
['m_inicial','m_login','m_cadastro','m_logado','m_reports','_cReport','_rReport','por_sigla','por_tipo','por_data_ant','por_data_dep','m_contribuir','_m_pf','_m_pj','m_perfil','_m_MeusReport','__rMeusReport','__uMeusReport','__dMeusReport','_m_InfoLogin',] """

# E cada menu tem seus submenus, declarados no dicionário abaixo:
codigoSubmenus = {1:[[1,2,0],['m_login(2)','m_cadastro(3)','fechar']],
                   4:[[1,2,3,0],['m_reports(5)','m_perfil(6)','m_contribuir(7)','sair']],
                   5:[[1,2,0],['_cReport(8)','_rReport(9)','voltar']],
                   6:[[1,2,0],['_m_MeusReport(10)','_m_InfoLogin(11)','voltar']],
                   7:[[1,2,0],['_m_pf(12)','_m_pj(13)','voltar']],
                   8:[[1,2,3,4,5,6],[]],
                   9:[[1,2,3,4],['por_sigla','por_tipo','por_data_ant','por_data_dep']],
                   10:[[1,2,3,0],['__rMeusReport(14)','__uMeusReport(15)','__dMeusReport(16)','voltar']]
                   }
# Legenda:
# flag do menu:[[nº das opcoes],[textos das opcoes(flag)]]

# Lista de usuários Cadastrados: [['user','password']]
usuariosCadastrados = [['admin','admin','Administrador']]

# Lista de últimos logins, recebe novos
historicoUserSenhaLogados = []

# Lista de últimos nomes dos logins, recebe novos
historicoDeNomesLogados = ['Administrador']

# Lista de Tipos de Report
tiposReport = [[1,'Mancha de óleo'],
               [2,'Lixo em praia'],
               [3,'Esgoto no mar'],
               [4,'Pesca ilegal'],
               [5,'Pesca com explosivos'],
               [6,'Pesca de arrasto']]

# Lista de Reports já cadastrados
allReports =  [['PE','Ipojuca','Praia de Porto de Galinhas',1,'02/09/2019'],
               ['RN','Tibau do Sul','Praia da Pipa',1,'10/09/2019'],
               ['AL','Marechal Deodoro','Praia do Francês',1,'18/09/2019'],
               ['PE','Ipojuca','Praia de Porto de Galinhas',1,'04/11/2019'],
               ['AL','Roteiro','Praia do Gunga',1,'13/11/2019'],
               ['AL','Roteiro','Praia do Gunga',1,'25/11/2019'],
               ['RN','Natal','Praia de Miami',2,'07/04/2024'],
               ['RJ','Rio de Janeiro','Praia de São Conrado',3,'30/01/2024'],
               ['PE','Tamandaré','Praia de Carneiros',3,'08/04/2024'],
               ['PB','João Pessoa','Hotel Nord Easy',3,'10/05/2024'],
               ['PR','Porecatu','Rio Paranapanema',4,'01/06/2024'],
               ['MS','Bonito','Rio Formoso',4,'03/06/2024'],
               ['BA','São Francisco do Conde','Baía de Todos-os-Santos',5,'25/08/2023'],
               ['BA','Ilha de Itaparica','Praia da Ponta do Mocambo',5,'18/12/2023'],
               ['SP','Lucélia','Rio Aguapeí',6,'30/11/2023'],
               ['RJ','Maricá','Litoral de Maricá',6,'28/02/2024'],
               ['SP','Guarujá','Rio do Meio',6,'27/05/2024']
               ]
meusReports = []        # "Minhas Denúncias", começa vazio
quantidadeFiltradas = []# Pega o total de denúncias filtradas, variável global modificada ao realizar uma busca

listaSiglas = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO',
               'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go', 'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'sp', 'se', 'to',
               'Ac', 'Al', 'Ap', 'Am', 'Ba', 'Ce', 'Df', 'Es', 'Go', 'Ma', 'Mt', 'Ms', 'Mg', 'Pa', 'Pb', 'Pr', 'Pe', 'Pi', 'Rj', 'Rn', 'Rs', 'Ro', 'Rr', 'Sc', 'Sp', 'Se', 'To']

# ==============================================================================================================================================
# Código executado:

init()
menuInicial()