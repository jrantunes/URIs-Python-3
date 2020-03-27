#Caesar Cipher

abc = 'abcdefghijklmnopqrstuvwxyz'
rep = int(input())
for x in range(rep):
  cifrada = ','.join(input()).lower().split(',')
  n = int(input())


  indices = []
  for c in cifrada:
    indices.append(abc.index(c) - n)

  palavra = []
  for i in indices:
    palavra.append(abc[i])

  resultado = ','.join(palavra).strip('[]').replace(',', '').upper()
  print(resultado)