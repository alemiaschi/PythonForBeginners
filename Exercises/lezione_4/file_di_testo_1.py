# USARE COME INPUT IL FILE DI TESTO: testo_1.txt

import sys

def main(doc):
    diz = {}
    file1 = open(doc, 'r', encoding='utf-8')
    contenuto = file1.readlines()
    for line in contenuto:
        elementi = line.rstrip('\n').split(' ')
        diz[elementi[0]] = int(elementi[1])
    print(diz)
    file1.close()

main(sys.argv[1])
