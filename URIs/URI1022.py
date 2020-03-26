#TDA Rational

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

v = int(input())

for i in range(v):
    n1, bar1, d1, op, n2, bar2, d2 = input().split()
    n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)

    if op == "+":
        a = (n1 * d2 + n2 * d1)
        b = (d1 * d2)

    elif op == "-":
        a = (n1 * d2 - n2 * d1)
        b = (d1 * d2)
    elif op == "*":
        a = (n1 * n2)
        b = (d1 * d2)
    elif op == "/":
        a = (n1 * d2)
        b = (n2 * d1)

    print("{}/{} = {:.0f}/{:.0f}".format(a, b, a/gcd(a, b), b/gcd(a, b)))