import pygame
from pygame import *
from spriteCase import SpriteCase
from variables import *
from aEtoile import AEtoile


#initialisation de pygame
init()


#Création de l'objet principal
a_etoile = AEtoile()


#Création de la surface principale
fenetre = display.set_mode(flags = FULLSCREEN )
fenetre.blit(BACKGROUND,(0,0))
a_etoile.draw_group.draw(fenetre)
display.flip()


#Création de l'horloge du programme
clock = time.Clock()


# """MAIN BROUILLON"""
# #Boucle principale
# continuer = True
# while continuer :
    
#     #Cap de framerate
#     clock.tick(60)
    
#     if mouse.get_pressed()[0]:
#         pos = mouse.get_pos()
#         for c in cases_group:
#                 if c.clic(*pos):
#                     c.add(refresh_group)
                
#     for event in pygame.event.get():
#         print(event)
#         if event.type == QUIT :
#             continuer = 0
#             quit()
    
#     dirty = refresh_group.draw(fenetre)
#     display.update(dirty)
    
    
"""MAIN FINAL"""    
if __name__ == '__main__' :
    
    
    continuer = True
    while continuer :
        
        #Cap de framerate
        clock.tick(60)
        
        #Reinitialise les groupes de modifications
        a_etoile.clear_group.empty()
        a_etoile.draw_group.empty()
        
        
        #Inputs
        for event in pygame.event.get() :
            
            if event.type == QUIT :
                continuer = 0
                quit()
                
            elif event.type == MOUSEBUTTONDOWN :
                a_etoile.clic(*event.pos)
                
            elif event.type == MOUSEMOTION and a_etoile.mouse_pressed == True :
                a_etoile.clic(*event.pos)
                
            elif event.type == MOUSEBUTTONUP :
                a_etoile.unclic()                
                
                
        #Affichage
        a_etoile.clear_group.clear(fenetre, BACKGROUND)
        dirty = a_etoile.draw_group.draw(fenetre)
        display.update(dirty)
    