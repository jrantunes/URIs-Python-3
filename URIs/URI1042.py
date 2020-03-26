#Simple Sort

valores = []
valores_sort = []
for i in list(map(int, input().split())):
    valores.append(i)
    valores_sort.append(i)

valores_sort.sort()

for v in valores_sort:
    print(v)

print()

for v in valores:
    print(v)