import random

#palauttaa käyttäjän syöttämän vastauksen
#esimerkiksi: query("question", ["1. answer1", "2. answer2", "3. answer3"], ["1", "2", "3"])
#palautaa 1, 2 tai 3 merkkijonon
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
        
        print("annoit väärän vastauksen")


#Ville minipeli 1
def late():
    print("Olet myöhästymässä lentokoneestasi!")
    print("Joudut improvisoimaan jotta kerkeät lennolle")
    print("Valitse jokin seuraavista vaihtoehdoista:")

    choise = query("Olet myöhästymässä lentokoneestasi!\nJoudut improvisoimaan jotta kerkeät lennolle", #kysymys
                   ["1: Juokse turvatarkastuksen", "2: Lainaa golfkärryn näköistä ajoneuvoa", "3: Pyydä apua henkilökunnalta"], #esitettävät vastaukset
                   ["1", "2", "3"]) #vastaukset

    if choise == "1":
        if random.randint(1,10) == 1:
            print ('Pääsit kuin ihmeen kaupalla livahtamaan tarkastuksen läpi.\n\nKerkesit lennolle ja ansaitsit 100 lisäpistettä!')
        else:
            print ('Turvatarkastus otti sinut kiinni joten myöhästyit lennoltasi.\n\nMenetit 100 pistettä.')

    if choise == "2":
        if random.randint(1, 5) == 1:
            print ('Sait ajoneuvolla kirittyä aikataulusi kuntoon ja kerkesit lennollesi!\n\nAnsaitsit 50 lisäpistettä.')
        else:
            print ('Törmäsit ajoneuvolla terminaalissa pylvääseen...\n\nMyöhästyit lennoltasi ja menetät 50 pistettä.')

    if choise == "3":
        if random.randint(1,2) == 1:
            print ('Henkilökunta viivästytti lentoa ja kerkesit matkaan mukaan!\n\nAnsaitsit 25 pistettä.')
        else:
            print ('Henkilökunta ei ymmärtänyt kieltäsi.\n\nMyöhästyit lennoltasi ja menetit 25 pistettä.')

late()

#Ville Minipeli 2
def frankfurt():
    print ('Vuokraat auton lentokentältä jotta pääset airbnb majoitukseesi')
    print ('Jostain syystä frankfurtissa on tarjolla vain BMW, Mercedes-benz tai Porsche')

    #kysymys 1
    while True:
        answer = input('Mikä näistä valmistajista on valmistanut ensimmäisenä pidetyn modernin auton?\n\n1. BMW\n2. Mercedes-benz\n3. Porsche\n\nVastauksesi: ')

        if answer == '2':
            print('Oikein vastattu! Ansaitsit 25 pistettä.')
            break
        elif answer == '1' or answer == '3':
            print('Vastasit väärin. Et ansainnut pisteitä')
            break
        else:
            print('Syötä numerovaihtoehto 1,2 tai 3!')

    #kysymys 2
    while True:
        answer = input('Kuinka pitkän matkan BMW driftasi maailmanennätysksen rikkoneessa ajassa 8 tuntia\n\n1. 374 km\n2. 618 km\n3. 112km\n\nVastauksesi: ')

        if answer == '1':
            print('Oikein vastattu! Ansaitsit 25 pistettä.')
            break
        elif answer == '2' or answer == '3':
            print('Vastasit väärin. Et ansainnut pisteitä')
            break
        else:
            print('Syötä numerovaihtoehto 1,2 tai 3!')

    #kysymys 3
    while True:
        answer = input('Millä seuraavista porschen malleista on nurburgringin sports cars luokan rataennätys?\n\n1. Porsche 911 GT3 RS\n2. Porsche 991  GT2 RS (Manthey performance kit)\n3. Porsche 718 GT4 RS (Manthey kit)\n\nVastauksesi: ')

        if answer == '2':
            print('Oikein vastattu! Ansaitsit 25 pistettä.')
            break
        elif answer == '1' or answer == '3':
            print('Vastasit väärin. Et ansainnut pisteitä')
            break
        else:
            print('Syötä numerovaihtoehto 1,2 tai 3!')


#Ville Minipeli 3
def stockholm():
    print("Eksyit laskettelemaan perinteistä telemarkkia!")
    print('Tavoitteenasi on laskea rinne alas saakka väistellen esteitä')
    start=input('Paina enter aloittaaksesi:')

    while start != '':
        start = input('Paina enter aloittaaksesi:')

    rounds= 0
    while rounds <= 5:
        obst= random.randint(1,3)

        if obst == 1:
            treeput= input('Edessäsi on puu. Väistä vasemmalta painamalla A tai oikealta painamalla D: ')
            if treeput == 'd':
                print('Väistit puun ')
                rounds += 1
            else:
                print('Ajauduit ulos rinteeltä ja kaaduit')
                break

        if obst == 2:
            treeput= input('Tielläsi on kivi. Hyppää painamalla H tai kyyristy painamalla K: ')
            if treeput == 'h':
                print('Hyppäsit kiven yli!')
                rounds += 1
            else:
                print('Kaaduit kiveen')
                break

        if obst == 3:
            treeput= input('Edessäsi roikkuu oksa matalalla. Kyyristy painamalla K tai hyppää painamalla H: ')
            if treeput == 'k':
                print('Mahduit oksan ali ja jatkat matkaa!')
                rounds += 1
            else:
                print('Osuit oksaan ja loukkaannuit')
                break

    if rounds >= 5:
        print('Pääsit turvallisesti afterski juhliin!')

    else:
        print('Et päässyt alas saakka joten et saa pisteitä.')


#Mika minipeli 1
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


#Mika minipeli 2
def carddraw():
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


#Mika minipeli 3
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


#Robbie minipeli 1
def pummi():

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


#Robbie minipeli 2
def roulette():
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
