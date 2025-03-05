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

# Construct file paths for sounds
sound_paths = [os.path.join(os.path.dirname(__file__), "sound", file) for file in sound_files]
sounds = [pygame.mixer.Sound(path) for path in sound_paths]  # Load all sounds

def slow_print(text, base_delay=0.05, sound_effect=True):
    """Prints text slowly with randomized sound effects and speed.

    Args:
        text (str): The text to print.
        base_delay (float): Base delay between characters.
        sound_effect (bool): Whether to play a sound effect.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        if sound_effect:
            sound = random.choice(sounds)  # Pick a random sound
            sound.play()
            pygame.time.wait(30)  # Short delay for sound sync

        # Add slight randomness to the delay
        time.sleep(base_delay + random.uniform(-0.02, 0.02))

    print()  # Move to a new line

# Example usage
slow_print("Hello, this is a GBA-style text effect!", base_delay=0.02, sound_effect=True)