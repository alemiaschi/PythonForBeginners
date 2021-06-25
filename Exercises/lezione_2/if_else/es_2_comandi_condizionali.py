stringa = input("Inserisci una stringa: ")

vocali = ['a', 'e', 'i', 'o', 'u']
carattere = stringa[0]

if carattere in vocali:
    print("La stringa inizia con una vocale!")
else:
    print("La stringa non inizia con una vocale!")
