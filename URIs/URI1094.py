#Experiments

n = int(input())
t = 0

coelhos = 0
ratos = 0
sapos = 0

while t < n:
    v = input().split()
    if v[1] == "C":
        coelhos += int(v[0])
    elif v[1] == "R":
        ratos += int(v[0])
    else:
        sapos += int(v[0])
    t += 1

total = coelhos + ratos + sapos
pc = (100 * coelhos) / total
pr = (100 * ratos) / total
ps = (100 * sapos) / total

print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}".format(total, coelhos, ratos, sapos))
print("Percentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %".format(pc, pr, ps))