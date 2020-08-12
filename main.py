import pygame
from pygame import *
from spriteCase import SpriteCase
from variables import *


#initialisation de pygame
init()


#Création du groupe de sprite des cases (damier)
cases_group = sprite.RenderUpdates()


#Création des cases (damier)
for x in range(NOMBRE_CASES_X) :
    for y in range(NOMBRE_CASES_Y) :
        SpriteCase(x*10 +POSITION_X, y*10 +POSITION_Y, cases_group)


#Création de la surface principale
fenetre = display.set_mode(flags = FULLSCREEN )
fenetre.fill((255,255,255))
display.flip()


continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT or event.type == MOUSEBUTTONDOWN :
            continuer = 0
            quit()
    cases_group.clear(fenetre,Surface((10,10)))
    dirty = cases_group.draw(fenetre)
    display.update(dirty)