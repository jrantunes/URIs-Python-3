#S Sequence

frac = []

for i in range(2, 100 + 1):
    frac.append(1/i)
s = 1 + sum(frac)
print("{:.2f}".format(s))
