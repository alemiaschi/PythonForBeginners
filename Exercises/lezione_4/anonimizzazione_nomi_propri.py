# USARE COME INPUT IL FILE DI TESTO: documento.txt

import sys
import re

def main(doc):
    file1 = open(doc, 'r', encoding='utf-8')
    output = open('testo_anonimizzato.txt', 'w', encoding='utf-8')

    data = file1.readlines()
    for line in data:
        frasi = line.rstrip('\n').split('. ')
        for frase in frasi:
            nuova_frase = re.sub(r' \b[A-Z][a-z]*\b', ' NOME_PROPRIO', frase)
            output.write(nuova_frase + '\n')

    output.close()


main(sys.argv[1])
