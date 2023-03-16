import PySimpleGUI as sg
from servicios import ApiTotem, django, formatear_rut
import time
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
    filtro = 0
    while True:
        event, values = window.read()
        if event in (None, 'Cancelar'):
            break
        if event == '-NUM-':
            rut = values['-NUM-']
            if not rut.isnumeric() :
                filtro = 1
                if len(rut) == 114: 
                    print(rut)
                    rut = formatear_rut.extraerRut(rut)
                    print(rut)
                    break
            elif len(rut)== 8 and filtro == 0:
                if (formatear_rut.validar_rut(rut)):
                    print(rut)
                    break    
                else:
                    dv = formatear_rut.calcular_dv(rut)
                    rut = str(rut)+str(dv) 
                    print(rut)
                    break

    # Cerramos la ventana
    window.close()
    return rut

def popUp(mensaje, title, duracion):
    sg.Popup(mensaje, title=title,auto_close=True,auto_close_duration=duracion)

   