"""
Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. 
Para isso, ela usará o horário atual. 
O escritório só permite acesso entre 8h e 18h. 
Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso 
é permitido ou negado.
"""

horas = float(input("Digita o horario em formato de 24 horas: "))
if horas < 8 or horas > 18:
    print("Entrada liberada somente em horario comercial")
else:
    print("Entrada liberada")

