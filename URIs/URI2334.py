#Little Ducks

while True:
    n = int(input())
    if n == -1:
        break

    elif 0 <= n <= 10 ** 19:
        if n == 0:
            print(0)
        
        else:
            print(n - 1)
    
