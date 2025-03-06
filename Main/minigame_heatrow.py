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
        print("Annoit väärän vastauksen kysymykseen, yritä uudelleen")
import random

def minigame_heatrow():
    points = 0
    question = query("Laukkusi hajosi kentällä. Haluatko ostaa uuden laukun?",
                     ["1: Ostat laukun, menetät -20 pistettä mutta osallistut arvontaan", "2: Haluan koittaa järjestellä tavarat toiseen laukkuun"],
                     ["1", "2"])
    if question == "1":
        points += random.randint(1,6)
        if points >3:
            print ("Voitit arvonnasta kultaisen matkalaukun ja kerrot kokonaispisteesi 1,2 kertaisena")
        else:
            print("Menetit -20 pistettä mutta sait itsellesi tyylikkään Cavalierin mustan laukun kromatuilla kahvoilla!")
    if question == "2":
        print("Pienellä palikkatestillä saatat saada tavarat mahtumaan laukkuusi.")

    question = query("Paljonko on 9 kertaa 9 jaettuna 3 kertaa 9?",
                     ["1: 243",
                             "2: 234"],
                     ["1","2"])
    if question == "1":
        print("Vastasit oikein ja ansaitset 10 pistettä")
        points += 10
        print("Pisteesi ovat:",points)
    else:
        print("Vastasit väärin ja et saa pisteitä")

    if question == "2":
        print("Pienellä palikkatestillä saatat saada tavarat mahtumaan laukkuusi.")
    question = query("Lasketaanko suorakulmaisen kolmion hypotenuusan pituus seuraavalla kaavalla?",
                     ["1: Kateetit potenssiin 2 ja summataan. Summasta otetaan neliöjuuri?",
                             "2: Kateettit kerrotaan keskenään ja jaetaan kahdella?"],
                     ["1","2"])
    if question =="1":
        print("Vastasit oikein ja ansaitset 10 pistettä")
        points += 10
        print("Pisteesi ovat:", points)
    else:
        print("Vastasit väärin ja et saa pisteitä")

    question = query("Paljonko on 3 potenssiin 5?",
                     ["1: 333",
                      "2: 243"],
                     ["1", "2"])
    if question == "2":
        print("Vastasit oikein ja ansaitset 10 pistettä")
        points += 10
        print("Pisteesi ovat:", points)
    else:
        print("Vastasit väärin ja et saa pisteitä")

    question = query("Viimeinen tavara on hankalampi mutta voit koittaa saada tällä lentokentällä ansaitut pisteet kerrattua!\n"
                     "Mikä on luvun 27 kuutiojuuri jaettuna luvun 4 neliöjuurella",
                     ["1: 12?",
                      "2: 16?",
                      "3: 6?"],
                     ["1", "2", "3"])
    if question == "3":
        print("Vastasit oikein ja ansaitset kertoimen 5 tällä lentokentällä")
        points *=5
        print("Pisteesi ovat:", points)
    else:
        print("Vastasit väärin ja et saa pisteitä")

minigame_heatrow()