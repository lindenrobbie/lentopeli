#robbien tekemä minipeli mallorcan lentokentälle

#import sys, os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import random

def get_serve_type():
    return random.randint(1,2)

def score(teamscore, opponentscore):
    return print(f'\033[33m{teamscore} - {opponentscore}\033[0m')


def minigame_beachball():
    print(f'\nSaavuit ihanaan mallorcaan missä rannalla paistaa ihanasti aurinko.')
    print('Rannalla kävelyllä astuit epähuomiossa rantapallopeliturnauksen keskelle ja jouduit pelaajaksi kentälle.')

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


minigame_beachball()