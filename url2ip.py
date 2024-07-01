import socket 
import argparse
import requests
from colorama import init, Fore, Style

# Banner inicial
banner = """
GGGGGGG     OOOOOO   DDDDDD    GGGGGGG   OOOOOO   DDDDDD
G          O      O  D     D   G        O      O  D     D
G   GGGG   O      O  D      D  G   GGGG O      O  D      D
G      G   O      O  D     D   G      G O      O  D     D
GGGGGGG     OOOOOO   DDDDDD    GGGGGGG   OOOOOO   DDDDDD
"""
print(banner)

# Inicialización de colorama
init()

def obtener_ip_y_verificar_estado(url, mostrar_status_code):
    try:
        addr_info = socket.getaddrinfo(url, None , socket.AF_INET)
        ip_addresses = [ai[4][0] for ai in addr_info]
        
        respuesta = None 
        
        for ip_address in ip_addresses:
            try:
                response = requests.get(f'http://{ip_address}', timeout=5)
                
                if response.status_code == 200:
                    estado = f'[{Fore.GREEN}{response.status_code}{Style.RESET_ALL}]'
                elif response.status_code == 404:
                    estado = f'[{Fore.RED}{response.status_code}{Style.RESET_ALL}]'
                else:
                    estado = f'[{Fore.YELLOW}{response.status_code}{Style.RESET_ALL}]'
                    
                respuesta = f'La direccion IP de {url} es: {Fore.GREEN}{ip_address}{Style.RESET_ALL}'
                
                if mostrar_status_code:
                    respuesta += f' {estado}'
                    
                break
            except requests.RequestException:
                continue
        if respuesta is None:
            respuesta = f'Error: No se pudo realizar la solicitud HTTP'
            
    except socket.gaierror:
        respuesta = f'Error: No se pudo resolver la direccion para {url}'
        
    return respuesta

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Obtener la direccion Ip y Opcionalmente el codigo de estado HTTP de una url')
    parser.add_argument('--url','-u', type=str, required=True, help='Ingrese solo el dominio, ejemplo: example.com')
    parser.add_argument('--status_code', '-s', action='store_true', help='Mostrar el código de estado HTTP.')
    args = parser.parse_args()
    
    resultado = obtener_ip_y_verificar_estado(args.url, args.status_code)
    print(resultado)
