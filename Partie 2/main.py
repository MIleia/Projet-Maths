tablongueur = [10,9,7.5,1,2,11,3,3,3,4,5,6,7,5,6,5,4,7,9,3,5,6,7,3,1,2,4,6,7,9,6,3,3,4,5,6,6,7,6,7,8,8,8,5,2.2,4.2,3.7,5.6,4.9,8.7,6.1,3.3,2.6,2.9,2,3,6,5,4,6,4,2,4,6,6,3,4,4,2,6,2,4,5,5,4,6,3,3,3,5,5,6,5,3,5,6,6,3,5,3,4,3,3,5,3,4,4,2,2,6]
lmax = 11.583
Lmax = 2.294
Hmax = 2.569




tableau = [
    (10, 1, 0.5), (9, 2, 0.7), (7.5, 1.2, 0.4), (1, 1, 1), (2, 2, 1), (11, 1, 0.2),
    (3, 2, 0.6), (3, 1.3, 1.8), (3, 2.1, 0.6), (4, 1, 0.5), (5, 0.8, 1), (6, 1.9, 1),
    (7, 1.6, 1.5), (5, 1.1, 2.3), (6, 2, 1.4), (5, 0.8, 0.8), (4, 1.6, 0.6), (7, 1, 1.3),
    (9, 0.9, 2.2), (3, 1.6, 0.9), (5, 1.1, 2.4), (6, 1.6, 1.4), (7, 0.9, 1.2), (3, 1.6, 1.9),
    (1, 1.8, 1), (2, 1.2, 2.3), (4, 0.7, 1.2), (6, 1.2, 2.5), (7, 0.6, 1.5), (9, 1.7, 1),
    (6, 1.9, 1.6), (3, 2.2, 2.2), (3, 0.5, 2.2), (4, 0.7, 1.9), (5, 2.2, 0.7), (6, 1.3, 2.5),
    (6, 1.3, 1.2), (7, 1.4, 2.5), (6, 1.1, 1), (7, 0.9, 1.3), (8, 0.5, 0.5), (8, 0.9, 1.7),
    (8, 0.9, 1.8), (5, 1.7, 1.2), (2.2, 1.6, 1.1), (4.2, 1.5, 0.8), (3.7, 0.9, 1.4), (5.6, 0.5, 1.4),
    (4.9, 0.9, 2.5), (8.7, 1.3, 1.3), (6.1, 2.2, 2.3), (3.3, 1.8, 2.3), (2.6, 1.6, 2.3), (2.9, 1.6, 2),
    (2, 1.1, 0.6), (3, 0.6, 1.2), (6, 1, 0.8), (5, 1.3, 0.6), (4, 2.1, 2.1), (6, 1.5, 1.9),
    (4, 0.8, 2.1), (2, 2, 2.3), (4, 1, 1.1), (6, 1.8, 1.1), (6, 1.9, 0.9), (3, 2, 2.2),
    (4, 1.5, 0.9), (4, 2.1, 2.5), (2, 1.2, 1.5), (6, 1.3, 2), (2, 0.8, 1.1), (4, 1.4, 2),
    (5, 0.6, 0.5), (5, 0.6, 1.8), (4, 0.7, 1.4), (6, 0.5, 0.7), (3, 1.5, 1.8), (3, 1.4, 2),
    (3, 2, 2.3), (5, 1.5, 0.7), (5, 2.2, 0.5), (6, 1.2, 1.2), (5, 0.8, 0.7), (3, 0.5, 1.9),
    (5, 1.4, 0.7), (6, 0.7, 0.7), (6, 1.2, 2), (3, 1.7, 1.1), (5, 1.6, 2.1), (3, 1.3, 1.7),
    (4, 1.5, 1.7), (3, 1.5, 1.9), (3, 0.6, 1.9), (5, 1.8, 0.5), (3, 1.8, 0.7), (4, 1.7, 1.4),
    (4, 1.5, 0.5), (2, 2.1, 1.8), (2, 0.7, 1.1), (6, 1.2, 1.3)
]


def offlineDim2():
    res=[]
    resulat=[]
    utilise=[0 for y in range(len(tableau))]
    for i in range(len(tableau)):
        rajoute=False
        if utilise[i]==1:
            i+=1
        else:
            maxTempl=[]
            maxTempl.append(tableau[i][0])
            maxTempL=[]
            maxTempL.append(tableau[i][1])
            maxTemp2l=[]
            maxTemp2l.append(tableau[i][0])
            maxTemp2L=[]
            maxTemp2L.append(tableau[i][1])
            utilise[i]=1
            #res.append(tableau[i][0])
            res.append(i+1)
            index=0
            fin=False
            j = 0
            ite=0
            while fin == False:
                if utilise[j] == 1:
                    ite+=1
                elif maxTemp2l+ tableau[j][0] <= lmax and :
                    maxTemp2l = maxTemp2l + tableau[j][0]

                    #res.append(tableau[j][0])

                    utilise[j]=1
                    ite=0
                elif maxTempl + tableau[j][0] <= lmax and maxTempl + tableau[j][0] > maxTemp2l and maxTemp2l + tableau[j][0] <= lmax:
                    if rajoute == False:

                        maxTemp2l = maxTemp2l + tableau[j][0]
                        res.append(tableau[j][0])
                        rajoute = True
                        index = j
                        ite=0
                    else:
                        res.pop()
                        maxTemp2l = maxTemp2l + tableau[j][0]
                        res.append(tableau[j][0])
                        index = j

                        ite=0
                j += 1
                if j==len(tableau):
                    j=0
                if ite==len(tableau):
                    fin=True
            utilise[index]=1
            resulat.append(res.copy())
            res.clear()

    return resulat

#print(offlineDim2())

def offlineDim1():
    res=[]
    resulat=[]
    utilise=[0 for y in range(len(tableau))]
    for i in range(len(tableau)):
        rajoute=False
        if utilise[i]==1:
            i+=1
        else:
            maxTemp=tableau[i][0]
            maxTemp2=tableau[i][0]
            utilise[i]=1
            #res.append(tableau[i][0])
            res.append(i+1)
            index=0

            fin=False
            j = 0
            ite=0
            while fin == False:
                if utilise[j] == 1:
                    ite+=1
                elif maxTemp2+ tableau[j][0] <= lmax:
                    maxTemp2 = maxTemp2 + tableau[j][0]
                    #res.append(tableau[j][0])
                    res.append(j+1)
                    utilise[j]=1
                    ite=0
                elif maxTemp + tableau[j][0] <= lmax and maxTemp + tableau[j][0] > maxTemp2 and maxTemp2 + tableau[j][0] <= lmax:
                    if rajoute == False:
                        maxTemp2 = maxTemp2 + tableau[j][0]
                        #res.append(tableau[j][0])
                        res.append(j+1)
                        rajoute = True
                        index = j
                        ite=0
                    else:
                        res.pop()
                        maxTemp2 = maxTemp2 + tableau[j][0]
                        #res.append(tableau[j][0])
                        res.append(j+1)
                        index = j

                        ite=0
                j += 1
                if j==len(tableau):
                    j=0
                if ite==len(tableau):
                    fin=True
            utilise[index]=1
            resulat.append(res.copy())
            res.clear()

    return resulat

print("offlineDm1 : ",offlineDim1())




def onlineDim1V2():
    conteneur = [tableau[0][0]]
    decalage=0
    for i in range(1,len(tableau)):
        longueur = tableau[i][0]
        if conteneur[i-decalage-1] + longueur <= lmax:
            conteneur[i-decalage-1] += longueur
            decalage+=1
        else :
            conteneur.append(longueur)
    #print("Le nombre de conteneurs est de ", len(conteneur) - 1)
    #print("Les longueurs des conteneurs sont ", conteneur[0:])

    return conteneur





onlineDim1V2()

def onlineDim1():
    conteneur = [0]
    for longueur,L,h in tableau:
        dispo = True
        for j in range(len(conteneur)):
            if dispo:
                if conteneur[j] + longueur <= lmax:
                    conteneur[j] += longueur
                    dispo = False
        if dispo:
            conteneur.append(longueur)

    print("Le nombre de conteneurs est de ",len(conteneur))
    print("Les longueurs des conteneurs sont ",conteneur[0:])
    dim = 0
    for i in range(len(conteneur)):
        dim += lmax - conteneur[i]
    print("La dimension non occupée est de ",round(dim,3),"m")

def onlineDim2():
    conteneur = [(0, 0)]  # Liste de tuples représentant (longueur, largeur)

    # Ajout des objets aux conteneurs
    for longueur, largeur, h in tableau:
        dispo = True
        for i in range(len(conteneur)):
            l, L = conteneur[i]
            if l + longueur <= lmax and L + largeur <= Lmax:
                conteneur[i] = (l + longueur, L + largeur)
                dispo = False
                break
        if dispo:
            conteneur.append((longueur, largeur))

    # Affichage des conteneurs
    print("Conteneurs après ajout des objets :", conteneur)
    print("Nombre de conteneurs utilisés :", len(conteneur))
    dim = 0
    for i in range(len(conteneur)):
        l, L = conteneur[i]
        dim += lmax*Lmax - l*L
    print("La dimension non occupée est de ",round(dim,3), "m²")

def onlineDim3():
    conteneur = [(0, 0, 0)]  # Liste de tuples représentant (longueur, largeur, hauteur)

    # Ajout des objets aux conteneurs
    for longueur, largeur, hauteur in tableau:
        dispo = True
        for i in range(len(conteneur)):
            l, L, H = conteneur[i]
            if l + longueur <= lmax and L + largeur <= Lmax and H + hauteur <= Hmax:
                conteneur[i] = (l + longueur, L + largeur, H + hauteur)
                dispo = False
                break
        if dispo:
            conteneur.append((longueur, largeur, hauteur))

    # Affichage des conteneurs
    print("Conteneurs après ajout des objets :", conteneur)
    print("Nombre de conteneurs utilisés :", len(conteneur))
    dim = 0
    for i in range(len(conteneur)):
        l, L, H = conteneur[i]
        dim += lmax*Lmax*Hmax - l*L*H
    print("La dimension non occupée est de ",round(dim,3), "m³")

#onlineDim1()
#onlineDim2()
#onlineDim3()