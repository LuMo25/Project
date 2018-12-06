#include <iostream>
#include <conio.h>
#include <time.h>
#include <future>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Game.h"
#include "Teriminos.h"

Teriminos T1(0,0,0);
Teriminos T2(0,0,0);

Game::Game(int h, int l)
{
    hy = h;
    lx = l;
    srand (time(NULL));
    int r1 = rand() % 6;
    int r2 = rand() % 6;
    T1 = Teriminos(lx/2,0,r1);
    T2 = Teriminos(lx/2,0,r2);
    Creer(h,l,matrice);
    mtmp = matrice; // mtmp = matrice, matrice = matrice + piece joueur

    Affiche(h,l);

    //Testevent();

    while(1)
    {
        Aligne();
        Recreer(h,l);
        Time();
        Event();
        Intergpiece(h,l);
        Psize();
        Affiche(h,l);
        if (Testcol(h,l,T1.posx)==false)
        {
            T1.posy += 1;
        }
        else
        {
            mtmp = matrice;
            int r1 = rand() % 7;
            int r2 = rand() % 7;
            T1 = T2;
            T2 = Teriminos(lx/2,0,r2);
            if (Testcol(h,l,T1.posx))
            {
                break;
            }
        }
    }
    system("cls");
    if (point < 1000)
    {
        std::cout << "\n\n\n\n\n\      nxxXxXX||MDR COMMENT T'AS PERDUE, ON AURRAIT DIT UN NUGGETS CUIT A LA VAPEUR... Mais sans vapeur...||XXxXxx\n\n";
        std::cout << "                                      SCORE: " << point << "\n";
    }
    else
    {
        std::cout << "\n\n\n\n\n\n\n";
        std::cout << "                         .-;+$XHHHHHHX$+;-.\n";
        std::cout << "                     ,;X@@X%/;=----=:/%X@@X/,\n";
        std::cout << "                    =$@@%=.              .=+H@X:\n";
        std::cout << "                  -XMX:                      =XMX=\n";
        std::cout << "                 /@@:                          =H@+\n";
        std::cout << "                %@X,                            .$@$\            T'es pas sense voir ca...\n";
        std::cout << "               +@X.                               $@%\n";
        std::cout << "              -@@,                                .@@=\n";
        std::cout << "              %@%                                  +@$\n";
        std::cout << "              H@:                                  :@H\                        SCORE: " << point << "\n";
        std::cout << "              H@:         :HHHHHHHHHHHHHHHHHHX,    =@H\n";
        std::cout << "              %@%         ;@M@@@@@@@@@@@@@@@@@H-   +@$\n";
        std::cout << "              =@@,        :@@@@@@@@@@@@@@@@@@@@@= .@@:\n";
        std::cout << "               +@X        :@@@@@@@@@@@@@@@M@@@@@@:%@%\n";
        std::cout << "                $@$,      ;@@@@@@@@@@@@@@@@@M@@@@@@$.\n";
        std::cout << "                 +@@HHHHHHH@@@@@@@@@@@@@@@@@@@@@@@+\n";
        std::cout << "                  =X@@@@@@@@@@@@@@@@@@@@@@@@@@@@X=\n";
        std::cout << "                    :$@@@@@@@@@@@@@@@@@@@M@@@@$:\n";
        std::cout << "                      ,;$@@@@@@@@@@@@@@@@@@X/-\n";
        std::cout << "                        .-;+$XXHHHHHX$+;-.\n\n\n\n\n\n\n";
    }

    getch();
}

long Game::ElapsedTime(long begTime)
{
    return ((long) clock() - begTime);
}
void Game::Time() {
	long seconds = timelvl; // permet de gérer le temps
	long begTime;
	begTime = clock();
	while(true) {
		if( ElapsedTime(begTime) >= seconds) {
			break;
		}
	}
}
void Game::Testevent()
{
    int c = 0;
    while(1)
    {
        c = 0;

        c=getch();
        std::cout << std::endl << c << std::endl;
            //h = 104
            //r = 114
    }
}
void Game::Ruels()
{
    system("cls");
    std::cout << "Bienvenu sur...... T TRISTE!!! Le T qui rend triste a cause de... son... A CAUSE D'UN TRUC!\n\n\n\n";




    std::cout << "Le but du jeu\n\nVotre but est de ranger les pieces de Tetris dans la Tetriceroom! \nUne foi qu'une piece est poser vous ne pouvez plus la deplacer.\nSi vous arrivez a completer une ligne celle ci sera suprimer et vous gagnerez 10 points!\n\n";
    std::cout << "Le jeu s'arrete quand vous avez perdu!\n\n\n\n\n";
    std::cout << "Commande\n\n";
    std::cout << "-Fleche gauche, Fleche droite, Fleche du bas --> sert a faire boujer la piece dans la tetrisroom\n";
    std::cout << "-R                                           --> permet de faire tourner la piece\n\n";
    std::cout << "-ECHAP                                       --> quiter";
    getch();
}
void Game::Event() // gére les événements
{
    int c = 0;
    while (1){
    if ( _kbhit() )
    {
        c=getch();
    }
    else
    {
        break;
    }
    }

    if (c == 75 && Testcol(hy,lx,T1.posx - 1) == false && T1.posx > 0)
    {
        T1.posx += -1; //-X

    }
    else if (c == 77  && Testcol(hy,lx,T1.posx + 1) == false && T1.posx + T1.wp + 1 < lx)
    {
        T1.posx += 1; //x

    }
    else if (c == 80 && Testcol(hy,lx,T1.posx) == false)
    {
        T1.posy += 1; //y

    }
    else if (c == 104)
    {
        Ruels();
    }
    else if (c == 114 && Testcol(hy,lx,T1.posx) == false)
    {
        Rotatepiece(4, 4);
    }
}
void Game::Creer(int h, int l, int** m)
{
    matrice = new int*[l];
    for (int x = 0; x < l; x++)
    {
        matrice[x] = new int[h];
    }
    for (int y = 0; y < h; y++)
    {
        for(int x = 0; x < l; x++)
        {
            matrice[x][y] = 0;
        }
    }
    //matrice[1][19] = 1;               // test la methode "Aligne()"
    /*for (int xbis = 0; xbis < lx; xbis++)
    {
                matrice[xbis][20] = 1;
                matrice[xbis][21] = 1;

    }*/
}

void Game::Recreer(int h, int l)
{
    matrice = new int*[l];
    for (int x = 0; x < l; x++)
    {
        matrice[x] = new int[h];
    }
    for (int y = 0; y < h; y++)
    {
        for(int x = 0; x < l; x++)
        {
            if (mtmp[x][y] == 1)
            {
                matrice[x][y] = 1;
            }
            else
            {
                matrice[x][y] = 0;
            }
        }
    }
}
void Game::Intergpiece(int h, int l)
{
    for (int y = 0; y < h; y++)
    {
        for (int x = 0; x < l; x++)
        {
            if (T1.posx <= x && x < (T1.posx + 4) && T1.posy <= y && y < (T1.posy + 4))
            {
                if(matrice[x][y] == 0)
                    {
                        matrice[x][y] = T1.piece[x-T1.posx][y-T1.posy];
                    }
            }
        }
    }
}
void Game::Rotatepiece(int m, int n)
{
    // Transpose the matrix
    for ( int i = 0; i < m; i++ ) {
        for ( int j = i + 1; j < n; j++ ) {
            int tmp = T1.piece[i][j];
            T1.piece[i][j] = T1.piece[j][i];
            T1.piece[j][i] = tmp;
        }
    }

    // Swap the columns
    for ( int i = 0; i < m; i++ ) {
        for ( int j = 0; j < n/2; j++ ) {
            int tmp = T1.piece[i][j];
            T1.piece[i][j] = T1.piece[i][n-1-j];
            T1.piece[i][n-1-j] = tmp;
        }
    }
    Replacemartice();
    Psize();
}
void Game::Replacemartice()
{
    int** matmp = new int*[5];
    for (int l = 0; l < 5; l++)
    {
        matmp[l] = new int[5];
    }
    for (int h = 0; h < 5; h++)
    {
        for(int l = 0; l < 5; l++)
        {
            matmp[l][h] = 0;
        }
    }
    while (1)
    {
        for (int x = 0; x < 4; x++)
        {
            for (int y = 0; y < 4; y++)
            {
                matmp[x][y] = T1.piece[x][y];
            }
        }
        int subject = 0;
        for (int ytmp = 0; ytmp < 4; ytmp++)
        {
            if (T1.piece[0][ytmp] == 1)
            {
                subject = 1;
            }
        }
        if (subject == 1)
        {
            break;
        }
        else
        {
            for (int xp = 0; xp < 4; xp++)
            {
                for (int yp = 0; yp < 4; yp++)
                {
                    T1.piece[xp][yp] = matmp[xp + 1][yp];
                }
            }
        }
    }
    while (1)
    {
        for (int x = 0; x < 4; x++)
        {
            for (int y = 0; y < 4; y++)
            {
                matmp[x][y] = T1.piece[x][y];
            }
        }
        int subject = 0;
        for (int xtmp = 0; xtmp < 4; xtmp++)
        {
            if (T1.piece[xtmp][0] == 1)
            {
                subject = 1;
            }
        }
        if (subject == 1)
        {
            break;
        }
        else
        {
            for (int xp = 0; xp < 4; xp++)
            {
                for (int yp = 0; yp < 4; yp++)
                {
                    T1.piece[xp][yp] = matmp[xp][yp + 1];
                }
            }
        }
    }

}
bool Game::Testcol(int h, int l, int posx)
{
    Psize();
    if (T1.posy == hy - (T1.hp + 1))
    {
        return true;
    }
    for (int x = 0; x < 4; x++)
    {
        for (int y = 0; y < 4; y++)
        {
            if (T1.piece[x][y] == 1)
            {
                for (int xbis = 0; xbis < l; xbis++)
                {
                    for (int ybis = 0; ybis < h; ybis++)
                    {
                        if (mtmp[xbis][ybis] == 1)
                        {
                            if (x + T1.posx == xbis && y + (T1.posy + 1) == ybis)
                            {
                                return true;
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}
void Game::Aligne()
{

    for (int y = hy; y > -1; y--)
    {
        int subjet = 0;
        for (int x = 0; x < lx; x++)
        {
            if (mtmp[x][y] == 0)
            {
                subjet = 1;
            }
        }
        if (subjet == 0)
        {
            // met les lignes à 0
            for (int xbis = 0; xbis < lx; xbis++)
            {
                mtmp[xbis][y] = 0;

            }
            // fait déscendre les lignes
            for (int ybis = y; ybis > -1; ybis--)
            {
                for (int xbis = 0; xbis < lx; xbis++)
                {
                    if (ybis - 1 > -1)
                    {
                        mtmp[xbis][ybis] = mtmp[xbis][ybis - 1];
                    }
                }
            }
            point += 10;
            if (point < 100)
            {
                lvl = 1;
                timelvl = 1000;
            }
            if (point >= 100 && point <= 200)
            {
                lvl = 2;
                timelvl = 750;
            }
            if (point >= 200 && point <= 300)
            {
                lvl = 3;
                timelvl = 500;
            }
            if(point >= 300 && point <= 500)
            {
                lvl = 4;
                timelvl = 250;
            }
            if (point >= 500)
            {
                lvl = 5;
                timelvl = 100;
            }
            Aligne();
        }
    }

}
void Game::Psize()
{
    int width = 0;
    int height = 0;
    for (int x = 0; x < 4; x++)
    {
        for (int y = 0; y < 4; y++)
        {
            if (T1.piece[x][y] == 1)
            {
                if (x > width)
                {
                    width = x;
                }
                if (y > height)
                {
                    height = y;
                }
            }
        }
    }
    T1.wp = width;
    T1.hp = height;
}
void Game::Affiche(int h, int l)
{
    system("cls");
    for (int x = 0; x < (l + 2); x++)
            {
                if (x == 0 || x == (l + 1))
                {
                    std::cout << "|*|" ;
                }
                else
                {
                    std::cout << "# " ;
                }
            }
    std::cout << std::endl;
    for (int y = 0; y < h; y++)
    {
        std::cout << "|*|";
        for (int x = 0; x < l; x++)
        {

            if (matrice[x][y] == 0)
            {
                std::cout << "  ";
            }
            else if (matrice[x][y] == 1)
            {
                std::cout << "[]";
            }
        }
        std::cout << "|*|";
        if (y == - 6 + h/2)
        {
            std::cout << "  SCORE |" << point;
        }
        if (y == - 4 + h/2)
        {
            std::cout << "        |";
            T2.Affiche(0);
        }
        if (y == - 3 + h/2)
        {
            std::cout << "  NEXT  |";
            T2.Affiche(1);
        }
        if (y == - 2 + h/2)
        {
            std::cout << "        |";
            T2.Affiche(2);
        }
        if (y == - 1 + h/2)
        {
            std::cout << "        |";
            T2.Affiche(3);
        }
        std::cout << std::endl;
    }
    for (int x = 0; x < (l + 2); x++)
            {
                if (x == 0 || x == (l + 1))
                {
                    std::cout << "|*|" ;
                }
                else
                {
                    std::cout << "# " ;
                }
            }
    std::cout << std::endl;
}
