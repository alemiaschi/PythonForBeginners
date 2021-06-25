diz = {"Alessio": [21, 28, 30, 18],
       "Laura": [21, 20, 30, 30, 28, 25]}

for k, v in diz.items():
    if len(v) < 5:
        esami_mancanti = 5 - len(v)
        print("Lo studente", k, "non ha raggiunto il numero minimo di esami. Numero di esami mancati:",
              esami_mancanti)
    else:
        media = 0.0
        for voto in v:
            media+=voto
        media = media / len(v)
        print(k, media)