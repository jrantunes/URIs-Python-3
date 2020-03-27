#Pizza Before BH

while True:
  try:
    n, d = input().split()
    n = int(n)
    d = int(d)
    data = ""
    
    for i in range(d):
      a = input().split()
      aux = a[0]
      del a[0]
      pessoas = []
      
      for i in range(n):
        pessoas.append(a[i])

      if '0' not in pessoas and data == "":
        data = aux

      else:
        pass
    
    if data != "":
      print(data)   
    
    else:
      print("Pizza antes de FdI")

  except EOFError:
    break