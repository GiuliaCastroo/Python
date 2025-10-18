"""
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
"""

despesas_realizadas =float(input("Insira as despesas realizadas: "))
if despesas_realizadas >= 3000:
    print ("Você gastou mais de 3.000,00")
else:
    print(f"Você está dentro do orçameto Total gasto de : {despesas_realizadas} de 3.000,00") 