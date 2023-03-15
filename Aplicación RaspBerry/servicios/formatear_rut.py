import re

def format_rut(rut):
    rut= re.sub("[^0-9]","",rut)
    rut = rut.zfill(9)
    rut_formateado = f"{rut[:2]}.{rut[2:5]}.{rut[5:8]}-{rut[8:]}"
    return rut_formateado