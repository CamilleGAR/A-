# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 20:59:01 2020

@author: camil
"""
from pygame import *
from damier import Damier
from spriteCase import SpriteCase
from renderClic import RenderClic

class AEtoile:
    def __init__(self) :
        #Informations sur la sourie
        self.mouse_pressed = False
        self.last_clic = None
        
        #Elements composants le aEtoile
        self.damier = Damier()
        
        #Groupe de sprite cliquables
        self.clic_group = RenderClic(self.damier.cases_group)
        
        #Création du groupe de sprite à clean
        self.clear_group = RenderClic()

        #Création du groupe de sprite à draw
        self.draw_group = RenderClic(self.damier.cases_group)
        
        
    def clic(self, x, y) :
        """
        Clique sur la position (x,y). 
        S'il s'agit d'une case, self.mouse_pressed passera à True
        """
        self.clic_group.clic(x, y)
        
    def unclic(self) :
        """On relache la sourie. self.mouse_pressed repasse à False"""
        self.mouse_pressed = False
        