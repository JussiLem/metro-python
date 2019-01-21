# -*- coding: utf-8 -*
def toinenpotenssi(arvo):
    tulos = arvo ** 2
    print("Toinen potenssi on", tulos)

def main():
    lukuarvo = int(input("Anna lukuarvo: "))
    toinenpotenssi(lukuarvo)


if __name__ == "__main__":
    main()
