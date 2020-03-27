#Leap Year or Not Leap Year and …

pula_linha = 0
while True:
    try:
        ano = int(input())
        
        biss = 0
        ordi = 1
        
        if pula_linha:
            print("")
        
        pula_linha = 1
        
        if ano % 4 == 0 and not(ano % 100 == 0) or ano % 400 == 0:
            print("This is leap year.")
            biss = 1
            ordi = 0
        
        if ano % 15 == 0:
            print("This is huluculu festival year.")
            ordi = 0
         
        if ano % 55 == 0 and biss:
            print("This is bulukulu festival year.")
        
        if ordi:
            print("This is an ordinary year.")

    except EOFError:
        break