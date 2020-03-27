#Positive Numbers

ctr = 0

for i in range(6):
    n = float(input())
    if n > 0:
        ctr += 1
    else:
        pass

print(ctr, "valores positivos")