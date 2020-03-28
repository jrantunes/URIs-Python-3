#Input and Output of Integers

n1 = int(input())
n2 = int(input())
n3 = int(input())

print("A = {}, B = {}, C = {}".format(n1, n2, n3))
print("A = {:>10}, B = {:>10}, C = {:>10}".format(n1, n2, n3))
print("A = %010d, B = %010d, C = %010d" % (n1, n2, n3))
print("A = {:<10}, B = {:<10}, C = {:<10}".format(n1, n2, n3))