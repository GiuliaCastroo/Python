"""
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. 
O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

"""

renda = float(input("Informe sua renda mensal: R$ "))
parcela = float(input("Informe o valor da parcela desejada: R$ "))

limite = renda * 0.3  

if renda > 2000 and parcela <= limite:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado.")
