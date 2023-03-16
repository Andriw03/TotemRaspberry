import re

def format_rut(rut):
    rut= re.sub("[^0-9]","",rut)
    rut = rut.zfill(9)
    rut_formateado = f"{rut[:2]}.{rut[2:5]}.{rut[5:8]}-{rut[8:]}"
    return rut_formateado


def calcular_dv(rut):
    suma = 0
    multiplo = 2
    for i in reversed(str(rut)):
        suma += int(i) * multiplo
        if multiplo == 7:
            multiplo = 2
        else:
            multiplo += 1
    dv = 11 - (suma % 11)
    if dv == 11:
        return "0"
    elif dv == 10:
        return "K"
    else:
        return str(dv)

def extraerRut(url):
    # URL completa
    # Busca el patrón del RUT en la URL
    rut_pattern = r"RUN¿(\d+)-?(\d)?"
    print(rut)
    matches = re.findall(rut_pattern, url)

    # Extrae el RUT de la primera coincidencia
    if matches:
        rut = matches[0][0]
        if matches[0][1]:
            rut += "-" + matches[0][1]
        dv = calcular_dv(rut)  # Calcula el dígito verificador
        rut +=  dv  # Agrega el dígito verificador al RUT
        
        # Imprime el RUT extraído
        print("RUT:", rut)
        return rut
    else:
        return 0
    
def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "")
    if len(rut) < 2:
        return False
    if not rut[:-1].isdigit():
        return False
    dv = rut[-1].upper()
    rut = rut[:-1]
    suma = 0
    multiplo = 2
    for i in reversed(rut):
        suma += int(i) * multiplo
        multiplo += 1
        if multiplo == 8:
            multiplo = 2
    digito = 11 - (suma % 11)
    if digito == 10:
        digito = "K"
    elif digito == 11:
        digito = "0"
    else:
        digito = str(digito)
    return dv == digito