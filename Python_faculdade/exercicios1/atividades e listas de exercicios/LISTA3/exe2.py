'''2) Elaborar um programa que leia o salário de um funcionário e o valor da prestação de um
empréstimo. Se a prestação for maior que 20% do salário mostre a mensagem: Empréstimo não
concedido, caso contrario mostre a mensagem: ́Empréstimo concedido.
'''
salario = float(input("Digite o salário do funcionário: "))
prestacao = float(input("Digite o valor da prestação do empréstimo: "))

limite_prestacao = 0.2 * salario

if prestacao > limite_prestacao:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")
