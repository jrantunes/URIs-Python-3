#Where is the Marble?

from bisect import bisect_left
def find(num, array):
    indice = (bisect_left(array, num))
    if indice < len(array) and array[indice] == num:
        return indice + 1
    else:
        return -1

casos = 1

while True:
    n, q = list(map(int, input().split()))
    if n == 0 and q == 0:
        break
    
    print("CASE# {}:".format(casos))
    casos += 1
    lista = []
    for i in range(n + q):
        if i < n:
            lista.append(int(input()))
        if i == (n - 1):
            lista.sort()
        if i >= n:
            pesq = int(input())
            indice = find(pesq, lista)
            
            if indice == -1:
                print(str(pesq) + " not found")
            else:
                print(str(pesq) + " found at " + str(indice))