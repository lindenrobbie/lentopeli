import random

#Olet myöhässä koneestasi
def minigame_late():
    print ('')
    print ("Olet myöhästymässä lentokoneestasi!")
    print ("Joudut improvisoimaan jotta kerkeät lennolle")
    print ("Valitse jokin seuraavista vaihtoehdoista:")

    while True:
        choise = input('1. Juokse turvatarkastuksen läpi\n2. Lainaa golfkärryn näköistä ajoneuvoa\n3. Pyydä apua henkilökunnalta\nValintasi: ')
        print ("")

        if choise =='1' or '2' or '3':
            if choise == '1':
                success = random.randint(1,10)
                if success == 1:
                    print ('Pääsit kuin ihmeen kaupalla livahtamaan tarkastuksen läpi.\n\nKerkesit lennolle ja ansaitsit 100 lisäpistettä!')
                else:
                    print ('Turvatarkastus otti sinut kiinni joten myöhästyit lennoltasi.\n\nMenetit 100 pistettä.')
                break

            if choise == '2':
                success = random.randint(1, 5)
                if success == 1:
                    print ('Sait ajoneuvolla kirittyä aikataulusi kuntoon ja kerkesit lennollesi!\n\nAnsaitsit 50 lisäpistettä.')
                else:
                    print ('Törmäsit ajoneuvolla terminaalissa pylvääseen...\n\nMyöhästyit lennoltasi ja menetät 50 pistettä.')
                break

            if choise == '3':
                success = random.randint(1,2)
                if success == 1:
                    print ('Henkilökunta viivästytti lentoa ja kerkesit matkaan mukaan!\n\nAnsaitsit 25 pistettä.')
                else:
                    print ('Henkilökunta ei ymmärtänyt kieltäsi.\n\nMyöhästyit lennoltasi ja menetit 25 pistettä.')
                break

            else:
                print ('Syötä numerovaihtoehto 1,2 tai 3!')

#minigame_late()




def minigame_frankfurt():
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






#print ('Oikein vastattu! Ansaitsit 25 pistettä.')
#print ('Vastasit väärin. Et ansainnut pisteitä')
#print('Syötä numerovaihtoehto 1,2 tai 3!')

minigame_frankfurt()

