""""Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

"""

produto1 = float(input("Digite a quantidade do produto 1: "))
produto2 = float(input("Digite a quantidade do produto 2: "))
if produto1>produto2 :
    print("O Produto 1 foi mais vendido que o 2")
elif produto1<produto2:
     print("O Produto 2 foi mais vendido que o 1")
elif produto1==produto2: 
    print("EMPATE")



"""macas = int(input("Digite a quantidade de maçãs vendidas: "))
bananas = int(input("Digite a quantidade de bananas vendidas: "))

if macas > bananas:
    print("As maçãs tiveram mais vendas.")
elif bananas > macas:
    print("As bananas tiveram mais vendas.")
else:
    print("As vendas foram iguais.") --> Código do instrutor"""