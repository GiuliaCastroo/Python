import os

nome = []
email = []
curso = []

arquivo = open('cadastro_aluno.tx', 'a')

def exibir_nome_do_programa():
    print("Cadastro de Alunos!!!")


def exibir_opcoes():
    print('1. Cadastrar')
    print('2. Listar')
    print('3. Buscar')
    print('4. Deletar')
    print('5. "Deseja continuar executando o programa?[S/N]')


def finalizar_app():
    print('Finalizando Aplicativo')
    

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastro():
    exibir_subtitulo('Cadastro de alunos')
    cadastro_aluno = input('Digite seu nome')
    nome.append(cadastro_aluno)
    print(f'O cadastro do aluno {cadastro_aluno} foi cadastrado com sucesso!')
    email_aluno = input('Digite seu e-mail')
    email.append(email_aluno)
    cadastro_curso = input('Digite seu curso')
    curso.append(cadastro_curso)
    arquivo.write(nome , email , curso)
    arquivo.close()
    voltar_ao_menu_principal()
    
     
def listar():
     arquivo = open("cadastro_aluno.txt" , "r")
     conteudo = arquivo.read()
     print(conteudo)
     arquivo.close()


def busca():
     busca = str
     busca = input("Digite o nome")



def escolher_opcao():
        sair = str
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastro()
        elif opcao_escolhida == 2: 
             print('2. Listar')
        elif opcao_escolhida == 3: 
              print('3. Buscar')
        elif opcao_escolhida == 4: 
             print('4. Deletar')
        else: 
           if sair == 's' or sair == 'S':
                 exibir_opcoes
           else: 
              print(finalizar_app)
    

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

