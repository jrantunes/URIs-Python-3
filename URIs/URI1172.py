#Array Replacement I

a = []
nul = []

for i in range(10):
    x = int(input())
    a.append(x)
    if x <= 0:
        nul.append(a.index(x)) 
        print("X[{}] = 1".format(i))
    else:
        print("X[{}] = {}".format(i, x))