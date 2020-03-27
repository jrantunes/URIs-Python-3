#Rock, Paper, Airstrike

escs = ["ataque", "pedra", "papel"]
n = int(input())
for i in range(n):
  jog1 = input()
  jog2 = input()
  if jog1 == escs[0] and jog2 == escs[0]:
    print("Aniquilacao mutua")
  
  elif jog1 == escs[2] and jog2 == escs[2]:
    print("Ambos venceram")
  
  elif jog1 == escs[1] and jog2 == escs[1]:
    print("Sem ganhador")
  
  elif jog1 == escs[1] and jog2 == escs[2]:
    print("Jogador 1 venceu")
  
  elif jog1 == escs[2] and jog2 == escs[1]:
    print("Jogador 2 venceu")
  
  elif jog1 == escs[0] and jog2 == escs[1] or jog2 == escs[2]:
    print("Jogador 1 venceu")
  
  else:
    print("Jogador 2 venceu")
  