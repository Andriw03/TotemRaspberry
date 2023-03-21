import json
import schedule
import time
import requests
import pandas as pd
from servicios import ApiTotem


def obtener_datos_y_exportar_excel():
    response = ApiTotem.getApi('informeflujo')

    df = pd.read_json(json.dumps(response))
    df.to_excel('/home/codelco/Desktop/Django/Pendrive/txttotem/clientes.xlsx', index=False)
obtener_datos_y_exportar_excel()
# schedule.every().month.at('10:00').do(obtener_datos_y_exportar_excel)

# while True:
#     schedule.run_pending()
#     time.sleep(1)