#ifndef GAME_H
#define GAME_H

class Game
{
    public:
        Game(int h,int l);
        void Rotatepiece(int m,int n);
        void Replacemartice();
        int** matrice;
        int** mtmp;
        void Aligne();
        int point = 0;
        int lvl = 0;
        int hy;
        int lx;
        void Psize();
        int timelvl = 1000;
        bool Testcol(int h, int l, int posx);
        void Time();
        long ElapsedTime(long begTime);
        void Testevent();
        void Ruels();
        void Event();
        void Intergpiece(int h, int l);
        void Creer(int h,int l,int** m);
        void Recreer(int h,int l);
        void Affiche(int h,int l);
};

#endif // GAME_H

