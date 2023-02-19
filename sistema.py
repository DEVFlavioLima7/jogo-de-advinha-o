import PySimpleGUI as sg
layout= [
    
    [sg.Text('usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key ='mensagem')],

]
window=sg.Window('login',layout=layout)
while True:
    event,values=window.read()
    if event==sg.WINDOW_CLOSED:
        break
    elif event=='login':
        principal='josé'
        senhacorreta='12345'
        usuario=values['usuario']
        senha=values['senha']
        if usuario ==principal and senha==senhacorreta:
            window['mensagem'].update('login feito com sucesso!')
        else:
            window['mensagem'].update('usuario ou senhas incorretos!digite novamente.')
            
       

    


















