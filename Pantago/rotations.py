def RotationGauche(plateau,m):
    plateau2 = [[0] * m for q in range(m)]
    for i in range(0,m):
        for e in range(0,m):
            plateau2[i][e] = plateau[i][e]
    plateau3=plateau
    for l in range(0,m):
        for c in range(0,m):
            plateau3[l][c] = plateau2[c][(m-1)-l]
def RotationDroite(plateau,m):
        plateau3 = plateau
        plateau3 = RotationGauche(plateau,m)
        plateau3 = RotationGauche(plateau,m)
        plateau3 = RotationGauche(plateau,m)
def Rotate_Final(plateau,n,e,c):
    m=n//2
    plateauHF = [[0] * m for q in range(m)]
    if e==1:
        for q in range(0,m):
            for p in range(0,m):
                plateauHF[q][p] = plateau[q][p]
        if c==True:
            RotationDroite(plateauHF,m)
        elif c==False:
            RotationGauche(plateauHF,m)
        for l in range(0,m):
            for a in range (0,m):
                plateau[l][a] = plateauHF[l][a]
    elif e==2:
        for q in range(0,m):
            for p in range(0,m):
                plateauHF[q][p] = plateau[q][p-m]
        if c==True:
            RotationDroite(plateauHF,m)
        elif c==False:
            RotationGauche(plateauHF,m)
        for l in range(0,m):
            for a in range (0,m):
                plateau[l][a-m] = plateauHF[l][a]
    elif e==3:
        for q in range(0,m):
            for p in range(0,m):
                plateauHF[q][p] = plateau[q-m][p]
        if c==True:
            RotationDroite(plateauHF,m)
        elif c==False:
            RotationGauche(plateauHF,m)
        for l in range(0,m):
            for a in range (0,m):
                plateau[l-m][a] = plateauHF[l][a]
    elif e==4:
        for q in range(0,m):
            for p in range(0,m):
                plateauHF[q][p] = plateau[q-m][p-m]
        if c==True:
            RotationDroite(plateauHF,m)
        elif c==False:
            RotationGauche(plateauHF,m)
        for l in range(0,m):
            for a in range (0,m):
                plateau[l-m][a-m] = plateauHF[l][a]