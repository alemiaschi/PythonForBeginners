a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 11]

nuova_lista = []
if len(a) != len(b):
    print("Le due liste hanno lunghezza diversa")
else:
    i = 0
    while i < len(a):
        if i == 5:
            break
        somma = a[i] + b[i]
        nuova_lista.append(somma)
        i+=1

    print(nuova_lista)
