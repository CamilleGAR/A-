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
                
            elif (event.type == MOUSEBUTTONDOWN and event.button == 1) \
                or (event.type == MOUSEMOTION and event.buttons[0])  :
                a_etoile.left_clic(*event.pos)
                
            elif (event.type == MOUSEBUTTONDOWN and event.button == 3) :
                a_etoile.right_clic(*event.pos)
                           
                                
        #Affichage
        a_etoile.clear_group.clear(fenetre, BACKGROUND)
        dirty = a_etoile.draw_group.draw(fenetre)
        display.update(dirty)
    