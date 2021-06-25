lista = [10, 15, 34, 33, 76, 150, 50, 10]

for numero in lista:
    if numero >= 150:
        break
    if numero%5 == 0:
        print(numero)