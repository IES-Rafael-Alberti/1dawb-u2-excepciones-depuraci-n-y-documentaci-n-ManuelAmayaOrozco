"""
Ejercicio 2.4
Algoritmo burbuja
"""


def bubbleAlgorythm(a: list):
    """Solves and puts the values of an array in order through the use of the bubble algorithm.
    
    Parameters
    ----------
    a : list
        The array to be ordered correctly by the bubble algorithm.
        
    Returns
    -------
    a : list
        The same list from before, now properly ordered by the bubble algorithm.
    """
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