"""
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, 
ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado

Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.s
"""

nota1 = int(input("Insira a N1: "))
nota2 =int(input("Insira a N2: "))
nota3 =int(input("Insira a N3: "))
media_final = (nota1 + nota2 + nota3) / 3

if media_final >= 7:
    print("Aprovado")
elif media_final >= 5:
    print("Recuperação")
else:
    print("Reprovado")
