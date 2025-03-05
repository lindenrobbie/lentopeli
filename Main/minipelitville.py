import random

#Minipeli 1
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



#Minipeli 2
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

#minigame_frankfurt()



#Minipeli 3
def minigame_stockholm():
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


#minigame_stockholm()

#paina enteriä jatkaaksesi ohjelmaa funktio
def enter_continue():
    while True:
        useri=input('Jatka painamalla enter: ')
        if useri == '':
            print('')
            break


#Minipeli 4
def minigame_bike():
    bikechoise = 0
    def bike_choise():
        print('Valitse pyöräsi seuraavista:\n')
        bikes={1:'1.Trek katupyörä',2:'2.Specialized DH pyörä',3:'3.Helkaman mummis',4:'4.Orbea sähköpyörä'}
        for key in bikes:
            print(f'{bikes[key]}')
        choise=int(input('\nValintasi: '))
        return choise

    print('Ilmoittauduit pyöräilykilpailuun.')
    print('Valitse oikea pyörä oikeaan tilanteeseen')
    enter_continue()

    #Startti
    print('Lähtopäikalta lähdetään kiihdyttämään\n')
    bikechoise=bike_choise()

    if bikechoise == 1:
        print('Katupyörä kiihtyy hitaasti mutta saavuttaa kovan nopeuden aikanaan')
    if bikechoise == 2:
        print('Polkemisesta häviää voima jousitukseen ja jäät jälkeen')
    if bikechoise == 3:
        print('Keulit mummiksella kisan kärkeen!')
    if bikechoise == 4:
        print('Painat kaasua ja pääset kärkikahinoihin ilman hikikarpaloita')

    print('')

    #Ylämäki
    print('Saavut jyrkkään ylämäkeen')
    enter_continue()
    bikechoise=bike_choise()

    if bikechoise == 1 or bikechoise == 2:
        print('Vaihdat vaihdetta pienempään ja pääset mäen ylös')
    if bikechoise == 3:
        print('Mummiksesta loppuu vaihteet ja joudut taluttamaan mäen ylös')
    if bikechoise == 4:
        print('Liidät mäen ylös sähkön voimalla')
    enter_continue()

    #Alamäki
    print('Edessäsi on jyrkkä ja epätasainen alamäki')
    enter_continue()
    bikechoise=bike_choise()

    if bikechoise == 1 or bikechoise == 4:
        while True:
            walk=input('Talutatko pyörän alas?\nkyllä/ei')
            if walk== 'kyllä':
                print('pääset hitaasti mäen taluttamalla alas')
                break
            if walk== 'ei':
                print('Kaadut alamäessä ja jäät viimeiseksi')
                break

    if bikechoise == 2:
        print('Lennät epätasaisuuksien yli jousituksesi avulla kisan kärkeen')

    if bikechoise == 3:
        print('Ryskäät mummiksella mäen alas mutta vanne menee kieroon')
    enter_continue()

    #Mutka
    print('Tulet alamäen jälkeen mutkaan')
    enter_continue()
    bikechoise=bike_choise()

    if bikechoise == 3:
        print('Jalkajarru ei ole riittävän tehokas ja törmäät kaiteeseen')
    else:
        print('Levyjarrut hidastivat sinua tarpeeksi ja selvisit mutkasta')




    



minigame_bike()
#enter_continue()






