def testligne(plateau,joueur,n,p) :
    for ligne in plateau:
        s=0
        for x in ligne:
            if x==joueur:
                s+=1
            elif s<p and x!=joueur:
                s=0
        if s>=p:
            return True
def testcolonne(plateau,joueur,n,p) :
    for j in range(n):
        s=0
        for i in range(n):
            if plateau[i][j]==joueur:
                s+=1
            elif s<p and plateau[i][j]!=joueur:
                s=0
        if s>=p:
            return True
def testdiagonale1(plateau,joueur,n,p):
    for j in range(n):
        s=0
        for i in range(n):
            if plateau[i][i]==joueur:
                s+=1
            elif s<p and plateau[i][i]!=joueur:
                s=0
        if s>=p:
            return True
def testdiagonale2(plateau,joueur,n,p):
    for j in range(n):
        s=0
        for i in range(n):
            if plateau[i][i-1]==joueur:
                s+=1
        if s==p:
            return True
def testdiagonale3(plateau,joueur,n,p):
    for j in range(n):
        s=0
        for i in range(n):
            if plateau[i-1][i]==joueur:
                s+=1
        if s==p:
            return True
def testdiagonale4(plateau,joueur,n,p):
    s=0
    for i in range(n):
        if plateau[i][n-i-1]==joueur:
            s+=1
        elif s<p and plateau[i][n-i-1]!=joueur:
            s=0
    if s>=(n-1):
        return True
def testdiagonale5(plateau,joueur,n,p):
    s=0
    for i in range(n):
        if plateau[i][n-i-2]==joueur:
            s+=1
    if s==(n-1):
        return True
def testdiagonale6(plateau,joueur,n,p):
    s=0
    for i in range((n-1)):
        if plateau[i+1][n-i-1]==joueur:
            s+=1
    if s==p:
        return True
def gagne(plateau,joueur,n,p):
    if testligne(plateau,joueur,n,p) or testcolonne(plateau,joueur,n,p) or testdiagonale1(plateau,joueur,n,p) or testdiagonale2(plateau,joueur,n,p) or testdiagonale3(plateau,joueur,n,p) or testdiagonale4(plateau,joueur,n,p) or testdiagonale5(plateau,joueur,n,p) or testdiagonale6(plateau,joueur,n,p):
        return True
    else:
        return False