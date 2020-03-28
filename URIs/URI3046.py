#Dominó

n = int(input())

if 0 <= n <= 10000:
    form = ((n + 1) * (n + 2)) / 2
    print("{:.0f}".format(form))