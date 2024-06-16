'''4) Elaborar um programa que leia um número. Se o número for positivo, o programa deve calcular
e mostrar a raiz quadrada do número. Se o número for negativo, o programa deve mostrar a
seguinte mensagem: o número é inválido.'''

import math

num = float (input("Digite um número: "))

if num > 0:
    raiz = math.sqrt(num)
    print("A raiz quadrada do número é: ", raiz)
else:
    print("Número Inválido")