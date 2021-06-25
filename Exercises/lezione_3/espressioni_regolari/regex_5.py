import re

def main():
    stringa = input("Inserisci una stringa: ")
    #lista_match = re.findall(r'\s(?:ho|hai|ha|abbiamo|avete|hanno|Ho|Hai|Ha|Abbiamo|Avete|Hanno)\svisto\s', stringa)
    lista_match = re.findall(r'(?:[hH](?:o|ai|a|anno)|[Aa](?:bbiamo|vete))\svisto', stringa)
    for match in lista_match:
        print(match)

main()
