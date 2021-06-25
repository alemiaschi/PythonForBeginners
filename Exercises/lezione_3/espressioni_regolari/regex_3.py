import re

def main():
    stringa = input("Inserisci una stringa: ")
    lista_match = re.findall(r'\w+[.,;:!?]\s', stringa)
    for match in lista_match:
        print(match)

main()
