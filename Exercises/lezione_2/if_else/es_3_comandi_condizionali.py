lista = [5, 6, 8, 10, 12]
num = input("Inserisci un numero: ")

num = int(num)

if lista[0] == num:
    print("Il primo numero della lista corrisponde al numero inserito!")
else:
    print("I due numeri non corrispondono. Il primo numero della lista è: ", lista[0])
