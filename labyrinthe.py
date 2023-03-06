"""
!/usr/bin/env python3
-*- coding: utf-8 -*-

Created on Thu Dec 8 - 20:00:00 2022

@author: deodorant@kangaroo
"""

import pygame
from pygame.locals import *
from time import *

#------------------------------------------------------------------------------

# Tableau des murs
Wall_list = []

# On charge les murs
def Display_wall():
    
    # On rafraîchit la fenêtre avec chaque mur 1 par 1
    for Wall_piece in Wall_list:
        fenetre.blit(Wall, Wall_piece)

Xe = 0
Ye = 0
Xtp = 0
Ytp = 0

#------------------------------------------------------------------------------

# On charge la carte en posant les murs, le perso, la sortie...
def Load_Map():
    global Xe
    global Ye
    Y = 0
    
    for line in map_lines:
        X = 0
        
        # On lit les chiffres et on place 0 = vide, on voit le fond
        for elem in line:
            if (elem == '1'):
                Wall_piece = Wall.get_rect()
                Wall_piece.topleft = (X,Y)
                Wall_list.append(Wall_piece)
           
            if (elem == '2'):
                persoRect.topleft = (X,Y)
           
            if (elem == '3'):
                Xe = X
                Ye = Y
            
            X += Size_Object_X
       
        Y += Size_Object_Y

#------------------------------------------------------------------------------

pygame.init()

# On permet de rester appuyé sur les flèches
pygame.key.set_repeat(50, 15)

# Taille des rect. de collision des sprites
Size_Player_X = 50
Size_Player_Y = 50

Size_Object_X = 50
Size_Object_Y = 50

Screen_Width = 500
Screen_Height = 500

# On ouvre la carte .txt et on lit les nombres
map = open(r"./map.txt", 'r')
map_lines = map.readlines()

# Collision de fin d'un niveau
endRect = pygame.Rect(450, 50, 45, 45)

# Taille fenêtre pygame
fenetre = pygame.display.set_mode((Screen_Width, Screen_Height))

# On importe le fond d'écran puis on en fait une surface
Surface_Background =  pygame.image.load(r"./background.jpg")
fond = Surface_Background.convert()

# On importe le sprite du perso et on le convertit pour des collisions
perso = pygame.image.load(r"./spriteperso().png").convert_alpha()
persoRect = perso.get_rect()

# Même chose avec le sprite de mur + on charge la carte
Surface_Wall =  pygame.image.load(r"./spritemur().png")
Wall = Surface_Wall.convert_alpha()
Load_Map()

# Même chose avec le sprite de la sortie de niveau
exit = pygame.image.load(r"./spriteexit().png").convert_alpha()
exitRect = exit.get_rect()
exitRect.topleft = (Xe,Ye)

#------------------------------------------------------------------------------

# Compteur de niveau
z = 0

# On rafraîchit
fenetre.blit(fond,(0,0))

# On lance le moteur de jeu
continuer = True

# Moteur de jeu
while continuer:
    # On dessine un rectangle de vide là où il y avait le sprite de perso
    pygame.draw.rect(fenetre, (0,0,0), persoRect)
    
    # On regarde l'évènement
    for event in pygame.event.get():
        
        # Si [QUITTER] pressé:
        if event.type == QUIT:
            continuer = False
            
        # Si [TOUCHE DE CLAVIER] pressé:
        if event.type == KEYDOWN:
            dicKeys = pygame.key.get_pressed()
            
            
            # Si [FLECHE_GAUCHE]:
            if dicKeys[K_LEFT]:
                
                # On bouge le rect de collision s'il n'est pas hors terrain
                if persoRect.left >= 10:
                    persoRect.move_ip(-10,0)
                    
                    # Si ça touche la fin:
                    if persoRect.colliderect(endRect):
                        
                        # Pour chaque niveau, on se réfère au compteur de niveau
                        if z == 0:
                            Surface_Background =  pygame.image.load(r"./bg1.jpg")
                            map = open(r"./map1.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 1
                            
                        elif z == 1:
                            pygame.image.load(r"./bg2.jpg")
                            map = open(r"./map2.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 2
                            
                        elif z == 2:
                            pygame.image.load(r"./bg3.jpg")
                            map = open(r"./map3.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 3
                            
                        elif z == 3:
                            pygame.image.load(r"./bg4.jpg")
                            map = open(r"./map4.txt", 'r')
                            map_lines = map.readlines()
                            Load_Map()
                            fenetre.blit(fond, (0, 0))
                        
                        # On rafraîchit la fenêtre
                        fenetre.blit(fond, (0,0))
                        
                    # Si on entre en collision avec un mur:    
                    if (persoRect.collidelist(Wall_list) != -1):
                        persoRect.move_ip(10,0)
                        continuer = False
            
            
            # Si [FLECHE_DROITE]:
            if dicKeys[K_RIGHT]:
                
                # On bouge le rect de collision s'il est dans le terrain
                if persoRect.righ < Screen_Width:
                    persoRect.move_ip(10,0)
                    
                    # Si ça touche la fin:
                    if persoRect.colliderect(endRect):
                           
                        # Pour chaque niveau, on se réfère au compteur de niveau
                        if z == 0:
                            Surface_Background =  pygame.image.load(r"./bg1.jpg")
                            map = open(r"./map1.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 1
                            
                        elif z == 1:
                            pygame.image.load(r"./bg2.jpg")
                            map = open(r"./map2.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 2
                            
                        elif z == 2:
                            pygame.image.load(r"./bg3.jpg")
                            map = open(r"./map3.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 3
                            
                        elif z == 3:
                            pygame.image.load(r"./bg4.jpg")
                            map = open(r"./map4.txt", 'r')
                            map_lines = map.readlines()
                            Load_Map()
                            fenetre.blit(fond, (0, 0))
                        
                        # On rafraîchit la fenêtre
                        fenetre.blit(fond, (0,0))
                        
                    # Si le perso entre en collision avec un mur:    
                    if (persoRect.collidelist(Wall_list) != -1):
                       persoRect.move_ip(-10,0)
                       continuer = False
            
            # Si [FLECHE_HAUT]:
            if dicKeys[K_UP]:
                
                # On bouge le rect du perso s'il est dans la limite du terrain
                if persoRect.top > 0:
                    persoRect.move_ip(0,-10)
                    
                    # Si on touche la sortie:
                    if persoRect.colliderect(endRect):
                           
                        # Pour chaque niveau, on se réfère au compteur de niveau
                        if z == 0:
                            Surface_Background =  pygame.image.load(r"./bg1.jpg")
                            map = open(r"./map1.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 1
                            
                        elif z == 1:
                            pygame.image.load(r"./bg2.jpg")
                            map = open(r"./map2.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 2
                            
                        elif z == 2:
                            pygame.image.load(r"./bg3.jpg")
                            map = open(r"./map3.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 3
                            
                        elif z == 3:
                            pygame.image.load(r"./bg4.jpg")
                            map = open(r"./map4.txt", 'r')
                            map_lines = map.readlines()
                            Load_Map()
                            fenetre.blit(fond, (0, 0))
                        
                        # On rafraîchit la fenêtre
                        fenetre.blit(fond, (0,0))
                    
                    # Si on touche un mur:    
                    if (persoRect.collidelist(Wall_list) != -1):
                        persoRect.move_ip(0,10)
                        continuer = False
            
            # Si [FLECHE_BAS]:            
            if dicKeys[K_DOWN]:
                
                # On bouge le rect si le perso est dans le terrain
                if persoRect.bottom < Screen_Height:
                    persoRect.move_ip(0,10)
                    
                    # Si on touche la fin:
                    if persoRect.colliderect(endRect):
                          
                        # Pour chaque niveau, on se réfère au compteur de niveau
                        if z == 0:
                            Surface_Background =  pygame.image.load(r"./bg1.jpg")
                            map = open(r"./map1.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 1
                            
                        elif z == 1:
                            pygame.image.load(r"./bg2.jpg")
                            map = open(r"./map2.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 2
                            
                        elif z == 2:
                            pygame.image.load(r"./bg3.jpg")
                            map = open(r"./map3.txt", 'r')
                            map_lines = map.readlines()
                            Wall_list = []
                            Load_Map()
                            fenetre.blit(fond, (0,0))
                            z = 3
                            
                        elif z == 3:
                            pygame.image.load(r"./bg4.jpg")
                            map = open(r"./map4.txt", 'r')
                            map_lines = map.readlines()
                            Load_Map()
                            fenetre.blit(fond, (0, 0))
                        
                        # On rafraîchit la fenêtre
                        fenetre.blit(fond, (0,0))
                    
                    # Si on entre en collision avec un mur:
                    if (persoRect.collidelist(Wall_list) != -1):
                        persoRect.move_ip(0,-10)
                        continuer = False
            
            # Si [ECHAP]:
            if dicKeys[K_ESCAPE]:
                continuer = False
                break
    
    # On rafraîchit      
    fenetre.blit(fond, (0,0))
    Display_wall()
    
    # On rafraîchit le rect du perso et le rect de sortie spécifiquement
    fenetre.blit(perso, persoRect)
    fenetre.blit(exit,exitRect)
    
    # On met à jour la fenêtre pygame
    pygame.display.update()

# On montre les murs
Display_wall()

# On ferme la carte
map.close()

# On quitte pygame
pygame.quit()
