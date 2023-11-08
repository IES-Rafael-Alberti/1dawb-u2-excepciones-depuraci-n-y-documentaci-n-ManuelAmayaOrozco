"""
Ejercicio 2.4
Algoritmo burbuja
"""


def bubbleAlgorythm(a: list):
    total = len(a) - 1
    
    for i in range(1, len(a)):
        for j in range(0, total):
            if (a[j] > a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
        
        total -= 1
    return a
            
                        
def main():
    a = [8, 3, 1, 19, 14]
    print(bubbleAlgorythm(a))
    
    
if __name__ == '__main__':
     main()