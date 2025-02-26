import random
import db_modules

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
            print("Jatkat matkaasi seuraavaan lentoon pikaisesti ja näät silmänkulmassasi kun surullisesti tärisee nälästä")

        elif r == 'Kyllä':


            if win == True:
                print(f'Pummi oli sosiaalisen median vaikuttaja ja hän palkitsi sinut PISTEET sinun kiltteydestä.')
                break
            #insert a win reward here

            elif win == False:
                print("Pummi kiitti nauraen ja hyväksikäytti sinisilmäistä anteliaisuuttasi.")
                break

        else:
            print("Älä ignooraa pummia... :(")




minigame_pummi()