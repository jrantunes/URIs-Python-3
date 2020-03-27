# Logical Sequence 2

n1, n2 = list(map(int, input().split()))
x = 1
for i in range(1, int((n2/n1)) + 1):
    r = ""
    for y in range(n1):
        r += str(x) + " "
        x += 1
    print(r[:-1])