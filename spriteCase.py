# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:56:36 2020

@author: camil
"""

from pygame import *
from variables import *
from spriteSelect import SpriteSelect


class SpriteCase(sprite.Sprite):
    
    """
    Sprite s'initialisant avec les attributs image et rect.
    Sprite avec une méthode clic() et move_ip()
    """
    
    images = IMAGES
    
    def __init__(self, x, y, a_etoile, *groups): 
        """On hérite de la classe Sprite"""
        sprite.Sprite.__init__(self, *groups)
        
        #redirige vers la classe principale
        self.a_etoile = a_etoile       
        
        self.image = SpriteCase.images['neutre']   
        self.rect = Rect(x, y, 10, 10)
        
        #fenetre select
        self.selection = None
        
    def left_clic(self, clic_x, clic_y):
        """
        Regarde si on a cliqué sur le sprite.
        """
        
        if (self.rect.x <= clic_x < self.rect.x +self.rect.w
        and self.rect.y <= clic_y < self.rect.y +self.rect.h):
            
            #Change la couleur de la case
            self.image = SpriteCase.images['mur']
            
            #Indique que l'on doit reafficher cette case
            self.a_etoile.draw_group.add(self)
            
        elif self.selection != None :
            self.selection.kill()
            self.selection = None
            
    def right_clic(self, clic_x, clic_y):
        if (self.rect.x <= clic_x < self.rect.x +self.rect.w
        and self.rect.y <= clic_y < self.rect.y +self.rect.h):
            
            self. selection = SpriteSelect(clic_x, clic_y, self, self.a_etoile, self.a_etoile.draw_group, self.a_etoile.left_clic_group)
            
        elif self.selection != None :
            self.selection.kill()
            self.selection = None
                