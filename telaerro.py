
def tratativaDeErro(erro: any):

    from PySimpleGUI import PySimpleGUI as sg


    sg.theme('Reddit')

    layout = [

        [sg.Titlebar('Erro:')],

        [sg.Text(f'\n \n Ocorreu um erro, motivo: {erro} \n \n')]

    ]


    janela = sg.Window('Erro:', layout)


    while True:

        eventos, valores = janela.read()

        if eventos == sg.WINDOW_CLOSED:

            break
        break