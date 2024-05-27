'''1) Elaborar um programa que leia dois números e mostre o maior deles, assim como a diferença
existente entre ambos.'''

x = float (input("Digite um número: "))
y= float (input("Digite um número: "))

if x > y :
    maior_x = x - y
    print("O maior número digitado é: ", x , "E a difrença de valores é : ",maior_x)
   
else:
    maior_y = y - x
    print("O maior número digitado é: ", y , "E a difrença de valores é : ",maior_y)

