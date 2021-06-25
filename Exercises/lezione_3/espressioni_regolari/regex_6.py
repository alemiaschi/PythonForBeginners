import re

def main():
    stringa = input("Inserisci una stringa: ")
    #lista_match = re.findall(r'\s\d\d[-/]\d\d[-/]\d\d\d\d', stringa)
    lista_match = re.findall(r'\s[0-3]?\d[-/][01]?\d[-/][0-2]?\d?\d?\d\s', stringa)
    for match in lista_match:
        print(match)

main()
