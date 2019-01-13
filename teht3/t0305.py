# -*- coding: utf-8 -*
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
print("""(1) +
(2) -
(3) *
(4) /""")
valinta = input("Tee valinta (1-4): ")
if valinta == "1":
    print("tulos on:", luku1 + luku2)
elif valinta == "2":
    print("tulos on:", luku1 - luku2)
elif valinta == "3":
    print("tulos on:", luku1 * luku2)
elif valinta == "4":
    print("tulos on:", luku1 / luku2)
else:
    print("valintaa ei tunnistettu.")
