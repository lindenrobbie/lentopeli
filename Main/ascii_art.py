import pygame
import sound

def print_ascii_art():
    ascii_art = """\033[31m
    ___                          _                _________       __    __     ____                     ___   ____ ___   ______
   /   |  ____ ___  ____ _____  (_)___  ____ _   / ____/ (_)___ _/ /_  / /_   / __ \____ _________     |__ \ / __ \__ \ / ____/
  / /| | / __ `__ \/ __ `/_  / / / __ \/ __ `/  / /_  / / / __ `/ __ \/ __/  / /_/ / __ `/ ___/ _ \    __/ // / / /_/ //___ \  
 / ___ |/ / / / / / /_/ / / /_/ / / / / /_/ /  / __/ / / / /_/ / / / / /_   / _, _/ /_/ / /__/  __/   / __// /_/ / __/____/ /  
/_/  |_/_/ /_/ /_/\__,_/ /___/_/_/ /_/\__, /  /_/   /_/_/\__, /_/ /_/\__/  /_/ |_|\__,_/\___/\___/   /____/\____/____/_____/   
                                     /____/             /____/                                                                 
\033[39m"""
    print(ascii_art)

    titlescreen_sound = sound.titlescreen()

    titlescreen_channel = pygame.mixer.find_channel()

    if titlescreen_channel:
        titlescreen_channel.play(titlescreen_sound)
    else:
        print("No available sound channel to play the sound.")

    pygame.time.wait(3000)
    input('Jatka painamalla enteriä')

print_ascii_art()