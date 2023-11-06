"""
Ejercicio 2.3.2
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos
los números impares desde 1 hasta ese número separados por comas.
"""


def cuentImpar(num: int) -> str:
    ser = None
    if (num < 0):
        raise ValueError
    i = 1
    ser = "{i}, ".format(i = i)
    if((num % 2) == 0):
        while(i < (num - 3)):
            i += 2
            ser = ser + "{i}, ".format(i = i)
        ser = ser + "{fin}".format(fin = (num - 1))
        return ser
    else:
        while(i < (num - 2)):
            i += 2
            ser = ser + "{i}, ".format(i = i)
        ser = ser + "{fin}".format(fin = num)
        return ser


def receiveNum(msj: str) -> int:
    
    number = None
    
    try:
        number = int(input(msj))
    except:
        print("**Error** Número introducido no válido")
    return number


def main():
    numer = receiveNum("Dime un número entero positivo: ")
    if numer != None:
        try:
            print(cuentImpar(numer))
        except ValueError:
            print("**Error** El número no es entero positivo.")
        except:
            print("**Error** Se produjo un error y no es posible realizar la cuenta.")
    
    
if __name__ == '__main__':
    main()