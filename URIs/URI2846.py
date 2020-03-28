#	Fibonot

def fib(n):
  if n == 1 or n == 2:
    return False 
  
  ant = 1
  atual = 2
  termo = 0
  check = True
  
  while True:
    termo = ant + atual
    ant = atual
    atual = termo

    if termo == n:
      check = False
      break
    
    elif n < termo:
      break
  
  return check

x = int(input())

cont = 0
continua = True
i = 4

while continua:
  if fib(i):
    cont += 1
    
    if x == cont:
      print(i)
      continua = not continua
  
  i += 1