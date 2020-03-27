#Several Scores with Validation

def notas():
    avaliacoes = []
    while True:
        nota = float(input())
        if 0 <= nota <= 10:
            avaliacoes.append(nota)
            if len(avaliacoes) == 2:
                media = sum(avaliacoes) / len(avaliacoes)
                print("media = {:.2f}".format(media))
                return notas

        else:
            print("nota invalida")
    
        
notas()
while True:
    escolhas = ["1", "2"]
    escolha = input("novo calculo (1-sim 2-nao)\n")
    if escolha in escolhas:
        if escolha == "1":
            notas()

        elif escolha == "2":
            break
    
    else:
        continue
    