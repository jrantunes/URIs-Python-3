#Event

while True:
    x, m = input().split()
    x = int(x)
    m = int(m)

    if 0 < x <= 3 and 10 <= m <= 2 ** 32-1:
        xp = x * m
        print(xp)
        continue

    elif x == 0 and m == 0:
        break