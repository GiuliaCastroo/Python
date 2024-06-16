'''6) Elaborar um programa que leia um número inteiro e mostre se o número é divisível por 2 e por
3 ou se é divisível por 5 ou por 7.'''
 
numero = int(input("Digite um número inteiro: "))

if (numero % 2 == 0 and numero % 3 == 0):
    print(f"O número {numero} é divisível por 2 e por 3.")
else:
    (numero % 5 == 0 or numero % 7 == 0)
    print(f"O número {numero} é divisível por 5 ou por 7.")