#Playing Darts by Distance

v = int(input())

for i in range(v):
    #JOAO
    pj1 = list(map(int, input().split())) 
    pontosj1 = pj1[0] * pj1[1]
        
    pj2 = list(map(int, input().split()))
    pontosj2 = pj2[0] * pj2[1]
        
    pj3 = list(map(int, input().split()))
    pontosj3 = pj3[0] * pj3[1]

    #MARIA
    pm1 = list(map(int, input().split()))
    pontosm1 = pm1[0] * pm1[1]

    pm2 = list(map(int, input().split()))
    pontosm2 = pm2[0] * pm2[1]
    
    pm3 = list(map(int, input().split()))
    pontosm3 = pm3[0] * pm3[1]

    pontos_joao = pontosj1 + pontosj2 + pontosj3
    pontos_maria = pontosm1 + pontosm2 + pontosm3

    if pontos_joao > pontos_maria:
        print("JOAO")
    
    else:
        print("MARIA") 