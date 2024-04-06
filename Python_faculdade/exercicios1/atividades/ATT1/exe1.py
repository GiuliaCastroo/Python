'''
1) Elaborar um programa que realize a divisão de um prêmio que será dividido entre três
ganhadores de um concurso. Após o programa receber o valor do prêmio, deve calcular e exibir o
valor que cada ganhador receberá. O primeiro ganhador receberá 47%, o segundo receberá 34%
e o terceiro receberá o restante.

'''

premio = float(input("Digite o valor do premio: "))
ganhador1 = 47/100 * premio
ganhador2 = 34/100 * premio
ganhador3 = 19/100 * premio

print("O valor do premio do primeiro ganhador é: ", ganhador1)
print("O valor do premio do segundo ganhador é: ", ganhador2)
print("O valor do premio do terceiro ganhador é: ", ganhador3)