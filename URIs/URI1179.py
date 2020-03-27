#Array Fill IV

par = []
impar = []
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    
    if len(par) == 5:
        ix = 0
        for v in par:
            print("par[{}] = {}".format(ix, v))
            ix += 1
        par = []
    if len(impar) == 5:
        ix = 0
        for v in impar:
            print("impar[{}] = {}".format(ix, v))
            ix += 1
        impar = []

if len(impar) > 0:
    ix = 0
    for v in impar:
        print("impar[{}] = {}".format(ix, v))
        ix += 1
if len(par) > 0:
    ix = 0
    for v in par:
        print("par[{}] = {}".format(ix, v))
        ix += 1