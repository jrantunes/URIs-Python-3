#Enjoy the Offer

rep = int(input())

for i in range(rep):
    n, k = input().split()
    n = int(n)
    k = int(k)
    vazias = 0
    while n >= k:
        n = n - k
        vazias += 1
    print(n + vazias)