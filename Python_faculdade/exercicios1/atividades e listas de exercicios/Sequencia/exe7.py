"""
7) Elaborar um algoritmo que leia 3 notas de um aluno e calcule a média final deste aluno.
Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente.
"""
n1 = int (input("insira sua nota 1: "))
n2 = int (input("insira sua nota 2: "))
n3 = int (input("insira sua nota 3: "))

peso_n1 = 2
peso_n2 = 3
peso_n3 = 5

media_ponderada = (n1 * peso_n1 + n2 * peso_n2 + n3 * peso_n3) / (peso_n1 + peso_n2 + peso_n3)

print("Sua média ponderada é:", media_ponderada)