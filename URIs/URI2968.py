#Hour for a Run

import math
v, n = input().split()

v = int(v)
n = int(n)

x = []
for i in range(1, 10):
    r = math.ceil((n * v * i) / 10.0)
    x.append(r)

print(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])