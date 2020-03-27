#Positives and Average

valores_positivos = [] 
for i in range(6):
    nums = float(input())
    if nums > 0:
        valores_positivos.append(nums)
    else:
        pass
print("{} valores positivos".format(len(valores_positivos)))

media = sum(valores_positivos) / len(valores_positivos)
print("{:.1f}".format(media))