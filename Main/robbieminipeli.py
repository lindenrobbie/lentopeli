import random
import gba_print
import sound
import pygame

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
    gba_print.slow_print("\nSaavuit suureen Casino Wien:iin ja edessäsi on rulettipöytä.")
    gba_print.slow_print("Pöydässä on tilaa pelata, liitytkö joukkoon? Kyllä/En")

    points = 100
    games = 0

    while True:
        gba_print.slow_print("")
        r = input('').strip()

        if r in ["Kyllä", "En"]:
            break
        gba_print.slow_print("Vastaa Kyllä/En")

    if r == 'En':
        gba_print.slow_print("\nOlet viisas ja ymmärrät että uhkapelaamisesta 𝐚𝐢𝐧𝐚 seuraa jotain pahaa.")
        points += 50
        gba_print.slow_print('+50 Pistettä')
        gba_print.slow_print('Jatkat matkaa seuraavaan kenttään...')
        gba_print.slow_print(f'Pisteesi ovat nyt: {points}')
        return

    def roulette_odds():
        black = (0, 48.5)
        red = (48.5, 97)
        green = (97, 100)
        odds = random.randint(0, 100)
        if black[0] <= odds < black[1]:
            return "black"
        elif red[0] <= odds < red[1]:
            return "red"
        else:
            return "green"

    gba_print.slow_print("\nKasinon työntekijä pyytää sinulta panosta.")
    gba_print.slow_print(f"Sinulla on käytössäsi {points} pistettä.")

    while points > 0 and games < 3:
        gba_print.slow_print("\nJos haluat lopettaa, syötä 'Lopeta'")
        bet = input('Syötä panos: ').strip()

        if bet.lower() == 'lopeta':
            gba_print.slow_print("\nPäätit olla fiksu ja lopettaa ennen kuin menetät kaikki rahat.")
            break

        if not bet.isdigit() or int(bet) <= 0:
            gba_print.slow_print("Syötä positiivinen numero!")
            continue

        bet = int(bet)
        if bet > points:
            gba_print.slow_print("Sinulla ei ole tarpeeksi pisteitä! Syötä oikea määrä pisteitä.")
            continue

        gba_print.slow_print("\nValitse väri (Kirjoita green/red/black): ")
        while True:
            usercolor = input('').strip().lower()
            if usercolor in ['red', 'green', 'black']:
                break
            gba_print.slow_print("Syötä valiidi väri (green/red/black)")

        color = roulette_odds()

        if usercolor != color:
            points -= bet
            gba_print.slow_print("\nWomp womp... Hävisit :D")
            sound.roulettelose().play()
            pygame.time.wait(500)

        elif color == 'green':
            bet *= 36
            points += bet
            gba_print.slow_print(f'Winner winner! Onnittelut! Pisteitä on nyt {points}. Nice')
            sound.roulettewin().play()
            pygame.time.wait(500)

        elif color == 'red' or color == 'black':
            bet *= 2
            points += bet
            gba_print.slow_print(f"Hienoa! Voitit tuplamäärän! Pisteitä on nyt {points}!")
            sound.roulettewin().play()
            pygame.time.wait(500)

        games += 1

        if points <= 0:
            sound.gameover().play()
            pygame.time.wait(1000)
            gba_print.slow_print("Sinulta loppui pisteet ja hävisit pelin. :|")
            input('Jatka painamalla enteriä')
            break

        if games >= 3:
            gba_print.slow_print(f'Pisteitä on nyt {points}')
            break

        gba_print.slow_print(f"Pisteitä on nyt {points}")

minigame_roulette()