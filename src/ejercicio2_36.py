"""
Ejercicio 2.3.1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""


def cuentEdad(ed: int):
    i = 1
    while(i < ed):
        print(i)
        i += 1
    return ed


def main():
    edad = (input("Dime tu edad: "))
    try:
        print(cuentEdad(int(edad)))
    except:
        print("**ERROR** Edad no válida.")
    
    
if __name__ == '__main__':
     main()