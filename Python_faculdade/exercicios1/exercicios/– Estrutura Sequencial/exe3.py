"""
3) Elaborar um programa que receba o salário de um funcionário e o percentual de aumento, calcule
e mostre o valor do aumento e o novo salário.
"""

sal = float (input("Digite seu salário: "))
percentual  = float (input("Digite o percentual de aumento: "))

aumento = sal * (percentual/ 100)
nv_sal = sal + aumento

print("O valor do aumento é: ", aumento)
print("Seu salário com o percentual de aumento é: ", nv_sal)