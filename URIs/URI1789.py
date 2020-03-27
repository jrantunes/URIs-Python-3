#The Race of Slugs

while True:
    try:
        tam = int(input())
        vel = []
        nums = list(map(int, input().split()))

        for i in range(tam):
            vel.insert(i, nums[i])

        veloz = max(vel)
        
        if 10 > veloz:
            print("1")

        elif 10 <= veloz < 20:
            print("2")

        elif 20 <= veloz:
            print("3")
        
    except(EOFError):
        break
