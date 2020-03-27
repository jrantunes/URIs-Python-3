#Theon's Answer

n = int(input())

valores = list(map(int, input().split()))
possiveis = []

for i in range(n):
    possiveis.insert(i, valores[i])

print(possiveis.index(min(possiveis)) + 1)
