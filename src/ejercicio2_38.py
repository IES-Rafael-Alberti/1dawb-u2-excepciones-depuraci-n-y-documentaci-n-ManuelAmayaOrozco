"""
Ejercicio 2.3.3
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la
cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número
hasta introducir uno correcto.
"""

from src.ejercicio2_37 import receiveNum


def cuentAtras(num: int):
    if (num < 0):
        raise ValueError
    i = num
    ser = "{i}, ".format(i = i)
    while(i > 1):
        i -= 1
        ser = ser + "{i}, ".format(i = i)
    ser = ser + "{fin}".format(fin = (i - 1))
    return ser


def main():
    correctnumer = False
    while (not correctnumer):
        numer = receiveNum("Dime un número entero positivo: ")
        if (numer != None):
            try:
                print(cuentAtras(numer))
                correctnumer = True
            except ValueError:
                if (numer == None):
                    print("**Error** Número no introducido.")
                else:
                    print("**Error** Número no válido.")
            except:
                print("**Error**")
    
    
if __name__ == '__main__':
    main()