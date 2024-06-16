"""
10) Elaborar um algoritmo que calcule o salário líquido de um funcionário, considerado:
a) os dados do funcionário: nome, RG e telefone.
b) salário bruto de R$ 2500,00
c) descontos de R$ 300,00
Exibir o nome, telefone e o salário líquido.
"""
nome = str (input("Digite seu nome "))
rg = int (input("Digite seu RG "))
tel= int (input("Digite seu Telefone "))

sal = 2500 -300

print("Seu nome é: ", nome , ",seu telefone é: ", tel, ",e o seu salário liquido é " ,sal)