#ifndef TERIMINOS_H
#define TERIMINOS_H


class Teriminos
{
    public:
        Teriminos(int x,int y,int index);
        int** piece;
        int posx;
        int posy;
        int hp = 0;
        int wp = 0;
        void Creer(int index);
        void Affiche(int yp);
};

#endif // GAME_H

