#Array Selection I

a = []

for i in range(100):
    
    x = float(input())
    a.append(x)
    
    if x <= 10.0:
        print("A[{}] = {}".format(i, x))