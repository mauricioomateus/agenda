AGENDA = {}

AGENDA['joao'] = {
    'telefone': '91111-1111',
    'email': 'joao@google.com',
    'end': 'Travessa neide',
}

AGENDA['maria'] = {
    'telefone': '95555-5555',
    'email': 'maria@google.com',
    'end': 'Manoel cabeceira',
}

AGENDA['dog'] = {
    'telefone': '99999-9999',
    'email': 'dog@google.com',
    'end': 'Rua Brasil',
}

def mostrar_contatos():
    for contato in AGENDA:
        buscar_contato(contato)
        print('---------------')

def buscar_contato(contato):
    try:
        print("Nome: " + contato)
        print("Telefone: ", AGENDA[contato]['telefone'])
        print("E-mail: ", AGENDA[contato]['email'])
        print("Endereco: ", AGENDA[contato]['end'])
    except:
        print("Contato nao existe no banco de dados!")

def incluir_editar_contato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        'telefone': telefone,
        'email': email,
        'end': endereco,
    }
    print("Contato adicionado comsucesso!")

def excluir_contato(contato):
    AGENDA.pop(contato)
    print(">>>> Contato {} excluirdo com sucesso".format(contato))

def menu():
    print("1 - Mostrar todos os contatos")
    print("2 - Buscar contato")
    print("3 - Incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("0 - Fechar agenda")

    opcao = input("Escolha uma opcao.: ")

    if opcao == "1":
        mostrar_contatos()
    elif opcao == "2":
        contato = input("Digite o nome do contato.: ")
        buscar_contato(contato)
    elif opcao == "3" or opcao == "4":
        nome = input("Insira o nome: ")
        telefone = input("Digite o telefone: ")
        endereco = input("Digite o endereco: ")
        email = input("Digite o email: ")
        incluir_editar_contato(nome, telefone, email, endereco)
        mostrar_contatos()
    elif opcao == "5":
        contato = input("Digite o nome do contato.: ")
        excluir_contato()
    elif opcao == "0":
        print("Fechando programa.")
        exit()
    else:
        print("Opcao invalida!")
    
if __name__ == '__main__':
    menu()
    #buscar_contato('joao')