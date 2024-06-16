"""
2) Elaborar um algoritmo que calcule a aceleração de um corpo em movimento conhecendo-se as
velocidades inicial e final, e o intervalo de tempo medido (a = (v2 –v1)/∆t). Exibir o resultado.
"""

vel_incial = float(input("Digite a velocidade inicial: "))
vel_final = float (input("Digite a velocidade final: "))
inter_tempo = float(input("Digite o intervalo de tempo: "))

aceleracao = (vel_final - vel_incial) / inter_tempo

print("A acerelação é igual: " , aceleracao)