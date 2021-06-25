import re

def main():
    stringa = input("Inserisci una stringa: ")
    lista_match = re.findall(r'[aeiouAEIOU]', stringa)
    for match in lista_match:
        print(match)

main()
