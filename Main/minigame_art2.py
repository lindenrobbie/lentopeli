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

def minigame_art2():
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

    question = query ("Kuuluuko ananas pizzaan?",
                    ["1: Hell yeah!", "2: Ei todellakaan","3: Ihan sama kun pizza!"],
                      ["1","2","3"])
    if question =="3" or question == "2" or question == "1":
        print("Sait vastauksen oikein, mielipiteistä ei voi kiistellä ja ansaitset +15 pistettä!")
        points += 15
        print("Pisteesi ovat:", points)


