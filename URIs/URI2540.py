#Leader's Impeachment

while True:
    try:
        n = int(input())
        votos = input().split()

        favor = votos.count("1")

        if favor/n >= 2/3:
            print("impeachment")

        else:
            print("acusacao arquivada")



    except(EOFError):
        break