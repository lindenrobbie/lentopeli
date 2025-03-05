import random
#Minipeli_donaldduck
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
#minipeli_carddraw
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


#minipeli_WORDS
def words():
    points=100
    repeats=0
    print("Pikkuvanha Elviira-Elise haluaa näpäyttää sinua ja pyytää laittamaan seuraavat sanat käänteiseen järjestykseen takaperin.\n"
        "'Python on kivaa vai mita'")
    while True:
        add=(input("Anna vastaus: "))
        if add =="atim iav aavik no nohtyP":
                print(f"Onnistuit ja saat {points} pistettä, Pikkuvanha katsoo huulipyöreenä ja taputtaa kunnioittavasti")
                break
        else:
                repeats+=1
                points -=20
                print("Menetit potista pisteitä ja yrityä uudelleen","Yrityksiä",repeats, "Pisteitä saatavilla",points)
        if repeats == 5:
                print("Et onnistunut voi pöhköliini <3 Pikkuvanha osasi sua paremmin!")
                break

#Minipeli_ ART
def query(question: str, options: list, answers: list):
    print(question)
    print("Valitse jokin seuraavista vaihtoehdoista: ", end="")
    for i in options:
        print(i + " / ", end="")
    print()

    while True:
        input_answer = input()

        for i in answers:
            if input_answer == i:
                return input_answer

        print("Annoit muun vaihtoehdon kuin kysymyksessä, yritä uudelleen")
points=0
question = query ("Mikä on Da Vincin koko nimi ?",
                ["1: Leonardo di ser Piero da Vinci", "2: Leonardo Alfred da Vinci","CC: Leonardo si Pedro da Vinci"],
                  ["1","2","3"])
if question =="1":
    print("Sait vastauksen oikein ja ansaitset +15 pistettä!")
    points += 15
    print("Pisteesi ovat:",points)
else:
    print("Vastasit väärin ja menetät -5 pistettä!")
    points -= 5
    print("Pisteesi ovat:",points)
question = query ("Minkä ikäisenä Da vinci kuoli ?",
                ["1: 52 vuotiaana", "2: 73 vuotiaana","3: 67 vuotiaana"],
                  ["1","2","3"])
if question =="3":
    print("Sait vastauksen oikein ja ansaitset +15 pistettä!")
    points += 15
    print("Pisteesi ovat:", points)
else:
    print("Vastasit väärin ja menetät -5 pistettä!")
    points -= 5
    print("Pisteesi ovat:", points)

question = query ("Mikä on Rooman jalkapallojoukkuuen virallinen nimi ?",
                ["1: As Roma", "2: Fc Roma","3: 67 F.C Roma"],
                  ["1","2","3"])
if question =="1":
    print("Sait vastauksen oikein ja ansaitset +15 pistettä!")
    points += 15
    print("Pisteesi ovat:", points)
else:
    print("Vastasit väärin ja menetät -5 pistettä!")
    points -= 5
    print("Pisteesi ovat:", points)

question = query ("Missä taideteos Mona Lisa on näytillä ?",
                ["1: Louvre in paris", "2: International museum of Roma","3: Brittish Museum"],
                  ["1","2","3"])
if question =="1":
    print("Sait vastauksen oikein ja ansaitset +15 pistettä!")
    points += 15
    print("Pisteesi ovat:", points)
else:
    print("Vastasit väärin ja menetät -5 pistettä!")
    points -= 5
    print("Pisteesi ovat:", points)

question = query ("Paljonko on roomalainen luku MMXXV ?",
                ["1: 0022", "2: 2210","3: 2025"],
                  ["1","2","3"])
if question =="3":
    print("Sait vastauksen oikein ja ansaitset +15 pistettä!")
    points += 15
    print("Pisteesi ovat:", points)
else:
    print("Vastasit väärin ja menetät -5 pistettä!")
    points -= 5
    print("Pisteesi ovat:", points)

question = query ("Mikä on seuraavista italialainen automerkki ?",
                ["1: Porche", "2: Seat","3: Alfa Romeo"],
                  ["1","2","3"])
if question =="3":
    print("Sait vastauksen oikein ja ansaitset +15 pistettä!")
    points += 15
    print("Pisteesi ovat:", points)
else:
    print("Vastasit väärin ja menetät -5 pistettä!")
    points -= 5
    print("Pisteesi ovat:", points)

question = query ("Kuuluuko ananas pizzaan?",
                ["1: Hell yeah!", "2: Ei todellakaan","3: Ihan sama kun pizza!"],
                  ["1","2","3"])
if question =="3" or question == "2" or question == "1":
    print("Sait vastauksen oikein, mielipiteistä ei voi kiistellä ja ansaitset +15 pistettä!")
    points += 15
    print("Pisteesi ovat:", points)
