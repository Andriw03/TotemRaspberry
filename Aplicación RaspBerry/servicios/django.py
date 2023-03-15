import requests

def entradaDjango(id):
    url_del_boton = (f"http://127.0.0.1:8000/presionar_entrada/{id}")
    response = requests.get(url_del_boton)
    return response

def salidaDjango(id):
    url_del_boton = (f"http://127.0.0.1:8000/presionar_salida/{id}")
    response = requests.get(url_del_boton)
    return response