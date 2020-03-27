#Merry Christmaaas!

a = []
N = int(input())
for i in range(N):
    a.append("a")

a = ','.join(a)
a = a.replace(",", "")
print("Feliz nat{}l!".format(a))