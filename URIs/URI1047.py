#Game Time with Minutes

horas = input().split()

hora_inicial = int(horas[0])
min_inicial = int(horas[1])

hora_final = int(horas[2])
min_final = int(horas[3])

if hora_inicial == hora_final and min_inicial == min_final:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:

    if hora_final > hora_inicial and min_final < min_inicial:
        hour = hora_final - 1
        min_finn = min_final + 60
        h = hour - hora_inicial
        min = min_finn - min_inicial
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, min))
    
    elif hora_final >= hora_inicial and min_final >= min_inicial:
        h = hora_final - hora_inicial
        min = min_final - min_inicial
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, min))
    
    elif hora_final == hora_inicial or hora_final <= hora_inicial and min_final < min_inicial:
        min = (min_final + 60) - min_inicial
        hf = hora_final - 1 
        h_abs = abs(hf - hora_inicial)
        h = 24 - h_abs
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, min))
        
        if h >= 24:
            h = 23
            print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, min))

    else:
        hour = abs(hora_final - hora_inicial)
        h = 24 - hour
        min = min_final - min_inicial
        print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, min))