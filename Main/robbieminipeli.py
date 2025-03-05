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

    points = 100
    games = 0

    while True:
        print("")
        r = input('').strip()

        if r in ["Kyllä", "En"]:
            break
        print("Vastaa Kyllä/En")

    if r == 'En':
        print("\nOlet viisas ja ymmärrät että uhkapelaamisesta 𝐚𝐢𝐧𝐚 seuraa jotain pahaa.")
        points += 50
        print('+50 Pistettä')
        print('Jatkat matkaa seuraavaan kenttään...')
        print(f'Pisteesi ovat nyt: {points}')
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
    print(f"Sinulla on käytössäsi {points} pistettä.")

    while points > 0 and games < 3:
        print("\nJos haluat lopettaa, syötä 'Lopeta'")
        bet = input('Syötä panos: ').strip()

        if bet.lower() == 'lopeta':
            print("\nPäätit olla fiksu ja lopettaa ennen kuin menetät kaikki rahat.")
            break

        if not bet.isdigit() or int(bet) <= 0:
            print("Syötä positiivinen numero!")
            continue

        bet = int(bet)
        if bet > points:
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
            points -= bet
            print("\nWomp womp... Hävisit :D")
        elif color == 'green':
            bet *= 36
            points += bet
            print(f'Winner winner! Onnittelut! Pisteitä on nyt {points}. Nice')

        else:
            bet *= 2
            points += bet
            print(f"Hienoa! Voitit tuplamäärän! Pisteitä on nyt {points}!")

        games += 1
        if games >= 3:
            print(f'Pisteitä on nyt {points}')
            break

        print(f"Pisteitä on nyt {points}")
        if points <= 0:
            print("Sinulta loppui pisteet ja hävisit pelin. :|")
            break



