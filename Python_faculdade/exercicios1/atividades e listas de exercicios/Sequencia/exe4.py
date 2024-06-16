"""
4) Elaborar um algoritmo que receba o raio e a altura de uma lata de óleo para calcular e apresentar
o valor do volume desta lata, dado: V = π*r2*h.
"""

raio = float (input("Digite o raio: "))
altura = float (input("Digite a altura: "))

valor_volume = 3,14* (raio ** 2)* altura

print("O valor do volume: " , valor_volume)