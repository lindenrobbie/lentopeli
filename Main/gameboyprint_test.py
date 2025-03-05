import sys
import time
import pygame
import os
import random

# Initialize pygame mixer
pygame.mixer.init()

# Load multiple sound variations
sound_files = [
    "type1.wav",
    "type2.wav",
    "type3.wav"
]

# Load the final sound separately
final_sound_file = "type4.wav"

# Construct file paths
sound_paths = [os.path.join(os.path.dirname(__file__), "sound", file) for file in sound_files]
final_sound_path = os.path.join(os.path.dirname(__file__), "sound", final_sound_file)

# Load all sounds
sounds = [pygame.mixer.Sound(path) for path in sound_paths]
final_sound = pygame.mixer.Sound(final_sound_path)

def slow_print(text, base_delay=0.05, sound_effect=True):
    """Prints text slowly with randomized sound effects and ensures the last letter plays a specific sound.

    Args:
        text (str): The text to print.
        base_delay (float): Base delay between characters.
        sound_effect (bool): Whether to play a sound effect.
    """
    for i, char in enumerate(text):
        sys.stdout.write(char)
        sys.stdout.flush()

        if sound_effect:
            if i == len(text) - 1:  # Last character
                final_sound.play()
            else:
                sound = random.choice(sounds)  # Random sound for other letters
                sound.play()
                pygame.time.wait(30)  # Short delay for sync

        # Add slight randomness to the delay
        time.sleep(base_delay + random.uniform(-0.02, 0.02))

    print()  # Move to a new line

# Example usage

while True:

    test = input('Laita tähän tekstiä ja testaa ääntä: ')

    slow_print(test, base_delay=0.04, sound_effect=True)