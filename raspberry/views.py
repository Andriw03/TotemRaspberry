from django.shortcuts import render, redirect
import time



# Create your views here.
def pagina_inicio(request):
    mensaje =''
    if request.method == 'POST':
        if 'btnEntrada' in request.POST:
            print("Oye yapo funciona")
            return redirect(to='ingresar_rut') 
        elif 'btnSalida' in request.POST:
            print ('salida') 
    return render(request, 'rasberry/pagina_inicio.html')
def ingresar_rut(request):
    return render(request,'rasberry/ingresar_rut.html')


def entrada(request, id):
    print('Presiono Entrada ' + str(id))  
    return redirect('ingresar_rut')
    #return render(request,'rasberry/ingresar_rut.html')

def salida(request):
    print("Ingresar Tip al scanner para Salida")
    rut_salida = input("")
    print('Presiono Salida')
    return render(request,'rasberry/pagina_inicio.html')    












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
