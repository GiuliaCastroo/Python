"""
1) Elaborar um programa que leia a idade e o tempo de serviço de um trabalhador e mostre se o
trabalhador pode ou não se aposentar. As condições para aposentadoria são:
• Ter pelo menos 65 anos,
• Ou ter trabalhado pelo menos 30 anos,
• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
"""
idade = int(input("Digite sua idade: "))
t_servico = int(input("Digite seu tempo de serviço: "))

if idade >=65 and t_servico >= 30 or (idade >= 60 and t_servico >= 25):
    print("o trabalhador pode se aposentar")
else:
    print("o trabalhador não pode se aposentar")
    
