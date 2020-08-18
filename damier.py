# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:01:29 2020

@author: camil
"""

from pygame import *
from spriteCase import SpriteCase
from variables import *

class Damier:
    def __init__(self, a_etoile):
        #redirige vers la classe principale
        self.a_etoile = a_etoile
        
        #Création du groupe de sprite des cases (damier)
        self.cases_group = sprite.RenderUpdates()
        
        #Création des cases (damier)
        for x in range(NOMBRE_CASES_X) :
            for y in range(NOMBRE_CASES_Y) :
                SpriteCase(x*10 +POSITION_X, y*10 +POSITION_Y, self.a_etoile, self.cases_group)