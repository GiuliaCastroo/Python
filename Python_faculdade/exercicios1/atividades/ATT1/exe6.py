'''
6) Elaborar um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor. O
programa deve também exibir a soma do sucessor de seu triplo com o antecessor de seu dobro.

'''

numInteiro = int (input("Digite um número inteiro: "))
sucessor = numInteiro + 1
antecessor = numInteiro -1 

sucTriplo = sucessor * 3
antDobro = antecessor * 2
somaTudo = (sucTriplo + antDobro)

print ("O Sucessor do numéro é: ",sucessor)
print ("O antecessor do numéro é: ",antecessor)
print ("A soma do sucessor de seu triplo com o antecessor de seu dobro é: ",somaTudo)