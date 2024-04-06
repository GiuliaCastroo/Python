'''
7) Elaborar um programa que receba o peso de uma pessoa em quilos. Calcule e mostre:
a. O novo peso se a pessoa engordar 15% sobre o peso digitado;
b. O novo peso se a pessoa emagrecer 20% sobre o peso digitado
'''

pesoQ = float (input("Digite seu peso em quilos: "))

#engorda
pesoEngorda = pesoQ *15/100
pesoEngorda = pesoQ + pesoEngorda

#emagrece
pesoEmagrece = pesoQ *20/100
pesoEmagrece = pesoQ - pesoEmagrece

print ("Se você engordar 15% do seu peso ficará com: ",pesoEngorda)
print ("Se você emagrecer 20% do seu peso ficará com: ",pesoEmagrece)