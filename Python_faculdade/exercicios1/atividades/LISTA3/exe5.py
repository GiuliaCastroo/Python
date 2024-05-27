'''5) Elaborar um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso
ideal, utilizando as seguintes formulas (onde h corresponde a altura):
• Homens: (72.7 ∗ h) 58
• Mulheres: (62, 1 ∗ h) − 44, 7'''

h = float (input("Digite sua altura: "))
sexo= str(input("Digite seu sexo. Digite F para feminino, e M para masculino: "))

if sexo == 'F':
    mulher = (62.1 * h )- 44.7
    print ("Seu peso ideal é : " , mulher)
else:
    homem = (72.7 * h) - 58
    print("Seu peso ideal é : " , homem)