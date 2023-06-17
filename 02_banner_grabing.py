import socket
import sys

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="IPAddress victima", required=True)
parser = parser.parse_args()

def banner(ip_address:str, port:int):
    sock = socket.socket()
    sock.connect((ip_address, port))
    print(str(sock.recv(1024)))

def main():
    if parser.target:
        ip_address = parser.target
        port = 443
        banner(ip_address, port)
        print('hola')
    else:
        print('ingresa una ip')    


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print("Exception - cerrando app....")
        sys.exit()        


