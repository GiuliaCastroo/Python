# Credenciais corretas pré-definidas
nome_correto = "admin"
senha_correta = "senha123"

# Solicita entrada do usuário
nome_digitado = input("Digite seu nome de usuário: ")
senha_digitada = input("Digite sua senha: ")

# Valida as credenciais
if nome_digitado == nome_correto and senha_digitada == senha_correta:
    print("Bem-vindo! Login realizado com sucesso.")
else:
    print("Seu login ou senha está incorreto.")