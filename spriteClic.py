# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:56:36 2020

@author: camil
"""

from pygame.sprite import Sprite


class SpriteClic(Sprite):
    
    """
    Sprite s'initialisant avec les attributs image et rect.
    Sprite avec une méthode clic() et move_ip()
    """
    
    def __init__(self, image, rect, *groups):
        Sprite.__init__(self, *groups)
        self.image = image
        self.rect = rect
        
    def clic(self):
        pass
        
    def move_ip(self):
        pass