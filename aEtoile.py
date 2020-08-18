# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 20:59:01 2020

@author: camil
"""
from pygame import *
from damier import Damier
from spriteCase import SpriteCase
from pygame.sprite import Group
from renderClic import RenderClic

class AEtoile:
    def __init__(self) :
        
        #Elements composants le aEtoile
        self.damier = Damier(self)
        
        #Groupe de sprite cliquables avec un clic gauche
        self.left_clic_group = RenderClic(self.damier.cases_group)
        
        #Groupe de sprite cliquables avec un clic droit
        self.right_clic_group = RenderClic(self.damier.cases_group)
        
        #Création du groupe de sprite à clean
        self.clear_group = RenderClic()

        #Création du groupe de sprite à draw
        self.draw_group = RenderClic(self.damier.cases_group)
        
        #Tous les éléments
        self.all_sprites = Group(self.damier.cases_group)
        
        
    def left_clic(self, x, y) :
        """
        Clique sur la position (x,y). 
        """
        self.left_clic_group.left_clic(x, y)
        
    def right_clic(self, x, y) :
        """
        Clique sur la position (x,y). 
        """
        self.right_clic_group.right_clic(x, y)
        