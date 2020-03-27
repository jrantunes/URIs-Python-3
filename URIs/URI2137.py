#The Library of Mr. Severino

while True:
    try:
        n = int(input())
        books = []
        for i in range(n):
            cod = input()
            books.append(cod)
        books.sort()
        for b in books:
            print(b)
    except EOFError:
        break