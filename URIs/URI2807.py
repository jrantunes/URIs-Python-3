#Iccanobif

n = int(input())
p1 = 0
p2 = 1

if n != 1:
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[p1] + fib[p2])
        p1 += 1
        p2 += 1

    fib.reverse()
    fib = str(fib).strip("[]").replace(",", "")
    print(fib)
else:
    print(1)