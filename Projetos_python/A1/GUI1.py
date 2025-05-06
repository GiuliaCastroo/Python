from  PySimpleGUI import  PySimpleGUI as sg
#import GUI_back

#Layout
sg.theme('Reddit')

layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char ='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de Login', layout)

#Ler Eventos
while True:
    eventos , valores = janela.read()
    if eventos == sg.WINDOW_CLOSE:
        break
    if eventos == "Entrar":
        if valores['usuario'] == 'root' and valores ['senha'] == 'root':
            print ("Bem-vindo ao teste!")
            
            
#Biblioteca  virando paga migrar para PyQT6 ou Tkinter