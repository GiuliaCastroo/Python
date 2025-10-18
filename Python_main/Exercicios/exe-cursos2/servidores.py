"""
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

"""

temperatura = int(input("Digite a temperatura do servidor: "))
if temperatura >= 30:
    print("ATENÇÃO a temperatura esta muito alta")
else:
    print("A temperatura esta estavél")