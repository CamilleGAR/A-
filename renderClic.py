# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:47:13 2020

@author: camil
"""
from pygame.sprite import RenderUpdates

class RenderClic(RenderUpdates):
    
    def left_clic(self, x, y):
        for sprite in self.sprites():
            sprite.left_clic(x, y)
            
    def right_clic(self, x, y):
        for sprite in self.sprites():
            sprite.right_clic(x, y)