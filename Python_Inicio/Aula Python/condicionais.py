#Estruturas de controle de Fluxo (Condicionais)#

#If / Else#


idade =18

if idade >= 18: 
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')



#Estrutura de média - Imprimir Aprovado média >= 7 é Reprovado <7.#

# Minha versão#

"""
nota1 = float (input('Insira a nota 1 : '))
nota2 = float (input('Insira a nota 2 :  ' ))
nota3 = float (input('Insira a nota 3 :  ' ))
nota4 = float (input('Insira a nota 4 :  ' ))

media = nota1 + nota2 + nota3+ nota4 / 4

if media >=7:
    print('Parabéns! você foi aprovado')
else:
    print('Infelimente você foi reprovado.')
"""


#Versão Instrutor#

"""
media = float (input('Informe a média do estudante: '))

if media >=7:
  print('Aprovado')
elif media >=5:                  #No python o else if é ELIF
    print ('Recuperação')
else:
    print('Reprovado')
"""


    #Exemplo 2

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado')
else:
    print('Reprovado')