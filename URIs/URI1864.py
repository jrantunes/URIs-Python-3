#Our Days Are Never Coming Back

while True:
    try:
        n = "LIFE-IS-NOT-A-PROBLEM-TO-BE-SOLVED"
        n = n.replace("", " ")
        n = n.split()
        n[4], n[7], n[11], n[13], n[21], n[24], n[27] = " ", " ", " ", " ", " ", " ", " "

        num = int(input())

        if 1 <= num <= 34:
            res = []
            for i in range(0, num):
                res.append(n[i])

            a = ",".join(res).strip("[]")
            a = a.replace(",", "")
            print(a)

    except(EOFError):
        break