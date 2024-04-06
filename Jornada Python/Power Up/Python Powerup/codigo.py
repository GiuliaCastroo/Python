#Passo a passo  ---> Lógica 
# Passo 1: Entrar no sistema da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo 2: Fazer Login
#Passo 3: Importar a base de dados
#Passo 4: Casdastrar um produto
#Passo 5: Enviar
#Passo 6: Cadastrar produtos até acabar

############################   Anotações   ###########################################
    #para automatizar usar a biblioteca pyautogui --> comando pip isntall pyautogui
    #pyautogui.hotkey (ex. ctrl + alt) para combinações de teclas
######################################################################################

# Importar bibliotecas
import pyautogui
import time 

pyautogui.PAUSE = 1.5

#variaveis
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
navegador = "Opera"

# Passo 1: Entrar no sistema da empresa (Abrir o navegador)

pyautogui.press ("win")
pyautogui.write (navegador)
pyautogui.press ("enter")

pyautogui.write (link)
pyautogui.press ("enter")

#Dar uma pausa em um lugar especifico
time.sleep(3)


#Passo 2: Fazer Login
pyautogui.click (x=661, y=487)
pyautogui.write ("adm@teste.com")
pyautogui.press ("tab")
pyautogui.write ("adm123")

#logar no botão de logar
pyautogui.click (x=987, y=692)
time.sleep(3) #garantia para o site carregar

#Passo 3: Importar a base de dados
