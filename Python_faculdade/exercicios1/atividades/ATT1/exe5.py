'''
5) Elaborar um programa que receba o salário-base de um funcionário. Calcule e imprima o salário
a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além
disso, ele paga 7% de imposto sobre o salário-base.
'''

salBase =float (input("Digite seu salário base: "))
gratificacao = salBase * 5/100
salBase = salBase + gratificacao

imposto = salBase * 7 /100
salBase = salBase - imposto



print ("Seu salário a receber é: ",salBase)