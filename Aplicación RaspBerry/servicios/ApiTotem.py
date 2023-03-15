import requests

url= 'http://localhost:3000/'
def getApi(tabla):
    response = requests.get(url+tabla)
    if response.status_code == 200:
        data= response.json()
        return data
    else:
        return response.status_code

def agregarFlujo(data):
    response = requests.post(url,data=data)

