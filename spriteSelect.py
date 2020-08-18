# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:48:03 2020

@author: camil
"""
from pygame import *
from variables import *


class SpriteSelect(sprite.Sprite):
    
    """
    Sprite s'initialisant avec les attributs image et rect.
    Sprite avec une méthode clic() et move_ip()
    """
    
    def __init__(self, x, y, sprite_case, a_etoile, *groups): 
        """On hérite de la classe Sprite"""
        sprite.Sprite.__init__(self, *groups)
        
        self.image = SELECT  
        self.rect = Rect(x, y, 30, 40)
        
        #redirige vers la classe principale
        self.a_etoile = a_etoile       
        
        #Case associées
        self.sprite_case = sprite_case
        
        #Elements que ce sprite cache. A redessiner quand killed
        self.draw_when_killed = sprite.spritecollide(self, a_etoile.all_sprites, dokill = False)
        
    def __del__(self) :
        self.a_etoile.draw_group.add(self.draw_when_killed)
        
    def left_clic(self, *args):
        pass