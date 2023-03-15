import RPi.GPIO as GPIO
import requests
import time
import PySimpleGUI as sg
import re
from servicios import ApiTotem, django, formatear_rut, obtenerMC
from vista import index
from entities.flujo import Flujo
from entities.persona import Persona
import datetime


#Al iniciar 
mc = obtenerMC.obtenerMac()
mc = ApiTotem.getApi(f'mca/{mc}')
# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variable booleana para indicar si el botón ha sido pulsado
boton_pulsado_entrada = False
boton_pulsado_salida = False

# Función que se ejecutará cuando se presione el botón físico
def boton_pulsado_entrada_callback(channel):
    global boton_pulsado_entrada
    boton_pulsado_entrada = True
    print("Botón entrada físico pulsado")
    

def boton_pulsado_salida_callback(channel):
    global boton_pulsado_salida
    boton_pulsado_salida = True
    print("Botón salida físico pulsado")


#defino una ventana para ingresar el rut

# Escuchar el botón físico
GPIO.add_event_detect(23, GPIO.RISING, callback=boton_pulsado_entrada_callback, bouncetime=300)
GPIO.add_event_detect(24, GPIO.RISING, callback=boton_pulsado_salida_callback, bouncetime=300)

# Mantener el script en ejecución
while True:
    if boton_pulsado_entrada:
        # Simular clic en el botón HTML
        fecha = datetime.datetime.now()
        response = django.entradaDjango(1)
        rut = index.ventanaInicio()
        response = django.entradaDjango(rut)
        data = ApiTotem.getApi(f'persona/{formatear_rut.format_rut(rut)}')
        index.popUp('Bienvenido: ' + data['nombrefull']+ '\nRut: '+ data['nombrefull']+ '\nHora de entrada: '+ str(fecha), 'Saludo',5)
        data = ApiTotem.getApi('flujo')
        flujo = Flujo()
        if data:
            for f in data:
                flujo.idFlujo = int(f['idFlujo']) + 1
        else:
            flujo.idFlujo = 1
        flujo.mc['idMCA']
        flujo.dirFoto = ''
        flujo.fechaHora = str(fecha)
        flujo.rutTrabajador = rut
        flujo.sentido = 1
        dataFlujo ={
            'idFlujo': flujo.idFlujo,

            'rutTrabajador': flujo.rutTrabajador,

            'sentido': flujo.sentido,

            'fechaHora': flujo.fechaHora,

            'dirFoto': flujo.dirFoto,

            'idMCA': flujo.idMCA 
        }
        response = ApiTotem.agregarFlujo(dataFlujo)
        print(response)
        boton_pulsado_entrada = False
        print("Botón HTML pulsado")
        
    if boton_pulsado_salida:
        # Simular clic en el botón HTML
        response = django.salidaDjango(1)
        rut = index.ventanaInicio()
        response = django.salidaDjango(rut)
        data = ApiTotem.getApi(f'persona/{formatear_rut.format_rut(rut)}')
        index.popUp('Hasta Luego: ' + data['nombrefull']+ '\nRut: '+ data['nombrefull']+ '\nHora de Salida: '+ str(fecha), 'Despedida',5)
        boton_pulsado_salida = False
        print("Botón HTML pulsado")

