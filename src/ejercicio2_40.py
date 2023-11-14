"""
Ejercicio 2.3.5
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción
NameError con el mensaje, "Incorrect Password!!"
"""

def tPassword(password: str):
    passOrig = "password"
    if password.replace(" ", "").lower() == passOrig:
        return "Correct Password!!"
    else:
        raise NameError


def getPassword():
    return input("Enter the Password: ")


def main():
    try:
        password = getPassword()
        print(tPassword(password))
    except NameError:
        print("Incorrect Password!!")
    
    
if __name__ == '__main__':
     main()