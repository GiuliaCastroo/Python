#Passo a passo  ---> Lógica 
# Passo 1: Entrar no sistema da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo 2: Fazer Login
#Passo 3: Importar a base de dados
#Passo 4: Cadastrar um produto
#Passo 5: Enviar
#Passo 6: Cadastrar produtos até acabar

############################   Anotações   ###########################################
    #para automatizar usar a biblioteca pyautogui --> comando pip isntall pyautogui
    #pyautogui.hotkey (ex. ctrl + alt) para combinações de teclas
######################################################################################

import pyautogui
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1.0

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=806, y=481)
# escrever o seu email
pyautogui.write("adm@teste.com.br")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab") # clique no botao de login
pyautogui.press("enter")


# Passo 3: Importar a base de produtos pra cadastrar


tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=779, y=346)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
