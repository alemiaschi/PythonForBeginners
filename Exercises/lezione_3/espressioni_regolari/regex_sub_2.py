import re

def main():
    stringa = input("Inserisci una stringa: ")
    nuovaStringa = re.sub(r'\b[AEIOUaeiou]\w{3,}\b', r'WORD', stringa)
    print(nuovaStringa)

main()
