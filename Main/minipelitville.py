import random

#Olet myöhässä koneestasi
def minigame_late():
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





minigame_late()