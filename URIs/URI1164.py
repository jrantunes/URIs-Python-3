#Perfect Number

n = int(input())
for i in range(n):
    num = int(input())
    div = []
    for m in range(1, num):
        if num % m == 0:
            div.append(m)
    if sum(div) == num:
        print("{} eh perfeito".format(num)) 
    else:
        print("{} nao eh perfeito".format(num))