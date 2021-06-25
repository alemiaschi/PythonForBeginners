import re

def main():
    stringa = input("Inserisci una stringa: ")
    nuovaStringa = re.sub(r'(\d)(\d*)(\d)', r'\3\2\1', stringa)
    print(nuovaStringa)

main()
