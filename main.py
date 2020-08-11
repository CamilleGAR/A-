import pygame
from pygame import *
from spriteClic import SpriteClic

init()
#fenetre = display.set_mode(flags = FULLSCREEN )
fenetre = display.set_mode((1536,864))

#Création du groupe de sprite : cases cliquables
cases_group = sprite.RenderClear()

#Création des sprites cliquables
perso = image.load("perso.png").convert_alpha()
sprite1 = SpriteClic(perso, Rect(0,0,0,0), cases_group)
sprite2 = SpriteClic(perso, Rect(10,10,0,0), cases_group)
for i in range(20000):
    SpriteClic(perso, Rect(0,0,0,0), cases_group)

continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
            quit()
        elif event.type == MOUSEBUTTONDOWN :
            sprite1.rect.move_ip(3,3)
    fenetre.fill((255,255,255))
    cases_group.draw(fenetre)
    display.flip()