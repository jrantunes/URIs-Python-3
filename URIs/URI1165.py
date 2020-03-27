#Prime Number

n = int(input())
for i in range(n):
    num = int(input())
    divisores = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            divisores += 1
            if divisores > 1:
                break
    if divisores > 1:
        print("{} nao eh primo".format(num))
    else:
        print("{} eh primo".format(num))