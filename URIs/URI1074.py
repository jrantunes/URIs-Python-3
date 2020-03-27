#Even or Odd

for i in range(int(input())):
    x = int(input())
    e_o = ""
    p_n = ""
    if x == 0:
        print("NULL")
        pass
    else:
        if x > 0:
            p_n = "POSITIVE"
        else:
            p_n = "NEGATIVE"
    
        if x % 2 == 0:
            e_o = "EVEN"
        else:
            e_o = "ODD"

        print(e_o, p_n)