AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print(">>>> Agenda vazia")
        print()

def buscar_contato(contato):
    try:
        print("Nome: ", contato)
        print("Telefone: ", AGENDA[contato]['telefone'])
        print("E-mail: ", AGENDA[contato]['email'])
        print("Endereco: ", AGENDA[contato]['end'])
        print("-----------------------------------------")
    except KeyError:
        print("\nContato nao existe no banco de dados! \n")

def detalhes_contato():
    telefone = input("Digite o telefone: ")
    endereco = input("Digite o endereco: ")
    email = input("Digite o email: ")
    return telefone, endereco, email

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'end': endereco,
    }
    salvar()
    print()
    print("[+][+] Contato adicionado com sucesso!")
    print()
    
def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print(">>>> Contato {} excluido com sucesso".format(contato))
        print()
    except KeyError as e:
        print("Erro ao excluir. Contato inexistente!")
        print("Codigo do erro: " + e)

def importar_contatos(file_name):
    try:
        with open(file_name, 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = print(linha.strip().split(',')) #dividir string em listas e separados por virgula
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print("[!] Arquivo nao encontrado [!]")   
        print()     
    except Exception as e:
        print(">>>> Algum erro inesperado ocorreu: {}".format(e))    
        print()

def exportar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo+".csv", 'w') as file:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['end']
                file.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print('\n[+] Agenda exportada com sucesso')
        print()
    except Exception as error:        
        print(">>>> Ocorreu um erro ao exportar contatos, {}".format(error))
        print()

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as file:
            linhas = file.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',') #dividir string em listas e separados por virgula
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                   'telefone': telefone,
                   'email': email,
                   'end': endereco,
                }
        print('[+] Database carregado com sucesso!\n')
        print('[+] {} contatos carregados\n'.format(len(AGENDA)))
    except FileNotFoundError:
        print("[!] Arquivo nao encontrado [!]")   
        print()     
    except Exception as e:
        print(">>>> Algum erro inesperado ocorreu: {}".format(e))    
        print()

def menu():
    carregar()
    while True:
        print("###################################")
        print("1 - Mostrar todos os contatos")
        print("2 - Buscar contato")
        print("3 - Incluir contato")
        print("4 - Editar contato")
        print("5 - Excluir contato")
        print("6 - Exportar contatos para CSV")
        print("7 - Importar arquivo CSV")
        print("0 - Fechar agenda")
        print("###################################")

        opcao = input("Escolha uma opcao.: ")

        if opcao == "1":
            mostrar_contatos()
        elif opcao == "2":
            contato = input("Digite o nome do contato.: ")
            buscar_contato(contato)
        elif opcao == "3":
            nome = input("Insira o contato: ")
            try:
                AGENDA[nome]
                print("[+][!] Contato já existe\n")
            except:
                telefone, email, endereco = detalhes_contato() #captura os dados retornados da funcao
                incluir_editar_contato(nome, telefone, email, endereco)
        elif opcao == '4':
            nome = input("Insira o contato: ")
            try:
                AGENDA[nome]
                print(">>>> Edidando contato ", nome)
                telefone, email, endereco = detalhes_contato() #captura os dados retornados da funcao
                incluir_editar_contato(nome, telefone, email, endereco)
            except:
                print("[+][!!] Contato inexistente no banco de dados. ")
        elif opcao == "5":
            contato = input("Digite o nome do contato.: ")
            excluir_contato(contato)
        elif opcao == "6":
            arquivo = input("Digite o nome do arquivo a ser exportado (sem a extensao): ")
            exportar_contatos(arquivo)
        elif opcao == "7":
            arquivo = input("Digite o nome do arquivo a ser importado: ")
            importar_contatos(arquivo)
        elif opcao == "0":
            print(">>> Fechando programa.")
            exit()
        else:
            print(">>> Opcao invalida!")
    
if __name__ == '__main__':
    menu()
    #buscar_contato('joao')
