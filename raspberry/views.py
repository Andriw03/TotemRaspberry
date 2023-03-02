from django.shortcuts import render 
import PySimpleGUI as sg
import usb.core
import usb.util

# Create your views here.
def pagina_inicio(request):
    if request.method == 'POST':
        if 'entrada' in request.POST:
            print ('Entrada')
            rut = request.POST.get('rutEntrada')
            print(rut)
            #prueba()
        elif 'salida' in request.POST:
            print ('salida')
            rut = request.POST.get('rutSalida')
            print(rut)
    return render(request,'rasberry/pagina_inicio.html')

def prueba():
   # Buscar el dispositivo USB del escáner Honeywell 3310g
    dev = usb.core.find(idVendor=0x0c2e, idProduct=0x0b7c)

    # Activar modo de emulación de teclado
    dev.set_configuration()

    # Leer datos del escáner en modo Keyboard Wedge
    while True:
        try:
            data = dev.read(0x81, 64)
            barcode = ''.join([chr(x) for x in data[2:]])
            print('Barcode: {}'.format(barcode))
        except usb.core.USBError as e:
            if e.args == ('Operation timed out',):
                continue