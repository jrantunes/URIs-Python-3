#Average 2

def media(v1, v2, v3):
    res = ((v1 * 2) + (v2 * 3) + (v3 * 5)) / (2 + 3 + 5)
    return print("MEDIA = {:.1f}".format(res))

media(float(input()), float(input()), float(input()))