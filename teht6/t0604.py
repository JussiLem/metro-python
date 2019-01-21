# -*- coding: utf-8 -*
def pituusmitta(merkkijono=""):
    if merkkijono != "":
        pituus = int(len(merkkijono))
        return pituus
    else:
        return 0


def main():
    while True:
        valinta = input("Anna syöte (Lopeta lopettaa): ")
        if "lopeta" in valinta.casefold():
            return 0
        elif len(valinta) == 0:
            print("Et antanut syötettä")
        else:
            print("Antamasi syöte oli", pituusmitta(valinta), "merkkiä pitkä.")


if __name__ == "__main__":
    main()
