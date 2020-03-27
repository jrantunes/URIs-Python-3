#Output 5

a = 15
b = int(a / 2)
c = 15.456
d = c / 7
vb = "Valores de b:"
print(vb)
print("-" * len(vb))
print("1) b = {}".format(b))
print("2) b =", " " * 18, "{}".format(b))
z = "0" * 19
print("3) b = {}{}".format(z, b))
print("4) b = {}".format(b), " " * 18)
print("5) b = {}%".format(b))
print()
vd = "Valores de d:"
print(vd)
print("-" * len(vd))
print("1) d = {:.6f}".format(d))
print("2) d = {}".format(round(d)))
print("3) d = {:.1f}".format(d))
print("4) d = {:.2f}".format(d))
print("5) d = {:.3f}".format(d))
print("6) d =", " " * 14, "{:.3f}".format(d))
zz = "0" * 15
print("7) d = {}{:.3f}".format(zz, d))
print("8) d = {:.3f}".format(d), " " * 14)
print("9) d = {:.2f}%".format(d))