# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:56:36 2020

@author: camil
"""

from pygame import *
from variables import *


class SpriteCase(sprite.Sprite):
    
    """
    Sprite s'initialisant avec les attributs image et rect.
    Sprite avec une méthode clic() et move_ip()
    """
    
    images = IMAGES
    
    def __init__(self, x, y, *groups): 
        """On hérite de la classe Sprite"""
        
        sprite.Sprite.__init__(self, *groups)
        self.image = SpriteCase.images['neutre']   
        self.rect = Rect(x, y, 10, 10)
        
    def clic(self, clic_x, clic_y):
        """
        Regarde si on a cliqué sur le sprite.
        Renvoie True si c'est le cas
        """
        
        if (self.rect.x <= clic_x < self.rect.x +self.rect.w
        and self.rect.y <= clic_y < self.rect.y +self.rect.h):
            self.image = SpriteCase.images['blanc']
            print('ok')
            return True
        return False
                