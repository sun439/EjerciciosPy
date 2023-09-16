#Ordenar una lista en forma ascendente 

import random

def main():

    lista = []

    for indice in range(1,11):
        lista.append(random.randint(1,100))

    print(lista)

    lista.sort() # Para forma descentente podemos poner sort( reverse = True )

    print(lista)

if __name__ == '__main__':
    main()