# USARE COME INPUT IL FILE DI TESTO: testo_2.txt

import sys

def main(doc):
    file1 = open(doc, 'r', encoding='utf-8')
    output = open('output_1.txt', 'w', encoding='utf-8')
    contenuto = file1.readlines()
    for line in contenuto:
        elemento = line.rstrip('\n')
        lunghezza = len(elemento)
        stringa = elemento + ', lunghezza = ' + str(lunghezza) + '\n'
        output.write(stringa)
    file1.close()
    output.close()

main(sys.argv[1])
