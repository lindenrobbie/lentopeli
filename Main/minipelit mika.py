import random

def donalduck():
    print("Lentokentän kahviossa edessä olevalta lapselta puuttuu pillimehusta rahaa 2 euroa.")

    while True:
        #toistuu kunnes käyttäjä vastaa kyllä tai ei
        question = input("Haluatko antaa puuttuvan rahan? (Kyllä / Ei)").lower()

        if question == "kyllä":
            if random.randint(1,10) == 1:
                print("Tehtävä epäonnistui, pillimehu tippui lapsen kädestä maahan ja meni rikki ;(")
            else:
                print("Saat palkinnoksi perheeltä kiiltävän Aku Ankka pinssin")

        elif question == "ei":
            print("Etenet seuraavaan paikkaan menettämättä rahaa mutta kuulet surullisen lapsen itkua!!! ")

        else:
            print("Annoit virheellisen vastauksen")
            continue #ohittaa break komennon jos käyttäjä ei vastaa oikein

        break

def carddraw():
    return
    while True:
        print("Vieressä istuva aussi Hugh Jackman on tylistymässä kuoliaaksi ja "
            "haastaa sinut pelaamaan kortin vetoa, isoin kortti voittakoon!")
        player1 =random.randint(2,14)
        player2 =random.randint(2,14)
        if player1==player2:
            coin=input(print("Ratkaistaan voittaja kolikolla, kruuna vai klaava?:  "))
        if coin=="kruuna":
            coin=1
        if coin=="klaava":
            coin=2
        else:
            print("Valitse kruuna tai klaava")
        continue  # ohittaa break komennon jos käyttäjä ei vastaa oikein
        random2=random.randint(1,2)
        if coin==random2:
            print("Arvasit oikein ja voitit!!")
        else:
            print("Voihan mielipaha arvasit väärin, hävisit tolle charmantille aussille!")

        if player1>player2:
            print(f"Hugh Jackmanin kortti: {player1} sinun korttisi {player2}")
            print(f"Hugh Jackman voitti kortilla: {player1}. Äläkä ala mököttää, tapasit sentään charmantin julkkiksen ^_^  !")
        else:
            print(f"Pelaaja (tähän pelaajan nimimerkki) voitti Hugh Jackmanin.\nPalkinnoksi sait wolverinen muoviset raateluterät. Oiva lahja siskon pojalle! Pisteesi kerrotaan kertoimella 1.2!")


points=100
repeats=0
def words():
      return
print("Pikkuvanha Elviira-Elise haluaa näpäyttää sinua ja pyytää laittamaan seuraavat sanat käänteiseen järjestykseen takaperin.\n"
      "'Python on kivaa vai mita'")
while True:
      add=(input("Anna vastaus: "))
      if add =="atsunim ikaniav aon no nohtyp":
            print(f"Onnistuit ja saat {points} pistettä, Pikkuvanha katsoo huulipyöreenä ja taputtaa kunnioittavasti")
            break
      else:
            repeats+=1
            points -=20
            print("Menetit potista pisteitä ja yrityä uudelleen","Yrityksiä",repeats, "Pisteitä saatavilla",points)
      if repeats == 5:
            print("Et onnistunut voi pöhköliini <3 Pikkuvanha osasi sua paremmin!")
            break
words()
