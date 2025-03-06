import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import gba_print
import sound
import random
import pygame

def minigame_pummi():
    gba_print.slow_print("\nNäät lentokentässä pummin joka pyytää sinulta rahaa ruokaan")
    gba_print.slow_print('Annatko pummille (x määrä) rahaa? Kyllä/En')

    while True:
        print("")
        r = input('').strip()

        if r in ["Kyllä", "En"]:
            break
        gba_print.slow_print("Vastaa Kyllä/En")

    chance = random.randint(1, 10)
    win = chance in range(1, 3)

    if r == 'En':
        gba_print.slow_print(
            "\nJatkat matkaasi seuraavaan lentoon pikaisesti ja näät silmänkulmassasi kun pummi surullisesti tärisee nälästä")
    elif r == 'Kyllä':
        if win:
            gba_print.slow_print("\nPummi oli sosiaalisen median vaikuttaja ja hän palkitsi sinut PISTEET sinun kiltteydestäsi.")
        else:
            gba_print.slow_print("Pummi kiitti nauraen ja hyväksikäytti sinisilmäistä anteliaisuuttasi.")