frase = "Questo è un esercizio"
nuova_frase = ""

for car in frase:
    if car == " ":
        nuova_frase+="_"
    else:
        nuova_frase+=car

print(nuova_frase)