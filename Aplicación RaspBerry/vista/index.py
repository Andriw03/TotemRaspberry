import PySimpleGUI as sg
from servicios import ApiTotem, django, formatear_rut

def ventanaInicio():
    sg.theme('DarkBlue')

    # Definimos el diseño de la ventana
    layout = [[sg.Text('Escanee identificacion:')],
            [sg.InputText(key='-NUM-', enable_events=True)],
            ]

    # Creamos la ventana
    window = sg.Window(' ', layout)

    #Inicializamos la variable rut
    rut=''
    # Leemos los eventos de la ventana
    #ver que pasa cuando la ventana queda abierta
    while True:
        
        event, values = window.read()
        if event in (None, 'Cancelar'):
            break
        if event == '-NUM-':
            rut = values['-NUM-']
            if len(rut)== 9 :
                data = ApiTotem.getApi(f'persona/{formatear_rut.format_rut(rut)}')
                break

    # Cerramos la ventana
    window.close()
    return rut

def popUp(mensaje, title, duracion):
    sg.Popup(mensaje, title=title,auto_close=True,auto_close_duration=duracion)