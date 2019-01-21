# -*- coding: utf-8 -*
def tulosta(merkkijono="Oletustulostus"):
    print(merkkijono)


def main():
    while True:
        valinta = input("Anna syöte (Lopeta lopettaa): ")
        if len(valinta) >= 5 and "lopeta" not in valinta.casefold():
            tulosta(valinta)
        elif len(valinta) < 5:
            tulosta()
        elif "lopeta" in valinta.casefold():
            return 0


if __name__ == "__main__":
    main()
