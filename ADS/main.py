def main():
    best_subject_test = []
    h = 0
    nstr = input("Enter a number (default = 665) : ")
    if nstr == "":
        nstr = "665"
    n = int(nstr)
    cho = 8
    while(cho >= 5 or cho <= 0):
        cho = int(input("\n\nSelect your methode:\n\n1) GLOUTONNE\n\n2) RECURSIF NAÏF\n\n3) BOTTOM DOWN\n\n4) BOTTOM UP\n\n> "))
        if cho == 1:
            best_subject_test, h = gloutonne(best_subject_test, h, n)
            print("pavé(s) utilisé(s) : ", best_subject_test)
            print("hauteur total de l'empilement : ", h)
        elif cho == 2:
            best_subject_test, h = gloutonne(best_subject_test, h, n)
            h = ret_cure_dent(best_subject_test,n)
            print("hauteur total de l'empilement : ", h)
        elif cho == 3:
            top_less(n)
        elif cho == 4:
            best_subject_test, h = Bottom_Up(best_subject_test, h, n)
            print("pavé(s) utilisé(s) : ", best_subject_test)
            print("hauteur total de l'empilement : ", h)
        else:
            print("Wait. I am earing things. they say monky-monky-graby-appel")

def genlist(n):
    with open("boxes.txt", "r") as f:
        content = []
        tmp = []
        for line in f:
            content.append([int(x) for x in line.split()])
        for i in range(n):
            tmp.append(content[i])
        return tmp

def permutliste(seq):
    lissttmp = []
    add = 0
    for x in seq:
        for y1 in range(3):
            for y2 in range(3):
                if y1 != y2:
                    lissttmp.append([])
                    lissttmp[add].append((x[0] + x[1] + x[2]) - (x[y1] + x[y2]))
                    lissttmp[add].append(x[y1])
                    lissttmp[add].append(x[y2])
                    add += 1
    return lissttmp



def gloutonne(best_subject_test, h, n):
    subject_test_00 = genlist(n)
    subject_test_00 = [[7, 2, 5],[7, 6, 3],[10, 20, 5],[3, 4, 5]]
    subject_test_00 = permutliste(subject_test_00)
    id = 0
    c = 0
    best_s = [100, 100, 100]
    while (subject_test_00 != []):
        for x in subject_test_00:
            if c == 0 or best_s[1] > x[1] and best_s[2] > x[2]:
                id = subject_test_00.index(x)
                best_s[0] = x[0]
                best_s[1] = x[1]
                best_s[2] = x[2]
                best_subject_test.append([])
                best_subject_test[c].append(x[0])
                best_subject_test[c].append(x[1])
                best_subject_test[c].append(x[2])
                h += x[0]
                c += 1
            else:
                id = 0

        del subject_test_00[id]
    return (best_subject_test, h)


def ret_cure_dent(best_subject_test,i):
    if i == 1:
        return best_subject_test[0][0]
    else:
        return ret_cure_dent(best_subject_test,i-1) + best_subject_test[i][0]


def top_less(n):
    print("Holy poopwalawala this is too spooky for me.")

#Bottom Up
def Bottom_Up(best_subject_test, h, n):
    subject_test_00 = genlist(n)
    subject_test_00 = [[7, 2, 5],[7, 6, 3],[10, 20, 5],[3, 4, 5]]
    subject_test_00 = permutliste(subject_test_00)
    id = 0
    c = 0
    print("LOADING: ", end='')
    while(subject_test_00 != []):
        best_s = [100, 100, 100]
        for x in subject_test_00:
            for y1 in range (3):
                for y2 in range (3):
                    if best_s[1] * best_s[2] > x[y1] * x[y2] and y1 != y2 or best_s[1] * best_s[2] == x[y1] * x[y2] and best_s[0] < (x[0] + x[1] + x[2]) - (x[y1] + x[y2]) and y1 != y2:
                        id = subject_test_00.index(x)
                        best_s[0] = (x[0] + x[1] + x[2]) - (x[y1] + x[y2])
                        best_s[1] = x[y1]
                        best_s[2] = x[y2]
        if c == 0 or best_s[1] > best_subject_test[c - 1][1] and best_s[2] > best_subject_test[c - 1][2]:
            best_subject_test.append([])
            best_subject_test[c].append(best_s[0])
            best_subject_test[c].append(best_s[1])
            best_subject_test[c].append(best_s[2])
            h += best_s[0]
            c += 1
            print(" ")
        del subject_test_00[id]

    return (best_subject_test, h)

main()
