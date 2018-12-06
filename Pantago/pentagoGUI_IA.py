import pygame, sys
from random import random
from pygame import *
from bases import *
#permettra de choisir la taille du tableau en fonction de n
def test_plateau(n):
    if n==6:
        #plateau pour n=6
        Plato = pygame.image.load('plateau01_01.png')
    elif n==12:
        #plateau pour n=12
        Plato = pygame.image.load('plateau02_01_f.png')
    elif n==4:
        Plato = pygame.image.load('plateau00_04.png')
    elif n==8:
        Plato = pygame.image.load('plateau08.png')
    elif n==10:
        Plato = pygame.image.load('plateau10.png')
    return Plato
#test qui permet de choisir les pions orange en fonction de n
def test_cross(n):
    if n==6:
        #pion orange (en croix) pour n=6
        Cross = pygame.image.load('cross01_01.png')
    elif n==12:
        #pion orange (toujours en croix)pour n=12
        Cross = pygame.image.load('cross01_02.png')
    elif n==4:
        Cross = pygame.image.load('cross01_04.png')
    elif n==8:
        Cross = pygame.image.load('cross01_08.png')
    elif n==10:
        Cross = pygame.image.load('cross01_10.png')
    return Cross
#test qui permet de choisir les pions bleu en fonction de n
def test_ring(n):
    if n==6:
        #pion bleu (circulaire) pour n=6
        Ring = pygame.image.load('Ring01_01.png')
    elif n==12:
        #pion bleu (encore circulaire) pour n=12
        Ring = pygame.image.load('Ring01_02.png')
    elif n==4:
        Ring = pygame.image.load('Ring01_04.png')
    elif n==8:
        Ring = pygame.image.load('Ring01_08.png')
    elif n==10:
        Ring = pygame.image.load('Ring01_10.png')
    return Ring

def test_neon(n):
    if n==6:
        maSurface.blit(neon06,(63,179))
    elif n==12:
        maSurface.blit(neon12,(63,179))
    elif n==4:
        maSurface.blit(neon04,(63,179))
    elif n==8:
        maSurface.blit(neon08,(63,179))
    elif n==10:
        maSurface.blit(neon10,(63,179))

def win(joueur,n):
    maSurface.blit(BGF,(0,0))
    test_neon(n)
    maSurface.blit(quit,(544,418))
    maSurface.blit(replay,(544,660))
    maSurface.blit(level,(544,180))
    pygame.mixer.fadeout(300)
    pygame.mixer.stop()
    sound = pygame.mixer.Sound("vo_blue00.wav")
    son = pygame.mixer.Sound("vo_orange00.wav")
    souund=pygame.mixer.Sound("vo_equality.wav")
    if joueur==1:
        sound.play()
        maSurface.blit(blue,(527,0))
    elif joueur==2:
        son.play()
        maSurface.blit(orange,(527,0))
    else:
        souund.play()
        maSurface.blit(equality,(527,0))

def verif(plateau,c,l,joueur) :
    if plateau[l][c] != 0:
        return False
    else :
        return True

def change(plateau,c,l,joueur) :
    plateau[l][c] = joueur
    return plateau

def dessine(plateau,C,n) :
    Cross=test_cross(n)
    Ring=test_ring(n)
    maSurface.blit(Plato,(112,112))
    for ligne in range(n):
        for colonne in range(n):
            if plateau[ligne][colonne] == 1:
                maSurface.blit(Ring,((((colonne)*C)+112.5)//1,(((ligne)*C)+112.5)//1))
            elif plateau[ligne][colonne] == 2:
                maSurface.blit(Cross,((((colonne)*C)+112.5)//1,(((ligne)*C)+112.5)//1))
#permet de fermer le menu d'option
def close1(joueur):
    if joueur==2:
        maSurface.blit(HBO,(898,0))
    elif joueur==1:
        maSurface.blit(HBB,(898,0))
    maSurface.blit(option,(1516,18))

def anime(wins,joueur):
    maSurface.blit(BGF,(0,0))
    test_neon(n)
    if wins == 1:
        maSurface.blit(surrender,(527,0))
    elif joueur == 1:
        maSurface.blit(blue,(527,0))
    elif joueur == 2:
        maSurface.blit(orange,(527,0))
    else:
        maSurface.blit(equality,(527,0))
    b = pygame.mixer.Sound("door_open_01.wav")
    b.play()
    x=0
    a=0
    while a==0:
        maSurface.blit(ANTIANIME,(0,644))
        maSurface.blit(door,((-x*326)+1274,644))
        maSurface.blit(ANTIANIME,(0,644))
        display.flip()
        time.wait(75)
        x+=1
        if x == 15:
            a=1
#pemrmet de relancer les images du jeu
def replaydef(n):
    maSurface.blit(Background,(0,0))
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
    if n==4:
        jouerSonlvl4.play(-1)
    elif n==6:
        jouerSonlvl6.play(-1)
    elif n==8:
        jouerSonlvl8.play(-1)
    elif n==10:
        jouerSonlvl10.play(-1)
    elif n==12:
        jouerSonlvl12.play(-1)

regles = [
	(('animal a poils',),
		'animal est mammifere'),
	(('animal donne lait',),
		'animal est mammifere'),
	(('animal a plumes',),
		'animal est oiseau'),
	(('animal vole', 'animal pond oeufs',),
		'animal est oiseau'),
	(('animal mange viande',),
		'animal est carnivore'),
	(('animal a dents pointues', 'animal a griffes',
		  'animal a yeux vers avant',),
		'animal est carnivore'),
	(('animal est mammifere', 'animal a sabots',),
		'animal est ongule'),
	(('animal est mammifere', 'animal rumine',),
		'animal est ongule'),
	(('animal est mammifere', 'animal est carnivore',
		  'animal a couleur brune', 'animal a taches sombres',),
		'animal est guepard'),
	(('animal est mammifere', 'animal est carnivore',
		  'animal a couleur brune', 'animal a raies noires',),
		'animal est tigre'),
	(('animal est ongule', 'animal a long cou',
		  'animal a longues pattes', 'animal a taches sombres',),
		'animal est girafe'),
	(('animal est ongule', 'animal a raies noires',),
		'animal est zebre'),
	(('animal est oiseau', 'animal ne vole pas', 'animal a long cou',
		  'animal a longues pattes', 'animal est noir est blanc',),
		'animal est autruche'),
	(('animal est oiseau', 'animal ne vole pas', 'animal nage',
		  'animal est noir et blanc',),
		'animal est pingouin'),
	(('animal est oiseau', 'animal vole bien',),
		'animal est albatros'),
]
def Pose_pion(joueur,plateau,n,C):
    if joueur == 1:
        for ligne in range(n):
            if (((ligne*C)+112.5)//1 <= cx <= ((ligne+1)*C)+112.5)//1:
                for k in range (n):
                    if ((k*C)+112.5)//1 <= cy <= (((k+1)*C)+112.5)//1:
                        libre = verif(plateau,ligne,k,joueur)
                        if libre:
                            plus1.play()
                            plateau = change(plateau,ligne,k,joueur)
                            dessine(plateau,C,n)
                            return 1
    else:
        while True:
            ligne = int(random()*n)
            k = int(random()*n)
            libre = verif(plateau, ligne, k, joueur)
            if libre:
                plus1.play()
                plateau = change(plateau, ligne, k, joueur)
                dessine(plateau, C, n)
                return 1
def Rotation(plateau,joueur,n,C):
    if joueur == 1:
        if 132 <= cx <= 431:
            if 19 <= cy <= 93:
                e=1
                c=1
                plus2.play()
                Rotate_Final(plateau,n,e,c)
                dessine(plateau,C,n)
                return 1
        if 19 <= cx <= 93:
            if 132 <= cy <= 431:
                e=1
                c=0
                plus2.play()
                Rotate_Final(plateau,n,e,c)
                dessine(plateau,C,n)
                return 1
        if 469 <= cx <= 768:
            if 19 <= cy <= 93:
                e=2
                c=1
                plus2.play()
                Rotate_Final(plateau,n,e,c)
                dessine(plateau,C,n)
                return 1
        if 807 <= cx <= 881:
            if 132 <= cy <= 431:
                e=2
                c=0
                plus2.play()
                Rotate_Final(plateau,n,e,c)
                dessine(plateau,C,n)
                return 1
        if 19 <= cx <= 93:
            if 469 <= cy <= 768:
                e=3
                c=0
                plus2.play()
                Rotate_Final(plateau,n,e,c)
                dessine(plateau,C,n)
                return 1
        if 132 <= cx <= 431:
            if 807 <= cy <= 881:
                e=3
                c=1
                plus2.play()
                Rotate_Final(plateau,n,e,c)
                dessine(plateau,C,n)
                return 1
        if 469 <= cx <= 768:
            if 807 <= cy <= 881:
                e=4
                c=1
                plus2.play()
                Rotate_Final(plateau,n,e,c)
                dessine(plateau,C,n)
                return 1
        if 807 <= cx <= 881:
            if 469 <= cy <= 768:
                e=4
                c=0
                plus2.play()
                Rotate_Final(plateau,n,e,c)
                dessine(plateau,C,n)
                return 1
    else:
        e = int(random()*5)
        c = int(random()*5)
        plus2.play()
        Rotate_Final(plateau, n, e, c)
        dessine(plateau, C, n)
        return 1

def Tour(tour,plateau,joueur,n,C):
    if tour==0:
        A=Pose_pion(joueur,plateau,n,C)
        if A==1:
            tour=1
            return 1
    if tour==1:
        B=Rotation(plateau,joueur,n,C)
        if B==1:
            tour=2
            return 2
        else:
            tour=1
            return 1
    return 0

pygame.init()
start = pygame.mixer.Sound("startup_02_01.wav")
start.play()
#musique d'ambience
jouerSonlvl4=pygame.mixer.Sound("mp_coop_lobby_2_c1.wav")
jouerSonlvl6=pygame.mixer.Sound("mp_coop_lobby_2_c2.wav")
jouerSonlvl8=pygame.mixer.Sound("mp_coop_lobby_2_c4.wav")
jouerSonlvl10=pygame.mixer.Sound("mp_coop_lobby_2_c5.wav")
jouerSonlvl12=pygame.mixer.Sound("mp_coop_lobby_2_c6.wav")
plus1 = pygame.mixer.Sound("button_synth_positive_01.wav")
plus2 = pygame.mixer.Sound("button_synth_negative_02.wav")
plus3 = pygame.mixer.Sound("menu_accept.wav")
plus4 = pygame.mixer.Sound("menu_back.wav")
plus5 = pygame.mixer.Sound("menu_focus.wav")
plus6 = pygame.mixer.Sound("buttonclick.wav")
seeyousoon = pygame.mixer.Sound("seeyousoon.wav")
maSurface = pygame.display.set_mode((1600, 900),pygame.FULLSCREEN)
pygame.display.set_caption('Pentago')
Background = pygame.image.load('background1_widescreen_01_01_00.png')
Back_ground = pygame.image.load('background1_widescreen_00_01_00.png')
Back_ground_= pygame.image.load('black_floor_metal_bullseye_001_00_01_00.png')
Background_ = pygame.image.load('black_floor_metal_bullseye_001_01_01_00.png')
#permettront de fermer le menu d'option en fonction du tour d'un joueur
HBO = pygame.image.load('half_background_orange_00.png')
HBB = pygame.image.load('half_background_blue_00.png')
LB = pygame.image.load('light_blue00_01.png')
#idem mais fait tourner le cadrant vers la droite (est orangatre)
LO = pygame.image.load('light_orange00_01.png')
LGB = pygame.image.load('light_blue01_01.png')
LGO = pygame.image.load('light_orange01_01.png')
#icon d'option
option = pygame.image.load('icon_option_00_00_00.png')
#icon de fermeture
close = pygame.image.load('close_icon_00_00_00.png')
#menu d'option (avec ses bouttons)
menu = pygame.image.load('button_econ_blue_over_00_00_00.png')
BGF=pygame.image.load('bg_f_00_00_00.png')
door=pygame.image.load('metal_door_anime00_12.png')
ANTIANIME = image.load('ANTIANIME.png')
#icons affichant l'abondon des joueurs l'orsqu'il quitteront le jeu sans avoir fini leur partie
surrender= image.load('icon_player_win_00_00_01.png')
equality=image.load('icon_player_win_01_00_00.png')
blue=image.load('icon_player_win_02_00_00.png')
orange=image.load('icon_player_win_03_00_00.png')
level=image.load('boutton_level_00_00.png')
replay=image.load('boutton_replay_00_00.png')
quit=image.load('boutton_quit_00_00.png')
neon04=image.load('progress_board_00_04_00.png')
neon06=image.load('progress_board_00_06_00.png')
neon08=image.load('progress_board_00_08_00.png')
neon10=image.load('progress_board_00_10_00.png')
neon12=image.load('progress_board_00_12_00.png')
BGLS=image.load('background_level_selector_00_00.png')
rule=image.load('rule_00_00_00.png')

maSurface.blit(Background,(0,0))
n=6
#affichage du jeu
Plato=test_plateau(n)
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
tour=0
compteur=0
#ne fonctionnera pas bien avec joueur 1
joueur=2
inProgress = True
jouerSonlvl6.play(-1)
wins=1
#permet de savoir si le menu de selection des niveau est ouvert
SL=0
C=675/n

menus=0
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
                    plus6.play()
            if menus==1 and 1046 <= cx <= 1441 :
                if 84 <= cy <= 281 :
                    plus5.play()
                    seeyousoon.play()
                    inProgress=False
            if menus==1 and 1046 <= cx <= 1441 :
                if 609 <= cy <= 817:
                    plus5.play()
                    maSurface.blit(rule,(700,0))
                    maSurface.blit(close,(1516,18))
            if menus==0 and wins==1 and 1516 <= cx <= 1579 :
                if 18 <= cy <= 81 :
                    plus4.play()
                    maSurface.blit(menu,(988,26))
                    maSurface.blit(close,(1516,18))
                    menus=1
            elif menus==1 and 1516 <= cx <= 1579 :
                if 18 <= cy <= 81 :
                    plus4.play()
                    close1(joueur)
                    menus=0
            elif wins==0 and SL==0 and 544 <= cx <= 1115 :
                if 418 <= cy <= 577 :
                    plus6.play()
                    seeyousoon.play()
                    inProgress=False
            if wins==0 and SL==0 and 544 <= cx <= 1115 :
                if 660 <= cy <= 819 :
                    plus6.play()
                    joueur=2
                    tour=0
                    compteur=0
                    plateau=[[0] * n for q in range(n)]
                    wins=1
                    replaydef(n)
            else:
                if menus==0 and wins==1:
                    tour=Tour(tour,plateau,joueur,n,C)
                    victoire = gagne(plateau,joueur,n,(n-1))
                    if tour == 1:
                        if victoire :
                            win(joueur,n)
                            wins=0
                    elif tour==2:
                        victoire = gagne(plateau,joueur,n,(n-1))
                        if not victoire:
                            if joueur == 1 :
                                joueur =2
                                maSurface.blit(Background_,(1025,226))
                            else :
                                joueur =1
                                maSurface.blit(Back_ground_,(1025,226))
                            tour=0
                            eq=0
                            for ligne in range(n):
                                for colonne in range(n):
                                    if plateau[ligne][colonne]!=0:
                                        eq+=1
                            if eq==(n**2):
                                joueur=0
                                win(joueur,n)
                                wins=0
                        else :
                            win(joueur,n)
                            wins=0
            if menus==1 and 1046 <= cx <= 1441 :
                if 354 <= cy <= 551 :
                    SL=1
                    wins=0
                    menus=0
                    pygame.mixer.fadeout(300)
                    pygame.mixer.stop()
                    maSurface.blit(BGLS,(0,0))
                    plus5.play()
            #test des bouttons de selection du niveau du plateau
            elif SL == 1:
                maSurface.blit(BGLS,(0,0))
                if 327 <= cx <= 461 :
                    if 340 <= cy <= 609 :
                        plus3.play()
                        n=4
                        C=675/n
                        joueur=2
                        tour=0
                        plateau=[[0] * n for q in range(n)]
                        wins=1
                        Plato=test_plateau(n)
                        replaydef(n)
                        SL=0
                if 572 <= cx <= 706 :
                    if 340 <= cy <= 609 :
                        plus3.play()
                        n=6
                        C=675/n
                        joueur=2
                        tour=0
                        plateau=[[0] * n for q in range(n)]
                        wins=1
                        Plato=test_plateau(n)
                        replaydef(n)
                        SL=0
                if 817 <= cx <= 951 :
                    if 340 <= cy <= 609 :
                        plus3.play()
                        n=8
                        C=675/n
                        joueur=2
                        tour=0
                        plateau=[[0] * n for q in range(n)]
                        wins=1
                        Plato=test_plateau(n)
                        replaydef(n)
                        SL=0
                if 1062 <= cx <= 1196 :
                    if 340 <= cy <= 609 :
                        plus3.play()
                        n=10
                        C=675/n
                        joueur=2
                        tour=0
                        plateau=[[0] * n for q in range(n)]
                        wins=1
                        Plato=test_plateau(n)
                        replaydef(n)
                        SL=0
                if 1307 <= cx <= 1441 :
                    if 340 <= cy <= 609 :
                        plus3.play()
                        n=12
                        C=675/n
                        joueur=2
                        tour=0
                        plateau=[[0] * n for q in range(n)]
                        wins=1
                        Plato=test_plateau(n)
                        replaydef(n)
                        SL=0
    pygame.display.update()
anime(wins,joueur)
pygame.quit()