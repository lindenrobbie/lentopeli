def minigame_pummi():
    print("\nNäät lentokentässä pummin joka pyytää sinulta rahaa ruokaan")
    print('Annatko pummille (x määrä) rahaa? Kyllä/En')

    while True:
        print("")
        r = input('').strip()

        if r in ["Kyllä", "En"]:
            break
        print("Vastaa Kyllä/En")

    chance = random.randint(1, 10)
    win = chance in range(1, 3)

    if r == 'En':
        print(
            "\nJatkat matkaasi seuraavaan lentoon pikaisesti ja näät silmänkulmassasi kun pummi surullisesti tärisee nälästä")
    elif r == 'Kyllä':
        if win:
            print("\nPummi oli sosiaalisen median vaikuttaja ja hän palkitsi sinut PISTEET sinun kiltteydestäsi.")
        else:
            print("Pummi kiitti nauraen ja hyväksikäytti sinisilmäistä anteliaisuuttasi.")