import sys
import time
import pygame
import os
import random

pygame.mixer.init()

sound_files = [
    "type1.wav",
    "type2.wav",
    "type3.wav"
]

final_sound_file = "type4.wav"

# Construct file paths
sound_paths = [os.path.join(os.path.dirname(__file__), "sound", file) for file in sound_files]
final_sound_path = os.path.join(os.path.dirname(__file__), "sound", final_sound_file)

# Load all sounds
sounds = [pygame.mixer.Sound(path) for path in sound_paths]
final_sound = pygame.mixer.Sound(final_sound_path)

def slow_print(text, base_delay=0.03, sound_effect=True, end_with_newline=True):

    for i, char in enumerate(text):
        sys.stdout.write(char)
        sys.stdout.flush()

        if sound_effect:
            if i == len(text) - 1:  #vika kirjain toistaa type4.wav (pidempi ääni niiku GBA:ssa)
                final_sound.play()
            else:
                sound = random.choice(sounds)  # Random sound for other letters
                sound.play()

        # varianssa kirjaimen äänelle
        time.sleep(base_delay + random.uniform(-0.02, 0.02))

    if end_with_newline:
        print()

def slow_input(prompt, base_delay=0.03):
    slow_print(prompt, base_delay=base_delay, sound_effect=True, end_with_newline=False)
    return input(" ")
