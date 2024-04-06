'''
4) Elaborar um programa para auxiliar vendedores. O programa deve receber o valor total de uma
compra e deve calcular e exibir: valor à vista (total a pagar com desconto de 10%) e o valor de cada
parcela (parcelamento de 3x sem juros)
'''

valorTotal = float (input("Digite o valor total da sua compra: "))
valoraVista = valorTotal * 10 /100
valorDesconto = valorTotal - valoraVista
valorParcela = valorDesconto /3 


print ("O Valor da primeira parcela será: " , valorParcela)
print ("O Valor da Segunda parcela será: " , valorParcela)
print ("O Valor da Ultima parcela será: " , valorParcela)
