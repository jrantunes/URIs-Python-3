#Sequence IJ 4

i = 0
j1 = 1
j2= 2
j3 = 3
print("I={} J={}".format(i, j1))
print("I={} J={}".format(i, j2))
print("I={} J={}".format(i, j3))

while i < 1:   
    i += 0.2
    j1 += 0.2
    j2 += 0.2
    j3 += 0.2
    if i == 1:
        break
    else:
        print("I={:.1f} J={:.1f}".format(i, j1))
        print("I={:.1f} J={:.1f}".format(i, j2))
        print("I={:.1f} J={:.1f}".format(i, j3))

print("I={:.0f} J={:.0f}".format(i, j1))
print("I={:.0f} J={:.0f}".format(i, j2))
print("I={:.0f} J={:.0f}".format(i, j3))

while i < 1.6:
    i += 0.2
    j1 += 0.2
    j2 += 0.2
    j3 += 0.2
    print("I={:.1f} J={:.1f}".format(i, j1))
    print("I={:.1f} J={:.1f}".format(i, j2))
    print("I={:.1f} J={:.1f}".format(i, j3))
   
print("I={:.0f} J={:.0f}".format(i + 0.2, j1 + 0.2))
print("I={:.0f} J={:.0f}".format(i + 0.2, j2 + 0.2))
print("I={:.0f} J={:.0f}".format(i + 0.2, j3 + 0.2))