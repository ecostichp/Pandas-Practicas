import sys

def imprimir(orm):
    print(f'{orm} es el modo que elgiste para tu ORM')


def wep(flag, func):
    for f in flag:
       if f in ('test', 'dev', 'prod'):
           print(f)


wep(sys.argv, imprimir)

# Corre el archivo con el comando "py b.py" y escribe cualquier opción entre "test, dev, prod"
