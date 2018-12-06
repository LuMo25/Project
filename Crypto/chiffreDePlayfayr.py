import re
import pygame
from pygame.locals import *
import string

#verification si doublon & insert x si doublon puis decale le reste
def bigramme(S):
    chaine=[0]*len(S)
    for i in range(0,len(S)):
        chaine[i]=S[i]
    x=0
    while (x+1<len(chaine)):
        if chaine[x] == chaine[x+1]:
            chaine.insert(x+1,'x')
        x+=2
    result = ''.join(chaine)
    return result
#On suprime tout les symboles non voulu
def supretion(S) :
    S = ''.join([x[0] for x in zip(S, S.upper()) if x[0] != x[1]])
    S= re.sub('[^A-Za-z0-9]+', '', S)
    return S
#remplissage d'une liste a deux dim avec la clé
def clef(S):
    chaine = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    x=0
    for i in range (5):
        for j in range(5):
            chaine[i][j]=S[x]
            x+=1
    return chaine
#cherche l'index d'un caractere
def searching(S,C):
    chaine=[]
    for i in range (5):
        for j in range(5):
            if S[i][j]==C:
                chaine=[i,j]
    return chaine
#change tout les W de la chaine en V
def Wv(S):
    chaine=[0]*len(S)
    for i in range(len(S)):
        if S[i] == 'w':
            chaine[i] = 'v'
        else :
            chaine[i]=S[i]
    result = ''.join(chaine)
    return result

#ajoutera un X si la les chaine de caractére est impaire
def impaire(S):
    chaine = []
    if (len(S)%2)==1:
        chaine.append(S)
        chaine.append('x')
        S = ''.join(chaine)
    return S

#separe une chaine de caractere dans une liste en bigramme
def SPACEBigramme(S):
    taille=len(S)//2
    chaine=[0]*taille
    x=0
    for i in range(0,taille):
        chaine[i]=S[x]+(S[x+1])
        x=x+2
    return chaine

#chiffrage bigramme
def chiffrageBigramme(bigramme,clef):
    o=searching(clef,bigramme[0])
    p=searching(clef,bigramme[1])
    o,p=Chiffrage(o,p)
    bigramme=[0]*2
    bigramme[0]=clef[o[0]][o[1]]
    bigramme[1]=clef[p[0]][p[1]]
    result = ''.join(bigramme)
    return result

#fonction de permutation valeur selon clé
def Chiffrage(N1,N2):
    #ligne
    if N1[0]==N2[0]:
        if N1[1]<4:
            N1[1]=N1[1]+1
        elif N1[1]==4:
            N1[1]=0
        if N2[1]<4:
            N2[1]=N2[1]+1
        elif N2[1]==4:
            N2[1]=0
        return N1,N2
    #colonne
    elif N1[1]==N2[1]:
        if N1[0]<4:
            N1[0]=N1[0]+1
        elif N1[0]==4:
            N1[0]=0
        if N2[0]<4:
            N2[0]=N2[0]+1
        elif N2[0]==4:
            N2[0]=0
        return N1,N2
    #rectangle
    else:
        N1[1],N2[1]=N2[1],N1[1]
        return N1,N2

def Dechiffrage(N1,N2):
    #ligne
    if N1[0]==N2[0]:
        if N1[1]>0:
            N1[1]=N1[1]-1
        elif N1[1]==0:
            N1[1]=4
        if N2[1]>0:
            N2[1]=N2[1]-1
        elif N2[1]==0:
            N2[1]=4
        return N1,N2
    #colonne
    elif N1[1] == N2[1]:
        if N1[0]>0:
            N1[0]=N1[0]-1
        elif N1[0]==0:
            N1[0]=4
        if N2[0]>0:
            N2[0]=N2[0]-1
        elif N2[0]==0:
            N2[0]=4
        return N1,N2
    #rectangle
    else:
        N1[1],N2[1]=N2[1],N1[1]
        return N1,N2

#déchiffrement bigramme
def dechiffrageBigramme(bigramme,clé):
    o=searching(clé,bigramme[0])
    p=searching(clé,bigramme[1])
    o,p=Dechiffrage(o,p)
    bigramme=[0]*2
    bigramme[0]=clé[o[0]][o[1]]
    bigramme[1]=clé[p[0]][p[1]]
    chaineCaract = ''.join(bigramme)
    return chaineCaract

#dechiffrage text entier
def dechiffrageText(texte,clef):
    taille=len(texte)
    chaine=[0]*taille
    for i in range(0,taille):
        chaine[i]=dechiffrageBigramme(texte[i],clef)
    return chaine
#chiffrage texte entier
def Chiffrage_Texte(texte,clé):
    a=len(texte)
    liste=[0]*a
    for x in range(0,a):
        liste[x]=chiffrageBigramme((texte[x]),clé)
    return liste

#interface graphique
def GUI():
    x=0
    chaine = [[0] * 5 for q in range(5)]
    pygame.init()
    maSurface = pygame.display.set_mode((1600, 900),pygame.FULLSCREEN)
    #nom de l'écran
    pygame.display.set_caption('Cryptocaco')
    start = pygame.mixer.Sound("startup_02_01.wav")
    start.play()
    b0=pygame.mixer.Sound("sp_a2_trust_fling_b0.wav")
    b0.play()
    #le fond d'écan
    Background = pygame.image.load('Test_background_01.png')
    #préparation de l'affichage du jeu et de son initialisation
    maSurface.blit(Background,(0,0))
    icone = pygame.image.load("tableau01.png")
    pygame.display.set_icon(icone)
    #affichage menu
    new = pygame.image.load("icon_letter_indicator_02.png")
    #Titre
    pygame.display.set_caption("Le chiffrage FAIR PLAY")

    #test affichage lettre dans case
    affichageAlphabet(0,maSurface)
    r=affichagePlateau(chaine,maSurface)
    listeRemplie=0
    lettre=list(string.ascii_uppercase)[listeRemplie]
    ouverture = 1
    pygame.display.flip()
    while ouverture:
        for event in pygame.event.get():
            if event.type == QUIT:
                ouverture = 0
            if listeRemplie==25:
                print("Nice potato!")
                pygame.mixer.stop()
                ouverture = 0
                return chaine
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                cx,cy = event.pos
                chaine,listeRemplie,lettre,x=Posepion(r,chaine,cx,cy,lettre,maSurface,listeRemplie,x)

#affichage de la lettre qu'il faut poser
def affichageAlphabet(x,maSurface):
    TOILET = pygame.image.load("title_04.png")
    maSurface.blit(TOILET,(930,126))
    a=list(string.ascii_uppercase)[x]
    myfont = pygame.font.SysFont("monospace", 30)
    new = pygame.image.load("icon_letter_indicator_02.png")
    maSurface.blit(new,(1466,126))
    label = myfont.render(a, 1, (0,0,0))
    maSurface.blit(label, (1525, 175))

#Affichage du plateau
def affichagePlateau(liste,maSurface):
    C=134
    Test= pygame.image.load("case_tab_02.png")
    x = 145
    y = 127
    quad = [[0] * (5) for i in range(5)]
    for l in range(5):
        for c in range(5):
            quad[l][c] = liste[l][c]
            pygame.display.flip()
    r=[]
    for i in range(5):
        for e in range(5):
            r.append((x,y))
            x += 134
            pygame.display.flip()
        x=134
        y = y + 134

    for ligne in range(5):
        for colonne in range(5):
            maSurface.blit(Test,((((colonne)*C)+130)//1,(((ligne)*C)+117)//1))

    liste = [[0] * (5) for i in range(5)]
    i=0
    for x in range (5):
        for y in range(5):
            liste[x][y]=r[i]
            i+=1
    return liste

#Pose des lettres pour la clé
def Posepion(r,liste,cx,cy,lettre,maSurface,listeRemplie,x):
    b0=pygame.mixer.Sound("sp_a2_trust_fling_b0.wav")
    b1=pygame.mixer.Sound("sp_a2_trust_fling_b1.wav")
    b2=pygame.mixer.Sound("sp_a2_trust_fling_b2.wav")
    b3=pygame.mixer.Sound("sp_a2_trust_fling_b3.wav")
    b4=pygame.mixer.Sound("sp_a2_trust_fling_b4.wav")
    b5=pygame.mixer.Sound("sp_a2_trust_fling_b5.wav")
    for i in range(5):
        for j in range(5):
            if r[i][j][0]<cx<r[i][j][0]+134 and r[i][j][1]<cy<r[i][j][1]+90:
                if 134<cx<804 and 134<cy<804:
                    if liste[i][j%5]==0:
                        x+=1
                        if x==5:
                            pygame.mixer.stop()
                            b0.play(-1)
                            b1.play(-1)
                        if x==1:
                            pygame.mixer.stop()
                            b0.play(-1)
                            b5.play(-1)
                        if x==10:
                            pygame.mixer.stop()
                            b0.play(-1)
                            b2.play(-1)
                        if x==15:
                            pygame.mixer.stop()
                            b0.play(-1)
                            b3.play(-1)
                        if x==20:
                            pygame.mixer.stop()
                            b0.play(-1)
                            b4.play(-1)
                        a=list("abcdefghijklmnopqrstuvxyz")[listeRemplie]
                        liste[i][j%5]=a
                        myfont = pygame.font.SysFont("monospace", 50)
                        label = myfont.render(a, 1, (0,0,0))
                        maSurface.blit(label, (r[i][j][0]+35,r[i][j][1]+25))
                        pygame.display.flip()
                        listeRemplie+=1
                        affichageAlphabet(listeRemplie,maSurface)
                        pygame.display.flip()
    return liste,listeRemplie,lettre,x

def main():
    print("Bonjour, souhaitez vous commencer par: ")
    print("1 : Dechiffrage du fichier txt 2?")
    print("2 : Cryptage/déccryptage de 'Hello world' avec entrée de la clé via l'interface graphique?")
    print("3 : Ou un petit exemple personnel? ")
    choix=0
    while choix<1 or choix>3:
        choix = eval(input())
    if choix==1:
        clefichier=open('cle2.txt','r')
        cletexte = clefichier.readlines()
        cletexte = ''.join(cletexte)
        fichierADechiffrer=open('chiffre2.txt','r')
        monTexte = fichierADechiffrer.readlines()
        monTexte = [element.lower() for element in monTexte]
        monTexte = ''.join(monTexte)
        monTexte = supretion(monTexte)
        monTexte = SPACEBigramme(monTexte)
        print("la clé est la suivante :")
        print(cletexte)
        print("le texte chiffré est le suivant :")
        print(monTexte)
        listecinqdim=clef(cletexte)
        dechiffrage =Chiffrage_Texte(monTexte,listecinqdim)
        dechiffrage = ''.join(dechiffrage)
        print("Le texte déchiffre donne :")
        print(dechiffrage)
    if choix==2:
        texte = "I'm a chiken"
        texte = supretion(texte)
        texte = Wv(texte)
        texte = bigramme(texte)
        texte = impaire(texte)
        texte = SPACEBigramme(texte)
        print(texte)
        cleGUI=GUI()
        print(cleGUI)
        #cleGUI = ''.join(cleGUI)
        #vingtcinq = cleGUI
        #listecinqdim=creationTab5Dim(vingtcinq)
        textecrypte = Chiffrage_Texte(texte,cleGUI)
        print(textecrypte)
        print(Chiffrage_Texte(textecrypte,cleGUI))
    if choix==3:
        clefichier=open('cleperso.txt','r')
        cletexte = clefichier.readlines()
        cletexte = ''.join(cletexte)
        fichierADechiffrer=open('chiffreperso.txt','r')
        monTexte = fichierADechiffrer.readlines()
        monTexte = [element.lower() for element in monTexte]
        monTexte = ''.join(monTexte)
        monTexte = supretion(monTexte)
        monTexte = Wv(monTexte)
        monTexte = bigramme(monTexte)
        monTexte = impaire(monTexte)
        monTexte = SPACEBigramme(monTexte)
        print("la clé est la suivante :")
        print(cletexte)
        print(monTexte)
        listecinqdim=clef(cletexte)
        textecrypte = Chiffrage_Texte(monTexte,listecinqdim)
        print(textecrypte)
        print(Chiffrage_Texte(textecrypte,listecinqdim))

main()
