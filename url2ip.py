import socket 
import argparse
import requests
from colorama import init, Fore, Style
banner = """

GGGGGGG     OOOOOO   DDDDDD    GGGGGGG   OOOOOO   DDDDDD
G          O      O  D     D   G        O      O  D     D
G   GGGG   O      O  D      D  G   GGGG O      O  D      D
G      G   O      O  D     D   G      G O      O  D     D
GGGGGGG     OOOOOO   DDDDDD    GGGGGGG   OOOOOO   DDDDDD
"""
print(banner)

init()

def obtener_ip_y_verificar_estado(url):
    try:
        ip_address = socket.gethostbyname(url)
                
        response = requests.get(f'http://{ip_address}')
        
        if response.status_code == 200:
            estado = f'[{Fore.GREEN}{response.status_code}{Style.RESET_ALL}]'
        elif response.status_code == 404:
            estado = f'[{Fore.RED}{response.status_code}{Style.RESET_ALL}]'
        return f'La dirección IP de {url} es: {Fore.GREEN}{ip_address}{Style.RESET_ALL}{estado}'
    except socket.gaierror:
        return f"Error: No se pudo resolver la dirección para {url}"
    except requests.RequestException as e:
        return f"Error: No se pudo realizar la solicitud HTTP {url}"
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Obtener la direccion IP de una URL. ')
    parser.add_argument('--url', '-u', type=str, required=True , help='ingrese solo el dominio ejemplo: example.com')
    arg = parser.parse_args()
    resultado = obtener_ip_y_verificar_estado(arg.url)
    print(resultado)

