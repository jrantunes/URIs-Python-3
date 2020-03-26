#Average 3

#media 3 adicionando a recuperação
#ler 4 valores com ponto flutuante na mesma linha
notas = input().split()

N1 = float(notas[0])
N2 = float(notas[1])
N3 = float(notas[2])
N4 = float(notas[3])

#calcular a media com os pesos (N1 - 2, N2 - 3, N3 - 4, N4 - 1) e imprimir
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4) / (2 + 3 + 4 + 1)
print("Media: {:.1f}".format(media))

#se a media estiver entre 5 e 6.9 imprimir "Aluno em exame."
if 5 <= media <= 6.9:
    print("Aluno em exame.")
    #ler a nota do exame e imprimir
    nota_exame = float(input())
    print("Nota do exame: {}".format(nota_exame))
    #recalcular a media (somando a media anterior com a nota do exame e dividindo por 2)
    media_final = (media + nota_exame) / 2
    
    #se a media final for maior ou igual a 5 (Aluno aprovado)
    if media_final >= 5:
        print("Aluno aprovado.")
    
    #se a media final for menor que 5 (Aluno reprovado)
    else:
        print("Aluno reprovado.")
    
    print("Media final: {:.1f}".format(media_final))

#se a media for maior ou igual a 7 imprimir "Aluno aprovado."
elif media >= 7:
    print("Aluno aprovado.")

#se a media for menor que 5 imprimir "Aluno reprovado."
else:
    print("Aluno reprovado.")

