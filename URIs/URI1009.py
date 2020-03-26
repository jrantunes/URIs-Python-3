#Salary with Bonus

nome = input()
sf = float(input())
vendas = float(input())

res = 0.15 * vendas + sf

print("TOTAL = R$ {:.2f}".format(res))