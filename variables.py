# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:10:35 2020

@author: camil
"""
from pygame import *
import numpy as np

#Caractéristiques du damier
NOMBRE_CASES_X = 125
NOMBRE_CASES_Y = 75
POSITION_X = 550
POSITION_Y = 165


#Caractéristiques des SpriteCase
pixels_noirs = np.array([[(0,0,0) for i in range(10)] for j in range(10)])
case_noire = surfarray.make_surface(pixels_noirs)

IMAGES = {'neutre' : case_noire}