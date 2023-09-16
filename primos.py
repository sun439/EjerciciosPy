#Generar una lista de números primos en un rango dado.

def main():
    
    rango_menor= int(input("Escribe el numero más bajo del rango: "))
    rango_mayor= int(input("Escribe el numero más alto del rango: "))

    for primo in range (rango_menor,rango_mayor + 1):

        if primo > 1:
            for i in range (2, primo):
                if (primo % i) == 0:
                    break
            else:

                print(primo)
    

if __name__ == '__main__':
    main()
