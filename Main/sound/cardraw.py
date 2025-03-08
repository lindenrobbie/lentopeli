import random
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


def minigame_carddraw():

    print("Vieressä istuva aussi Hugh Jackman on tylistymässä kuoliaaksi "
        "ja haastaa sinut pelaamaan kortin vetoa, isoin kortti voittakoon!")
    player_hugh = random.randint(2,14)
    player_player = random.randint(2,14)
    print("Charmantin aussin kortin arvo on ",player_hugh)
    print("Sinun korttisi arvo on ", player_player)
    if player_player < player_hugh:
        print("Hävisit aussin korteille, et ansainnut pisteitä tästä tehtävästä! Mutta äläpä mutrua, \n"
              "tapasit sentään charmantin julkkiksen <3")
    if player_player > player_hugh:
        print("Voitit korteillasi, sait palkinnoksi semipäheet Wolwerinen raateluhanskat. Oiva lahja siskon pojalle!\n"
              "Pisteesi kerrotaan 1,2")
        #kerro pisteet scoreboard
    if player_player==player_hugh:
        print("Teillä on samat kortit ja voittaja arvotaan kolikon heitolla")
        question = query("Valitsetko kruunan vai klaavan?",
                         ["1: Kruuna",
                          "2: Klaava"],
                         ["1", "2"])
        if question == "1" :
            coin = 0
            coin += random.randint(1, 2)
            if coin == 1 :
                print("Tuli kruuna")
                print("Arvasit oikein ja voitit. Sait palkinnoksi semipäheet Wolwerinen raateluhanskat.\nOiva lahja siskon pojalle!"
              "Pisteesi kerrotaan 1,2"
                      "")
            else:
                print(" Tuli klaava ja arvasit väärin. Hugh Jackman voitti. Älä Sure Tapasit sentään ihanan julkkiksen!")
        if question =="2":
            coin = 0
            coin+=random.randint(1,2)
            if coin == 2:
                print("Tuli Klaava")
                print("Arvasit oikein ja voitit tämänkin erän. Sait palkinnoksi semipäheet Wolwerinen raateluhanskat.\nOiva lahja siskon pojalle!"
              "Pisteesi kerrotaan 1,3"
                      "")

            else:
                print(
                    "Tuli kruuna, arvasit väärin! Hugh Jackman voitti. Älä sure, tapasit sentään charmantin aussin <3")

minigame_carddraw()