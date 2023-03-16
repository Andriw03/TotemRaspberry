from django.shortcuts import render, redirect, get_object_or_404
import time
import requests
import datetime
from .models import Lugar, MCA, Flujo

url= 'http://localhost:3000/'
def getApi(tabla):
    response = requests.get(url+tabla)
    if response.status_code == 200:
        data= response.json()
        return data
    else:
        return response.status_code

# Create your views here.
def pagina_inicio(request):
    mensaje =''
    if request.method == 'POST':
        if 'btnEntrada' in request.POST:
            pass
        elif 'btnSalida' in request.POST:
            pass
    return render(request, 'rasberry/pagina_inicio.html')

def ingresar_rut(request):
    return render(request,'rasberry/ingresar_rut.html')


def entrada(request, rut, mca):
    persona = getApi(f'persona/{rut}')
    mcadress = getApi(f'mca/{mca}')
    flujo = Flujo()
    flujo.rutTrabajador= rut
    flujo.sentido=1
    fecha = datetime.datetime.now()
    flujo.fechaHora = str(fecha.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    flujo.dirFoto = ''
    newMca = MCA()
    newMca =get_object_or_404(MCA, descripcionMCA=mca)
    flujo.idMCA = newMca
    flujo.save()
    return render(request,'rasberry/pagina_inicio.html')   


def salida(request, rut, mca):

    return render(request,'rasberry/pagina_inicio.html')    









