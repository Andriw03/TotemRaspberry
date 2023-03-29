import json
import schedule
import time
from datetime import datetime
import requests
import pandas as pd

from servicios import ApiTotem

fecha = datetime.now()
fecha = fecha.strftime('%m-%Y')
print(fecha)

def obtener_datos_y_exportar_excel():
    response = ApiTotem.getApi('informeflujo')

    df = pd.read_json(json.dumps(response))
    df.to_excel(f'/home/codelco/Desktop/Django/Pendrive/txttotem/informe-{fecha}.xlsx', index=False)

obtener_datos_y_exportar_excel()

schedule.every().month.at('06:00').do(obtener_datos_y_exportar_excel)

while True:
     schedule.run_pending()
     time.sleep(1)

