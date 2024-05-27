"""
2) Elaborar um programa que leia o saldo de uma aplicação e imprimir o novo saldo, considerando
um reajuste de 15%.
"""
sal= float(input("Digite seu salário: "))

reajuste = sal * 0.15
sal = sal + reajuste

print("Seu salário com reajuste é: " , sal)