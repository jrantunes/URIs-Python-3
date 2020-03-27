#Lowest Number and Position

n = int(input())

vetor = []

nums = list(map(int, input().split()))

for i in range(n):
    vetor.insert(i, nums[i])

print("Menor valor: {}".format(min(vetor)))
print("Posicao: {}".format(vetor.index(min(vetor))))