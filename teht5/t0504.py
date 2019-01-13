# -*- coding: utf-8 -*
tiedostonNimi = "muistio.txt"
try:
    while True:
        print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n"
              "(4) Lopeta")
        valinta = input("Mitä haluat tehdä?: ")
        if valinta == "4":
            print("Lopetetaan.")
            break
        elif valinta == "1":
            tiedosto = open(tiedostonNimi, 'r')
            luettuTeksti = tiedosto.read()
            luettuTeksti.strip()
            print(luettuTeksti)
            tiedosto.close()
        elif valinta == "2":
            tiedosto = open(tiedostonNimi, 'a')
            muistio = input("Kirjoita uusi merkintä: ")
            tiedosto.write(muistio + "\n")
            tiedosto.close()
        elif valinta == "3":
            tiedosto = open(tiedostonNimi, 'w').close()
            print("Muistio tyhjennetty.")
        else:
            print("Valintaa ei tunnistettu.")
except IOError:
    print("tiedoston käsittelyssä virhe")
