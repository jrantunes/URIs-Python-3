#Floating Number Input and Output

import struct
v1 = list(map(float, input().split()))
a = struct.unpack("f", struct.pack("f", v1[0]))
b = struct.unpack("f", struct.pack("f", v1[1]))

v2 = list(map(float, input().split()))
c = v2[0]
d = v2[1]

print("A = %f," % (a), "B = %f\n" % (b) + "C = %f, D = %f" % (c, d))
print("A = %.1f," % (a), "B = %.1f\n" % (b) + "C = %.1f, D = %.1f" % (c, d))
print("A = %.2f," % (a), "B = %.2f\n" % (b) + "C = %.2f, D = %.2f" % (c, d))
print("A = %.3f," % (a), "B = %.3f\n" % (b) + "C = %.3f, D = %.3f" % (c, d))
print("A = %.3E," % (a), "B = %.3E\n" % (b) + "C = %.3E, D = %.3E" % (c, d))
print("A = %.0f," % (a), "B = %.0f\n" % (b) + "C = %.0f, D = %.0f" % (c, d))