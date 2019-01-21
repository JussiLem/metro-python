# -*- coding: utf-8 -*
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Vaihda luvut\n(6)Lopeta")
    print("Valitut luvut:", luku1, luku2)
    valinta = input("Tee valinta (1-6): ")
    if valinta == "6":
        break
    elif valinta == "5":
        luku1 = int(input("Anna uusi ensimmäinen luku: "))
        luku2 = int(input("Anna uusi toinen luku: "))
        continue
    else:
        if valinta == "1":
            print("Tulos on:", luku1 + luku2)
        elif valinta == "2":
            print("Tulos on:", luku1 - luku2)
        elif valinta == "3":
            print("Tulos on:", luku1 * luku2)
        elif valinta == "4":
            print("Tulos on:", luku1 / luku2)
        else:
            print("Valintaa ei tunnistettu.")
