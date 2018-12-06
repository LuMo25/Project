#importation des programmes et modules qui nous serviront à l'avenir
import pygame, sys
from pygame import *
#permet de vérifier si une case est libre lorqu'on fera appelle à cette fonction
def verif(plateau,c,l,joueur) :
    if plateau[l][c] != 0:
        return False
    else :
        return True
#permet de changer une valeur de la liste bidimensionelle représentant notre plateau
def change(plateau,c,l,joueur) :
    plateau[l][c] = joueur
    return plateau
#dessinera les pions après un raffréchissement complet de notre plateau (les cadrant ayant une tous une texture différente) en fonction de la taille de celui ci
def dessine(plateau,C,n) :
    maSurface.blit(Plato,(112,112))
    for ligne in range(n):
        for colonne in range(n):
            """if plateau[ligne][colonne] == 1:
                maSurface.blit(Ring,((((colonne)*C)+112.5)//1,(((ligne)*C)+112.5)//1))
            elif plateau[ligne][colonne] == 2:
                maSurface.blit(Cross,((((colonne)*C)+112.5)//1,(((ligne)*C)+112.5)//1))"""
#permet de fermer le menu d'option
def close1(joueur):
    maSurface.blit(HBB,(898,0))
    maSurface.blit(option,(1516,18))
def Pose_pion(plateau,n,C):
    #permettent de créer un ordre lors d'un tour de jeu
    tour=0
    #test les coordonnés pour choisir où l'on veut faire apparaître un pion
    for ligne in range(n):
        if menus==0 and (((ligne*C)+112.5)//1 <= cx <= ((ligne+1)*C)+112.5)//1:
            for k in range (n):
                if ((k*C)+112.5)//1 <= cy <= (((k+1)*C)+112.5)//1:
                    libre = verif(plateau,ligne,k,joueur)
                    if libre:
                        plateau = change(plateau,ligne,k,joueur)
                        dessine(plateau,C,n)
pygame.init()
#taille de l'écran
maSurface = pygame.display.set_mode((1600, 900),pygame.FULLSCREEN)
#nom de l'écran
pygame.display.set_caption('Pentago')
start = pygame.mixer.Sound("startup_02_01.wav")
start.play()
#le fond d'écan
Background = pygame.image.load('background1_widescreen_00_01_00.png')
#permettront de fermer le menu d'option en fonction du tour d'un joueur
HBB = pygame.image.load('half_background_blue_00.png')
#image qui permettre de faire tourner le cadrant vers la gauche (garde un aspect décorative, et est de couleur bleuté comme son nom l'indique)
LB = pygame.image.load('light_blue00_01.png')
#idem mais fait tourner le cadrant vers la droite (est orangatre)
LO = pygame.image.load('light_orange00_01.png')
#idem que pour LB mais pivoté de 90°
LGB = pygame.image.load('light_blue01_01.png')
#idem que pour LO mais pivoté de 90°
LGO = pygame.image.load('light_orange01_01.png')
#icon d'option
option = pygame.image.load('icon_option_00_00_00.png')
#icon de fermeture
close = pygame.image.load('close_icon_00_00_00.png')
#menu d'option (avec ses bouttons)
menu = pygame.image.load('button_econ_blue_over_00_00_00.png')
Plato=image.load('tableau01.png')
#préparation de l'affichage du jeu et de son initialisation
maSurface.blit(Background,(0,0))
a=pygame.mixer.Sound("sp_a5_finale01_03.wav")
a.play(-1)
n=5
maSurface.blit(Plato,(112,112))
maSurface.blit(LGO,(132,19))
maSurface.blit(LGO,(469,19))
maSurface.blit(LGO,(132,807))
maSurface.blit(LGO,(469,807))
maSurface.blit(LB,(19,132))
maSurface.blit(LB,(19,469))
maSurface.blit(LB,(807,132))
maSurface.blit(LB,(807,469))
maSurface.blit(option,(1516,18))
p=(n-1)
plateau=[[0] * n for q in range(n)]
#permettent de créer un ordre lors d'un tour de jeu
tour=1
compteur=0
#ne fonctionnera pas bien avec joueur 1
joueur=2
#variable servant à fermer notre boucle de jeu
inProgress = True
#son d'embiance joué
#servira pour savoir si un joueur à gagné et permettera d'éviter de pouvoir continuer à poser des pions (ou même de quitter le jeu sans le voloire lorsqu'on cliquera sur une case prise)
wins=1
SL=0
if n==6:
    #coéffitiant qui permettra de placer correctement les pions à l'endroie voulu
    C=112.5
elif n==12:
    C=56.5
elif n==4:
    C=168.75
elif n==8:
    C=84.375
elif n==10:
    C=67.5
#idem que pour savoir si un joueur à gagné sauf que celle ci permet de savoir si le menu d'option est ouvert
menus=0
#démarrage
while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
        #on veut test si on clique sur une case/boutton
        if event.type == MOUSEBUTTONUP:
            cx,cy = event.pos
            if wins==0 and 544 <= cx <= 1115 :
                if 180 <= cy <= 339 :
                    SL=1
            #coordonné du boutton pour quitter du menu d'option
            if menus==1 and 1046 <= cx <= 1441 :
                if 84 <= cy <= 281 :
                    #même princique que plus haut
                    inProgress=False
            #coordonné de l'iconne d'option
            if menus==0 and wins==1 and 1516 <= cx <= 1579 :
                if 18 <= cy <= 81 :
                    maSurface.blit(menu,(988,26))
                    maSurface.blit(close,(1516,18))
                    menus=1
            #on utilise un elif pour eviter de fermer puis réouvrir le menu d'option
            elif menus==1 and 1516 <= cx <= 1579 :
                if 18 <= cy <= 81 :
                    close1(joueur)
                    menus=0
            #coordonné du boutton pour quitter lors de la fin du jeu
            elif wins==0 and SL==0 and 544 <= cx <= 1115 :
                if 418 <= cy <= 577 :
                    #on arrête la boucle et le jeu se ferme par l'animation en fin de programme
                    inProgress=False
    pygame.display.update()
pygame.quit()