import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Define the path to your sound files directory
SOUND_DIR = os.path.join(os.path.dirname(__file__), "sound")

# Load sounds by file name
def load_sound(filename):
    path = os.path.join(SOUND_DIR, filename)
    return pygame.mixer.Sound(path)

# Example functions to load specific sounds
def roulettewin():
    return load_sound("roulettewin.wav")

def roulettelose():
    return load_sound("roulettelose.wav")

def gameover():
    return load_sound("gameover.wav")

def titlescreen():
    return load_sound("titlescreen.wav")