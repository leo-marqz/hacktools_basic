import sys
import requests
from os import path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Dominio victima", required=True)
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists('subdomains.txt'):
            domains = open('subdomains.txt', 'r')
            domains = domains.read().split('\n')

            for domain in domains:
                url = f'https://{domain}.{parser.target}'
                try:
                    requests.get(url)
                except requests.ConnectionError as ce:
                    print(f'(-) No se encontro el subdominio: {url}')
                else:
                    print(f'(+) Subdominio encontrado: {url}')   

            for domain in domains:
                url = f'http://{domain}.{parser.target}'
                try:
                    requests.get(url)
                except requests.ConnectionError as ce:
                    print(f'(-) No se encontro el subdominio: {url}')
                else:
                    print(f'(+) Subdominio encontrado: {url}')           
           
        else:
            print('(-) No se encontraron subdominios')
            sys.exit()    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Script cancelado por el usuario")
        sys.exit()
    except Exception as e:
        pass    