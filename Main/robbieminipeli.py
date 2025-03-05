import random


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


def minigame_roulette():
    print("\nSaavuit suureen Casino Wien:iin ja edessäsi on rulettipöytä.")
    print("Pöydässä on tilaa pelata, liitytkö joukkoon? Kyllä/En")

    pisteet = 100
    pelit = 0

    while True:
        print("")
        r = input('').strip()

        if r in ["Kyllä", "En"]:
            break
        print("Vastaa Kyllä/En")

    if r == 'En':
        print("\nOlet viisas ja ymmärrät että uhkapelaamisesta 𝐚𝐢𝐧𝐚 seuraa jotain pahaa.")
        pisteet += 50
        print('+50 Pistettä')
        print('Jatkat matkaa seuraavaan kenttään...')
        print(f'Pisteesi ovat nyt: {pisteet}')
        return

    def roulette_odds():
        black = (0, 48.5)
        red = (48.5, 97)
        green = (97, 100)
        odds = float(random.randint(0, 100))
        if black[0] <= odds < black[1]:
            return "black"
        elif red[0] <= odds < red[1]:
            return "red"
        else:
            return "green"

    print("\nKasinon työntekijä pyytää sinulta panosta.")
    print(f"Sinulla on käytössäsi {pisteet} pistettä.")

    while pisteet > 0 and pelit < 3:
        print("\nJos haluat lopettaa, syötä 'Lopeta'")
        bet = input('Syötä panos: ').strip()

        if bet.lower() == 'lopeta':
            print("\nPäätit olla fiksu ja lopettaa ennen kuin menetät kaikki rahat.")
            break

        if not bet.isdigit() or int(bet) <= 0:
            print("Syötä positiivinen numero!")
            continue

        bet = int(bet)
        if bet > pisteet:
            print("Sinulla ei ole tarpeeksi pisteitä! Syötä oikea määrä pisteitä.")
            continue

        print("\nValitse väri (Kirjoita green/red/black): ")
        while True:
            usercolor = input('').strip().lower()
            if usercolor in ['red', 'green', 'black']:
                break
            print("Syötä valiidi väri (green/red/black)")

        color = roulette_odds()

        if usercolor != color:
            pisteet -= bet
            print("\nWomp womp... Hävisit :D")
        elif color == 'green':
            bet *= 36
            pisteet += bet
            print(f'Winner winner! Onnittelut! Pisteitä on nyt {pisteet}. Nice')

        else:
            bet *= 2
            pisteet += bet
            print(f"Hienoa! Voitit tuplamäärän! Pisteitä on nyt {pisteet}!")

        pelit += 1
        if pelit >= 3:
            break

        print(f"Pisteitä on nyt {pisteet}")
        if pisteet <= 0:
            print("Sinulta loppui pisteet ja hävisit pelin. :|")
            break


minigame_roulette()
