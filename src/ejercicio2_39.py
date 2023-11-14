"""
Ejercicio 2.3.4
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará
el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""


def enterNum(number: int):
    if (type(number) != int):
        raise ValueError
    else:
        return "La entrada es correcta."


def main():
    try:
        numer = int(input("Dime un número entero: "))
        print(enterNum(numer))
    except ValueError:
        print("La entrada no es correcta.")
                    

if __name__ == '__main__':
    main()