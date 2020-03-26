#Banknotes and Coins

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

N = float(input())

print("NOTAS:")
for nota in notas:
    qtde_notas = int(N / nota)
    print("{} nota(s) de R$ {:.2f}".format(qtde_notas, nota))
    N -= qtde_notas * nota

print("MOEDAS:")
for moeda in moedas:
    qtde_moedas = int(round(N, 2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtde_moedas, moeda))
    N -= qtde_moedas * moeda