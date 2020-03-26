#Banknotes

notas = [100, 50, 20, 10, 5, 2, 1]

n = int(input())
print(n)

for nota in notas:
    qtde = int(n / nota)
    print("{} nota(s) de R$ {},00".format(qtde, nota))
    n -= qtde * nota