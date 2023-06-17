
import subprocess
import argparse
import sys
import webtech

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Ingresa url de sitio web", required=True)
parser = parser.parse_args()

def main():
    if parser.target:
        wt = webtech.WebTech()
        result = wt.start_from_url(parser.target, timeout=5)
        with open('results_scanner_webtech.txt', 'a') as file:
            file.write(result + '\n')
            file.write('-'*100 + '\n\n')
    else:
        parser.print_help()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Cerrando app....')
        sys.exit()
    except Exception as e:
        print(e)
        print('Error, Cerrando app....')
        sys.exit()        