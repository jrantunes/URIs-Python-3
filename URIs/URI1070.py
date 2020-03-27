#Six Odd Numbers

x = int(input())
ctr = 0

while ctr < 6:
    if x % 2 != 0:
        print(x)
        ctr += 1
    else:
        pass
    x += 1