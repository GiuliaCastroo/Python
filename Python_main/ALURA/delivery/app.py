import os

restaurantes = [
    {"nome": "Praça", "categoria": "Japonesa", "ativo": False},
    {"nome": "Pizzaria são josé", "categoria": "Pizza", "ativo": True},
    {"nome": "Cantina", "categoria": "Italiana", "ativo": False},
]


def exibir_nome_do_programa():
    print(
        """
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
"""
    )


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")


def finalizar_app():
    exibir_subtitulo("Finalizando o app")


def voltar_menu():
    input("\nDigite uma tecla para voltar ao menu principal.")
    main()


def exibir_subtitulo(texto):
    os.system("cls")
    linha= '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    os.system("cls")
    exibir_subtitulo("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar:")
    categoria = input(f"Digite a categoria do {nome_do_restaurante}: ")
    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria,
        "ativo": False,
    }
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_menu()


def listar_restaurantes():
    os.system("cls")
    exibir_subtitulo("Listando restaurantes cadastrados\n")
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo_restaurante = 'ativado' if restaurante["ativo"] else 'desativado'
        print(f"-{nome_restaurante} | {categoria_restaurante} | {ativo_restaurante}")

    voltar_menu()


def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
                                                  
        
    voltar_menu()


def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))

    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        alternar_estado_restaurante()
    else:
        finalizar_app()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
