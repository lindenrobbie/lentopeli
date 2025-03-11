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
        
        print("Anna validi vastaus!")


#Ville minipeli 1 "late"
def athens():
    print("Olet myöhästymässä lentokoneestasi!")
    print("Joudut improvisoimaan jotta kerkeät lennolle")
    print("Valitse jokin seuraavista vaihtoehdoista:")

    points=0

    choise = query("Olet myöhästymässä lentokoneestasi!\nJoudut improvisoimaan jotta kerkeät lennolle", #kysymys
                   ["1: Juokse turvatarkastuksen", "2: Lainaa golfkärryn näköistä ajoneuvoa", "3: Pyydä apua henkilökunnalta"], #esitettävät vastaukset
                   ["1", "2", "3"]) #vastaukset

    if choise == "1":
        if random.randint(1,10) == 1:
            print ('Pääsit kuin ihmeen kaupalla livahtamaan tarkastuksen läpi.\n\nKerkesit lennolle ja ansaitsit 100 lisäpistettä!')
            points+=100
        else:
            print ('Turvatarkastus otti sinut kiinni joten myöhästyit lennoltasi.\n\nMenetit 100 pistettä.')
            points-=100

    if choise == "2":
        if random.randint(1, 5) == 1:
            print ('Sait ajoneuvolla kirittyä aikataulusi kuntoon ja kerkesit lennollesi!\n\nAnsaitsit 50 lisäpistettä.')
            points+=50
        else:
            print ('Törmäsit ajoneuvolla terminaalissa pylvääseen...\n\nMyöhästyit lennoltasi ja menetät 50 pistettä.')
            points-=50

    if choise == "3":
        if random.randint(1,2) == 1:
            print ('Henkilökunta viivästytti lentoa ja kerkesit matkaan mukaan!\n\nAnsaitsit 25 pistettä.')
            points+=25
        else:
            print ('Henkilökunta ei ymmärtänyt kieltäsi.\n\nMyöhästyit lennoltasi ja menetit 25 pistettä.')
            points-=25
    return ["sum", points]



#Ville Minipeli 2
def frankfurt():
    print ('Vuokraat auton lentokentältä jotta pääset airbnb majoitukseesi')
    print ('Jostain syystä frankfurtissa on tarjolla vain BMW, Mercedes-benz tai Porsche')

    points=0

    #kysymys 1
    while True:
        answer = input('Mikä näistä valmistajista on valmistanut ensimmäisenä pidetyn modernin auton?\n\n1. BMW\n2. Mercedes-benz\n3. Porsche\n\nVastauksesi: ')

        if answer == '2':
            print('Oikein vastattu! Ansaitsit 25 pistettä.')
            points+=25
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
            points+=25
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
            points+=25
            break
        elif answer == '1' or answer == '3':
            print('Vastasit väärin. Et ansainnut pisteitä')
            break
        else:
            print('Syötä numerovaihtoehto 1,2 tai 3!')
    return ["sum", points]


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
        return ["sum", 100]

    else:
        print('Et päässyt alas saakka joten et saa pisteitä.')

#Paina enteriä jatkaaksesi
def enter_continue():
    while True:
        useri=input('Jatka painamalla enter: ')
        if useri == '':
            print('')
            break

#Ville Minipeli 4
def amsterdam():
    print('Ilmoittauduit pyöräilykilpailuun.')
    print('Valitse oikea pyörä oikeaan tilanteeseen')
    enter_continue()

    # Startti
    print('|Lähtopäikalta lähdetään kiihdyttämään|\n')
    bikechoise = query('Valitse pyöräsi seuraavista',
                                 ['1. Trek katupyörä', '2.Specialized DH pyörä', '3.Helkaman mummis',
                                  '4.Orbea sähköpyörä'], ['1', '2', '3', '4'])

    if bikechoise == '1':
        print('Katupyörä kiihtyy hitaasti mutta saavuttaa kovan nopeuden aikanaan')
    if bikechoise == '2':
        print('Polkemisesta häviää voima jousitukseen ja jäät jälkeen')
    if bikechoise == '3':
        print('Keulit mummiksella kisan kärkeen!')
    if bikechoise == '4':
        print('Painat kaasua ja pääset kärkikahinoihin ilman hikikarpaloita')

    print('')

    # Ylämäki
    print('|Saavut jyrkkään ylämäkeen|')
    enter_continue()
    bikechoise = query('Valitse pyöräsi seuraavista',
                                 ['1. Trek katupyörä', '2.Specialized DH pyörä', '3.Helkaman mummis',
                                  '4.Orbea sähköpyörä'], ['1', '2', '3', '4'])

    if bikechoise == '1' or bikechoise == '2':
        print('Vaihdat vaihdetta pienempään ja pääset mäen ylös')
    if bikechoise == '3':
        print('Mummiksesta loppuu vaihteet ja joudut taluttamaan mäen ylös')
    if bikechoise == '4':
        print('Liidät mäen ylös sähkön voimalla')
    enter_continue()

    # Alamäki
    print('|Edessäsi on jyrkkä ja epätasainen alamäki|')
    enter_continue()
    bikechoise = query('Valitse pyöräsi seuraavista',
                                 ['1. Trek katupyörä', '2.Specialized DH pyörä', '3.Helkaman mummis',
                                  '4.Orbea sähköpyörä'], ['1', '2', '3', '4'])

    if bikechoise == '1' or bikechoise == '4':
        while True:
            walk = input('Talutatko pyörän alas?\nkyllä/ei')
            if walk == 'kyllä':
                print('pääset hitaasti mäen taluttamalla alas')
                break
            if walk == 'ei':
                print('Kaadut alamäessä ja pyöräsi hajosi')
                return ["sum", -50]

    if bikechoise == '2':
        print('Lennät epätasaisuuksien yli jousituksesi avulla kisan kärkeen')

    if bikechoise == '3':
        print('Ryskäät mummiksella mäen alas mutta vanne menee kieroon')
    enter_continue()

    # Mutka
    print('|Tulet alamäen jälkeen mutkaan|')
    enter_continue()
    bikechoise = query('Valitse pyöräsi seuraavista',
                                 ['1. Trek katupyörä', '2.Specialized DH pyörä', '3.Helkaman mummis',
                                  '4.Orbea sähköpyörä'], ['1', '2', '3', '4'])

    if bikechoise == '3':
        print('Jalkajarru ei ole riittävän tehokas ja törmäät kaiteeseen')
    else:
        print('Levyjarrut hidastivat sinua tarpeeksi ja selvisit mutkasta\n|Pääsit maaliin saakka!|')
        return ["sum", 100]

#Ville Minipeli 5
def zurich():
    print('Matkaat zurichiin tallettamaan käteisvarojasi')
    while True:
        try:
            money = int(input('Syötä talletettava rahamäärä: '))
            break
        except:
            pass

    bank = query(
        f'|Haluat tallettaa {money}€. Valitse seuraavista pankeista tili joka mielestäsi on tuottoisin hyvin pitkälle aikavälille|',
        ['1.Banque Heritage: 2.5% talletuskorko + 3% vuosikorko', '2.Bank SYZ: 1.5% talletuskorko + 4% vuosikorko',
         '3.Geneva Swiss Bank: 5.5% vuosikorko'],
        ['1', '2', '3'])

    if bank == '1':
        print('|Tämän pankin tilillä on paras tuotto lyhyellä aikavälillä.|')
        print('Tili ei kuitenkaan ole paras pitkälle tähtäimelle')
    if bank == '2':
        print('|Tämän pankin tili on ns. kultainen keskitie lyhyelle ja pitkälle tähtäimelle|')
        return print('Tili ei kuitenkaan ole paras pitkälle tähtäimelle')
    if bank == '3':
        print('|Tällä tilillä on paras vuosikorko joten se ylittää aikanaan toisten tilien talletuskoron hyödyn|')
        print('Valitsit oikean tilin ja sait 100 pistettä!')
        return ["sum", 100]


#Mika minipeli 1 "donalduck"
def helsinki():
    print("Lentokentän kahviossa edessä olevalta lapselta puuttuu pillimehusta rahaa 2 euroa.")

    while True:
        #toistuu kunnes käyttäjä vastaa kyllä tai ei
        question = input("Haluatko antaa puuttuvan rahan? (Kyllä / Ei)").lower()

        if question == "kyllä":
            if random.randint(1,10) == 1:
                print("Tehtävä epäonnistui, pillimehu tippui lapsen kädestä maahan ja meni rikki ;(")
            else:
                print("Saat palkinnoksi perheeltä kiiltävän Aku Ankka pinssin")
                return ["mult", 1.2]

        elif question == "ei":
            print("Etenet seuraavaan paikkaan menettämättä rahaa mutta kuulet surullisen lapsen itkua!!! ")

        else:
            print("Annoit virheellisen vastauksen")
            continue #ohittaa break komennon jos käyttäjä ei vastaa oikein

        break


#Mika minipeli 2 "carddraw"
def manchester():

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
                return ["mult", 1.2]
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
                return ["mult", 1.3]

            else:
                print(
                    "Tuli kruuna, arvasit väärin! Hugh Jackman voitti. Älä sure, tapasit sentään charmantin aussin <3")


#Mika minipeli 3 "words"
def charles():
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
        
    return ["sum", points]

#Mika minipeli 4
def london():
    print("london")
    return ["sum", 100]

#Mika minipeli 5
def rome():
    print("rome")
    return ["sum", -100]

#Mallorca minipeli
def mallorca():
    print(f'\nSaavuit ihanaan mallorcaan missä rannalla paistaa ihanasti aurinko.')
    print('Rannalla kävelyllä astuit epähuomiossa rantapallopeliturnauksen keskelle ja jouduit pelaajaksi kentälle.')

    def get_serve_type():
        return random.randint(1, 2)

    def score(teamscore, opponentscore):
        return print(f'\033[33m{teamscore} - {opponentscore}\033[0m')

    teamscore = 0
    opponentscore = 0

    while teamscore < 5 or opponentscore < 5:

        servetype = get_serve_type()

        if servetype == 1:
            print('\nPallo lentää \033[36mhitaasti\033[0m korkealle, miten syötät pallon takaisin? (\033[33m1\033[0m/\033[33m2\033[0m)')
            print('\033[33m1\033[0m Hitaasti takaisin vastustajalle')
            print('\033[33m2\033[0m Yritä lyödä pallo takaisin kovaa alaspäin.\n')
            choice = input('')

            if choice == '1':
                print('\nVastustaja löi pallon takaisin kovaa ja sai pisteen.')
                opponentscore += 1
                score(teamscore, opponentscore)

            if choice == '2':
                print('\nHienoa! Pallo osui vastustajan puolelle maahan ja saitte pisteen.')
                teamscore += 1
                score(teamscore, opponentscore)

            else:
                print('\nEt tehny mitään ja pallo putosi maahan. Vastustaja sai pisteen.')
                opponentscore += 1
                score(teamscore, opponentscore)

        if servetype == 2:
            print('\nPallo lentää \033[36mnopeasti\033[0m alaspäin teille, miten syötät pallon takaisin? (\033[33m1\033[0m/\033[33m2\033[0m)')
            print('\033[33m1\033[0m Hitaasti takaisin vastustajalle')
            print('\033[33m2\033[0m Yritä lyödä pallo takaisin kovaa alaspäin.\n')
            choice = input('')

            if choice == '1':
                print('\nOnnistuit syöttämään pallon takaisin.')

            if choice == '2':
                print('\nPallo jäi verkkoon kiinni ja vastustaja sai pisteen.')
                opponentscore += 1
                score(teamscore, opponentscore)

        if teamscore == 5:
            print(f'\nHienoa! Voitit pelin!')
            print('Joukkuetoverisi kiitti sinua 200:lla pisteellä!')
            points =+ 200
            break

        if opponentscore == 5:
            print(f'\nHävisit pelin.')
            print('Joukkuetoverisi katsoivat sinua pettyneesti kun menit pilaamaan heidän rantapalloturnausta.')
            break

    return ["sum", 100]

#Robbie minipeli 1 "pummi" (DONE)
def tirana():

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
                print(f'Pummi oli sosiaalisen median vaikuttaja ja hän palkitsi sinut 100 pistettä sinun kiltteydestäsi.')
                return ["sum", 100]
                break
                #insert a win reward here

            elif win == False:
                print("Pummi kiitti nauraen ja hyväksikäytti sinisilmäistä anteliaisuuttasi.")
                return["sum", -100]
                break

        else:
            print("Älä ignooraa pummia... :(")


#Robbie minipeli 2 "roulette" (DONE)
def vienna():
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
            print('Olet viisas ja ymmärrät että uhkapelaamisesta aina seuraa jotain pahaa.')
            print('Jatkat matkaa seuraavaan kenttään...')
            break

        elif r == 'Kyllä':

            pisteet = 100 #main.pisteet TÄHÄN PITÄÄ IMPORTTAA MAIN PISTEET

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


    return ["sum", pisteet]

#Robbie minipeli 3 "kapina" (DONE)
def warsaw():

    question = query("Mikä vuosi on tunnettu Varsovan kapinan vuodesta?",
                     ["1: 1939", "2: 1944", "3: 1945", "4: 1956"],
                     ["1", "2", "3", "4"])

    if question == "2":
        print("Vastasit oikein!\nVoitit 100 pistettä!")
        return ["sum", 100]
    else:
        print("Vastasit väärin!\nMenetät 100 pistettä")
        return ["sum", -100]

#Robbie minipeli 4 "soutukilpailu" (DONE)
def budapest():

    def paddle_type():
        return random.choice(["slow", "fast"])

    def score(teamscore, opponentscore):
        print(f'\033[33m{teamscore} - {opponentscore}\033[0m')

    print(f'\nSaavuit budapestiin, ja soudat Danube joessa.')
    print(f'Harhaannuit väärään osaan jokea ja et tiennyt että joessa oli soutukilpailu.')
    print('Aika kilpailla!')

    teamscore = 0
    opponentscore = 0
    points = 0

    while teamscore < 5 and opponentscore < 5:
        print(f'\nKilpailu on kiivas! Veneesi liitää eteenpäin Tonavalla!')
        print('Mitä teet?')

        type = paddle_type()

        if type == "slow":
            print('\nPaddlaat hitaasti, mutta virta on voimakas!')
            action_choice = input('Haluatko yrittää nopeuttaa venettäsi? (1/2) \n1. Paddlaa nopeammin \n2. Jatka hitaasti paddlaamista\n')

            if action_choice == '1':
                print('\nPaddlasit nopeammin! Veneesi kiihdytti eteenpäin!')
                teamscore += 1
            elif action_choice == '2':
                print('\nVeneesi jäi hieman jälkeen. Vastustaja sai etumatkaa!')
                opponentscore += 1
            else:
                print('\nJäiksite paikalleen ja et tehnyt mitään. Vastustaja ohitti sinut!')
                opponentscore += 1

        elif type == "fast":

            print('\nPaddlaat nopeasti, veneesi kiihdyttää eteenpäin!')
            action_choice = input('Haluatko väistää edessä olevia esteitä? (1/2)\n1. Siirry vasemmalle väistäksesi roskia\n2. Jatka nykyisellä kurssilla\n')

            if action_choice == '1':
                print('\nVäistit roskat ja sait lisää vauhtia!')
                teamscore += 1
            elif action_choice == '2':
                print('\nHidastit veneesi törmätessä roskien kanssa. Vastustaja otti johdon!')
                opponentscore += 1
            else:
                print('\nEt tehnyt liikettä ja törmäsit roskiin. Menetit aikaa!')
                opponentscore += 1

        score(teamscore, opponentscore)

        if teamscore == 5:
            print(f'\nUpeat suoritus! Voitit venekilpailun! Woohoo!')
            print('Rannalla olevat ihmiset kannustivat sinua, kun veneesi ylitti maalilinjan!')
            points += 200
            break

        if opponentscore == 5:
            print(f'\nHävisit kilpailun. :(')
            print('Rannalla olevat katsojat pudistivat päätään pettyneinä.')
            break
    return ["sum", points]

#Robbie minipeli 5 "vikiinki" (DONE)
def keflavik():

    question = query("\nKuka oli ensimmäinen Islantiin asettunut vikingi?\n",
                     ["1: Leif Erikson", "2: Erik the Red", "3: Ingólfur Arnarson", "4: Snorri Sturluson\n"],
                     ["1", "2", "3", "4"])

    if question == "3":
        print("Vastasit oikein!\nVoitit 100 pistettä!")
        return ["sum", 100]
    else:
        print("Vastasit väärin!\nMenetät 100 pistettä")
        return ["sum", -100]

#Robbie minipeli 6 "beachball" (DONE)
def mallorca():
    print(f'\nSaavuit ihanaan mallorcaan missä rannalla paistaa ihanasti aurinko.')
    print('Rannalla kävelyllä astuit epähuomiossa rantapallopeliturnauksen keskelle ja jouduit pelaajaksi kentälle.')

    def get_serve_type():
        return random.randint(1, 2)

    def score(teamscore, opponentscore):
        return print(f'\033[33m{teamscore} - {opponentscore}\033[0m')
    points = 0
    teamscore = 0
    opponentscore = 0

    while teamscore < 5 or opponentscore < 5:

        servetype = get_serve_type()

        if servetype == 1:
            print('\nPallo lentää \033[36mhitaasti\033[0m korkealle, miten syötät pallon takaisin? (\033[33m1\033[0m/\033[33m2\033[0m)')
            print('\033[33m1\033[0m Hitaasti takaisin vastustajalle')
            print('\033[33m2\033[0m Yritä lyödä pallo takaisin kovaa alaspäin.\n')
            choice = input('')

            if choice == '1':
                print('\nVastustaja löi pallon takaisin kovaa ja sai pisteen.')
                opponentscore += 1
                score(teamscore, opponentscore)

            if choice == '2':
                print('\nHienoa! Pallo osui vastustajan puolelle maahan ja saitte pisteen.')
                teamscore += 1
                score(teamscore, opponentscore)

            else:
                print('\nEt tehny mitään ja pallo putosi maahan. Vastustaja sai pisteen.')
                opponentscore += 1
                score(teamscore, opponentscore)

        if servetype == 2:
            print('\nPallo lentää \033[36mnopeasti\033[0m alaspäin teille, miten syötät pallon takaisin? (\033[33m1\033[0m/\033[33m2\033[0m)')
            print('\033[33m1\033[0m Hitaasti takaisin vastustajalle')
            print('\033[33m2\033[0m Yritä lyödä pallo takaisin kovaa alaspäin.\n')
            choice = input('')

            if choice == '1':
                print('\nOnnistuit syöttämään pallon takaisin.')

            if choice == '2':
                print('\nPallo jäi verkkoon kiinni ja vastustaja sai pisteen.')
                opponentscore += 1
                score(teamscore, opponentscore)

        if teamscore == 5:
            print(f'\nHienoa! Voitit pelin!')
            print('Joukkuetoverisi kiitti sinua 200:lla pisteellä!')
            points += 200
            break

        if opponentscore == 5:
            print(f'\nHävisit pelin.')
            print('Joukkuetoverisi katsoivat sinua pettyneesti kun menit pilaamaan heidän rantapalloturnausta.')
            break
    return ["sum", points]

#Elias minipeli 1
def humberto():
    question = query("Milloin Humberto Delgadon lentoasema vihittiin virallisesti käyttöön",
                    ["1: 1930", "2: 1942", "3: 1955", "1966"],
                    ["1", "2", "3", "4"])

    if question == "2":
        print("Vastasit oikein!\nVoitit 10 pistettä!")
    
    else:
        print("Vastasit väärin!\nMenetät 10 pistettä")

#Elias minipeli 2
def copenhagen():
    question = query("Minä vuonna Kööpenhaminan Kastrupin lentoasema avattiin?",
                    ["1: 1925", "2: 1935", "3: 1945", "4: 1955"],
                    ["1", "2", "3", "4"])
    if question == "1":
        print("Vastasit oikein!\nVoitit 100 pistettä!")
        return ["sum", 100]
    else:
        print("Vastasit väärin!\nMenetät 100 pistettä")
        return ["sum", -100]

#Elias minipeli 3
def oslo():
    question = query("Mikä on Oslon lentoaseman IATA-koodi?",
                    ["1: LITP", "2: ASDF", "3: DFKL", "4: ENGM"],
                    ["1", "2", "3", "4"])
    if question == "4":
        print("Vastasit oikein!\nVoitit 100 pistettä!")
        return ["sum", 100]
    
    else:
        print("Vastasit väärin!\nMenetät 100 pistettä")
        return ["sum", -100]

#Elias minipeli 4
def brussels():
    question = query("Mikä lentoyhtiö liikennöi suoria lentoja Brysselistä New Yorkiin?",
                    ["1: LITP", "2: ASDF", "3: DFKL", "4: ENGM"],
                    ["1", "2", "3", "4"])
    if question == "4":
        print("Vastasit oikein!\nVoitit 100 pistettä!")
        return ["sum", 100]
    else:
        print("Vastasit väärin!\nMenetät 100 pistettä")
        return ["sum", -100]
    
#Elias minipeli 5
def riga():
    question = query("Minä vuonna Riigan lentoasema perustettiin?",
                    ["1: 1963", "2: 1973", "3: 1953", "4: 2003"],
                    ["1", "2", "3", "4"])
    if question == "2":
        print("Vastasit oikein!\nVoitit 100 pistettä!")
        return ["sum", 100]
    else:
        print("Vastasit väärin!\nMenetät 100 pistettä")
        return ["sum", -100]