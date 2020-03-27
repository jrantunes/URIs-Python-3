#Remaining 2

restos = []
N = int(input())

for i in range(1, 10000 + 1):
    if i % N == 2:
        restos.append(i)

for resto in restos:
    print(resto)