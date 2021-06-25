stringa = input("Inserisci stringa: ")
nuova_stringa = ""

lunghezza = len(stringa)-1

while lunghezza >= 0:
    nuova_stringa+=stringa[lunghezza]
    lunghezza-=1

if stringa == nuova_stringa:
    print("La stringa è palindroma!")
else:
    print("La stringa NON è palindroma")
