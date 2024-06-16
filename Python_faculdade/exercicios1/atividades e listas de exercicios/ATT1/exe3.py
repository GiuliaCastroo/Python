'''
3) Um funcionário recebeu seu salário e precisa pagar duas contas que estão atrasadas. Como as
contas estão atrasadas, ele terá que pagar multa de 2% sobre cada conta. Elaborar um programa
que calcule e mostre quanto restará do salário do funcionário.

'''

salario = float(input("Digite o salario: "))
conta1 = float(input("Digite o valor da conta 1: "))
conta2 = float(input("Digite o valor da conta 2: "))
multa1 = conta1 + 0.02
multa2 = conta2 + 0.02
restante = salario - multa1 - multa2

print("O valor restante do seu salário é: ", restante)
