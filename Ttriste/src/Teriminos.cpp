#include <iostream>
#include "Game.h"
#include "Teriminos.h"

Teriminos::Teriminos(int x, int y, int index)
{
    posx = x;
    posy = y;
    Creer(index);
    //Affiche();
}
void Teriminos::Creer(int index)
{
    piece = new int*[4];
    for (int xp = 0; xp < 4; xp++)
    {
        piece[xp] = new int[4];
    }

    for (int xp = 0; xp < 4; xp++)
    {
        for(int yp = 0; yp < 4; yp++)
        {
            piece[xp][yp] = 0;
        }
    }
    if (index == 0)
    {
     piece[0][0] = 1;
     piece[0][1] = 1;
     piece[0][2] = 1;
     piece[0][3] = 1;
    }
    else if (index == 1)
    {
     piece[0][0] = 1;
     piece[0][1] = 1;
     piece[0][2] = 1;
     piece[1][1] = 1;
    }
    else if (index == 2)
    {
     piece[0][0] = 1;
     piece[0][1] = 1;
     piece[0][2] = 1;
     piece[1][2] = 1;
    }
    else if (index == 3)
    {
     piece[1][0] = 1;
     piece[0][1] = 1;
     piece[0][2] = 1;
     piece[1][1] = 1;
    }
    else if (index == 4)
    {
     piece[0][0] = 1;
     piece[0][1] = 1;
     piece[0][2] = 1;
     piece[1][0] = 1;
    }
    else if (index == 5)
    {
     piece[0][0] = 1;
     piece[0][1] = 1;
     piece[1][2] = 1;
     piece[1][1] = 1;
    }
    else if (index == 6)
    {
     piece[0][0] = 1;
     piece[0][1] = 1;
     piece[1][0] = 1;
     piece[1][1] = 1;
    }
}
void Teriminos::Affiche(int yp)
{
    for (int xp = 0; xp < 4; xp++)
    {
        if (Teriminos::piece[xp][yp] == 0)
        {
            std::cout << "  ";
        }
        else if (Teriminos::piece[xp][yp] == 1)
        {
            std::cout << "[]";
        }
    }
}
