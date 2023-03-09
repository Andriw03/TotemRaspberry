from django.shortcuts import render
import time


# Configurar los pines 23 y 24 como entrada


# Create your views here.
def pagina_inicio(request):
    
    mensaje =''
    if request.method == 'POST':
        if 'entrada' in request.POST:
            print("Oye yapo funciona")
        elif 'salida' in request.POST:
            print ('salida') 

    return render(request,'rasberry/pagina_inicio.html')


def prueba():
    print('Hola')
        












    # Buscar el dispositivo USB del escáner Honeywell 3310g
    #dev = usb.core.find(idVendor=0x0c2e, idProduct=0x0b61)
    #dev.set_configuration()
    #print(dev)
    # Configurar el puerto serial
    #port = serial.Serial('/dev/ttyprintk', baudrate=9600, timeout=1)

    # Esperar a que el escáner esté listo
    #port.write(b'\x16\x54\x0D')
    #response = port.read(7)

    # Imprimir la respuesta del escáner
    #print(response)
