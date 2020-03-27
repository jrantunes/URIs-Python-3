#Scientific Notation

x = float(input())
if x == 0 and str(x)[0] != "-":
    print("+{:.4E}".format(x))

elif x == 0 and str(x)[0] == '-':
    print("{:.4E}".format(x))

elif x >= 0:
    print("+{:.4E}".format(x))
else: 
    print("{:.4E}".format(x))