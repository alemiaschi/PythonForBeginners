prezzo = input("Inserisci prezzo del prodotto: ")
prezzo = float(prezzo)

sconto = (prezzo*25)/100
prezzo_nuovo = prezzo - sconto

print("L'importo da pagare è: ", prezzo_nuovo)
