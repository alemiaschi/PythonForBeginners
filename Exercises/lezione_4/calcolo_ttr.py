# USARE COME INPUT IL FILE DI TESTO: documento.txt

import sys


def main(doc):
    file1 = open(doc, 'r', encoding='utf-8')
    data = file1.readlines()

    all_words = []
    for line in data:
        frasi = line.rstrip('\n').split('. ')
        for frase in frasi:
            parole = frase.split(" ")
            for parola in parole:
                if parola != '':
                    all_words.append(parola)

    vocabolario = list(set(all_words))
    ttr = len(vocabolario) / len(all_words)
    print("La Type/Token Ratio del file è: ", ttr)


main(sys.argv[1])
