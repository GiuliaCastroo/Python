import os

def menu():
    print("Menu do sistema")
    print("1 - Cadastrar um novo aluno")
    print("2 - Listar todos os alunos cadastrados")
    print("3 - Buscar um aluno cadastrado")
    print("4 - Excluir um aluno cadastrado")

def cadastrar():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o email do aluno: ")
    curso = input("Digite o curso do aluno: ")
    
    with open("cadastro_aluno.txt", "a") as file:
        file.write(nome + "," + email + "," + curso + "\n")
    
    print("Aluno cadastrado com sucesso!")

def listar():
    if not os.path.exists("cadastro_aluno.txt"):
        print("Nenhum aluno cadastrado.")
        return

    with open("cadastro_aluno.txt", "r") as file:
        alunos = file.readlines()
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            nome, email, curso = aluno.strip().split(",")
            print(f"Nome: {nome}, Email: {email}, Curso: {curso}")

def buscar():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ")

    if not os.path.exists("cadastro_aluno.txt"):
        print("Nenhum aluno cadastrado.")
        return

    with open("cadastro_aluno.txt", "r") as file:
        alunos = file.readlines()
    
    for aluno in alunos:
        nome, email, curso = aluno.strip().split(",")
        if nome.lower() == nome_busca.lower():
            print(f"Nome: {nome}, Email: {email}, Curso: {curso}")
            return
    
    print("Aluno não encontrado!")

def excluir():
    nome_excluir = input("Digite o nome do aluno que deseja excluir: ")

    if not os.path.exists("cadastro_aluno.txt"):
        print("Nenhum aluno cadastrado.")
        return

    with open("cadastro_aluno.txt", "r") as file:
        alunos = file.readlines()
    
    encontrado = False
    with open("cadastro_aluno.txt", "w") as file:
        for aluno in alunos:
            nome, email, curso = aluno.strip().split(",")
            if nome.lower() != nome_excluir.lower():
                file.write(nome + "," + email + "," + curso + "\n")
            else:
                encontrado = True
    
    if encontrado:
        print("Aluno excluído com sucesso!")
    else:
        print("Aluno não encontrado!")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            buscar()
        elif opcao == '4':
            excluir()
        else:
            print("Opção inválida. Tente novamente.")
            continue
        
        continuar = input("Deseja continuar executando o programa? [S/N]: ").strip().upper()
        if continuar == 'N':
            break

if __name__ == "__main__":
    main()