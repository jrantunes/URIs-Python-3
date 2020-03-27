#Ascending and Descending

while True:
    valores = input().split()
    
    x = int(valores[0])
    y = int(valores[1])
    
    if x == y:
        break
    
    elif x > y:
        print("Decrescente")
        
    else:
        print("Crescente")