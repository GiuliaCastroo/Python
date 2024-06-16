'''
2) Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro
quadrado, deve-se usar 18W de potência. Elaborar um programa que receba as duas dimensões
de um cômodo (em metros). Calcule e mostre a sua área (em m2
) e a potência de iluminação que
deverá ser utilizada.

'''
largura = float(input("Digite largura em metros: "))
comprimento = float(input("Digite comprimento em metros: "))
area = largura * comprimento 
potencia = area * 18

print("A área em metros quadrado é: ", area)
print("A potência de iluminação necessária é: ", potencia)