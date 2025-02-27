import random
import main

def minigame_pummi():

    print("")
    print("Näät lentokentässä pummin joka pyytää sinulta rahaa ruokaan")
    print('Annatko pummille (x määrä) rahaa? Kyllä/En')

    while True:

        print("")
        r = input('')

        chance = random.randint(1, 10)

        if chance in range(1, 3):
            win = True
        else:
            win = False

        if r == 'En':
            print("")
            print("Jatkat matkaasi seuraavaan lentoon pikaisesti ja näät silmänkulmassasi kun pummi surullisesti tärisee nälästä")
            break

        elif r == 'Kyllä':
                #deduct fee to agree to minigame

            if win == True:
                print("")
                print(f'Pummi oli sosiaalisen median vaikuttaja ja hän palkitsi sinut PISTEET sinun kiltteydestäsi.')
                break
                #insert a win reward here

            elif win == False:
                print("Pummi kiitti nauraen ja hyväksikäytti sinisilmäistä anteliaisuuttasi.")
                break

        else:
            print("Älä ignooraa pummia... :(")

def minigame_roulette():
    print("")

    def roulette_odds(color):

        black = (0, 48.5)
        red = (48.5, 97)
        green = (97, 100)

        odds = float(random.randint(0, 100))

        if black[0] <= odds < black[1]:
            return "black"

        elif red[0] <= odds < red[1]:
            return "red"

        elif green[0] <= odds < green[1]:
            return "green"
    print("")
    print("Saavuit suureen Casino Wien:iin ja edessäsi on rulettipöytä.")
    print("Pöydässä on tilaa pelata, liitytkö joukkoon? Kyllä/En")

    while True:

        print("")
        r = input('')

        if r == 'En':
            print("")
            print('Olet viisas ja ymmärrät että uhkapelaamisesta 𝐚𝐢𝐧𝐚 seuraa jotain pahaa.')
            print('Jatkat matkaa seuraavaan kenttään...')
            break

        elif r == 'Kyllä':

            pisteet = main.pisteet

            print("")
            print("Kasinon työntekijä pyytää sinulta panosta.")
            print("Paljon laitat panosta?")
            print(f"Sinulla on käytössäsi {pisteet}")

            print("")

            while True:
                print("")
                print("Jos haluat lopettaa syötä 'Lopeta'")
                bet = input('Syötä panos: ')

                if bet == 'Lopeta':
                    print("")
                    print("Päätit olla fiksu ja lopettaa ennen kuin menetät kaikki rahat.")
                    break

                # Validate if the bet is an integer
                if not bet.isdigit() or bet == 0:
                    print("Syötä numero!")
                    continue

                bet = int(bet)  # Convert to integer

                if bet > pisteet:
                    print("Sinulla ei ole tarpeeksi pisteitä!")
                    print("Syötä oikea määrä pisteitä")

                elif bet <= pisteet:
                    print("")
                    print('Valitse väri (Kirjoita green/red/black tai syötä tyhjä kenttä sulkeaksi): ')

                    while True:

                        print("")
                        usercolor = input('').strip().lower()

                        color = roulette_odds('')

                        if usercolor not in ('red', 'green', 'black'):
                            print("")
                            print("Syötä valiidi väri (green/red/black)")
                            continue  # Loops back if color is invalid

                        #lose sequence
                        if usercolor != color:
                            pisteet = pisteet - bet
                            print("")
                            print('Womp womp... Hävisit :D')
                            print(f"Pisteitä on nyt {pisteet}")
                            break

                        #green win sequence
                        elif color == 'green':
                            bet = bet * 36
                            pisteet = pisteet + bet
                            print(f'Winner winner! Onnittelut! Pisteitä on nyt {pisteet}. Nice')
                            break

                        #general (black/red) win sequence
                        elif color == 'black' or 'red':
                            bet = bet * 2
                            pisteet = pisteet + bet
                            print(f"Hienoa! Voitit tuplamäärän! Pisteitä on nyt {pisteet}!")
                            break

minigame_roulette()
