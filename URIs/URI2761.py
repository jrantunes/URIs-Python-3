#Input and Output of Various Types

import re
import struct
n = input()
m = re.split(r'(\s+)', n)


inteiro = int(m[0])
del m[0]
del m[0]

dec = float(m[0])
decimal = struct.unpack("f", struct.pack("f", dec))
del m[0]
del m[0]

caracter = m[0]
del m[0]
del m[0]

a = ','.join(m).replace(",", "")

print("%d" % inteiro + "%f" % decimal + "%s" % caracter + "%s" % a)
print("%d\t" % inteiro + "%f\t" % decimal + "%s\t" % caracter + "%s" % a)
print("%10d" % inteiro + "%10f" % decimal + "%10s" % caracter + "%10s" % a)