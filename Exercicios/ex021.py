"""
FACA UM PROGRAMA QUE ABRA E REPRODUZA UM ARQUIVO MP3
"""
import pygame
pygame.init()
pygame.mixer.music.load('se-loko-num-compensa.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()