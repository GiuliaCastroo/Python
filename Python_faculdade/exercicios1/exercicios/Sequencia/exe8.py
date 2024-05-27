"""
8) Elaborar um algoritmo que leia a idade de
 uma pessoa expressa em anos, meses e dias e mostrea expressa apenas em dias.
"""

anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))

total_dias = anos * 365 + meses * 30 + dias

print("A idade expressa apenas em dias é:", total_dias)