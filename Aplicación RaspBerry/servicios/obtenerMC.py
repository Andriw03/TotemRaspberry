import netifaces

def obtenerMac():
    # Obtener información de las interfaces de red
    interfaces = netifaces.interfaces()

    # Buscar la interfaz Ethernet
    eth_interface = None
    for interface in interfaces:
        if interface.startswith("eth"):
            eth_interface = interface
            break

    # Obtener la dirección MAC de la interfaz Ethernet
    if eth_interface is not None:
        mac_address = netifaces.ifaddresses(eth_interface)[netifaces.AF_LINK][0]['addr']
        print("La dirección MAC de la interfaz Ethernet es:", mac_address)
        return mac_address
    else:
        print("No se encontró la interfaz Ethernet")
        return 0