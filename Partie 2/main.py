tablongueur = [10,9,7.5,1,2,11,3,3,3,4,5,6,7,5,6,5,4,7,9,3,5,6,7,3,1,2,4,6,7,9,6,3,3,4,5,6,6,7,6,7,8,8,8,5,2.2,4.2,3.7,5.6,4.9,8.7,6.1,3.3,2.6,2.9,2,3,6,5,4,6,4,2,4,6,6,3,4,4,2,6,2,4,5,5,4,6,3,3,3,5,5,6,5,3,5,6,6,3,5,3,4,3,3,5,3,4,4,2,2,6]
lmax = 11.583
Lmax = 2.294
Hmax = 2.569
import time



tableau = [
    [10, 1, 0.5, 1], [9, 2, 0.7, 2], [7.5, 1.2, 0.4, 3], [1, 1, 1, 4], [2, 2, 1, 5], [11, 1, 0.2, 6],
    [3, 2, 0.6, 7], [3, 1.3, 1.8, 8], [3, 2.1, 0.6, 9], [4, 1, 0.5, 10], [5, 0.8, 1, 11], [6, 1.9, 1, 12],
    [7, 1.6, 1.5, 13], [5, 1.1, 2.3, 14], [6, 2, 1.4, 15], [5, 0.8, 0.8, 16], [4, 1.6, 0.6, 17], [7, 1, 1.3, 18],
    [9, 0.9, 2.2, 19], [3, 1.6, 0.9, 20], [5, 1.1, 2.4, 21], [6, 1.6, 1.4, 22], [7, 0.9, 1.2, 23], [3, 1.6, 1.9, 24],
    [1, 1.8, 1, 25], [2, 1.2, 2.3, 26], [4, 0.7, 1.2, 27], [6, 1.2, 2.5, 28], [7, 0.6, 1.5, 29], [9, 1.7, 1, 30],
    [6, 1.9, 1.6, 31], [3, 2.2, 2.2, 32], [3, 0.5, 2.2, 33], [4, 0.7, 1.9, 34], [5, 2.2, 0.7, 35], [6, 1.3, 2.5, 36],
    [6, 1.3, 1.2, 37], [7, 1.4, 2.5, 38], [6, 1.1, 1, 39], [7, 0.9, 1.3, 40], [8, 0.5, 0.5, 41], [8, 0.9, 1.7, 42],
    [8, 0.9, 1.8, 43], [5, 1.7, 1.2, 44], [2.2, 1.6, 1.1, 45], [4.2, 1.5, 0.8, 46], [3.7, 0.9, 1.4, 47], [5.6, 0.5, 1.4, 48],
    [4.9, 0.9, 2.5, 49], [8.7, 1.3, 1.3, 50], [6.1, 2.2, 2.3, 51], [3.3, 1.8, 2.3, 52], [2.6, 1.6, 2.3, 53], [2.9, 1.6, 2, 54],
    [2, 1.1, 0.6, 55], [3, 0.6, 1.2, 56], [6, 1, 0.8, 57], [5, 1.3, 0.6, 58], [4, 2.1, 2.1, 59], [6, 1.5, 1.9, 60],
    [4, 0.8, 2.1, 61], [2, 2, 2.3, 62], [4, 1, 1.1, 63], [6, 1.8, 1.1, 64], [6, 1.9, 0.9, 65], [3, 2, 2.2, 66],
    [4, 1.5, 0.9, 67], [4, 2.1, 2.5, 68], [2, 1.2, 1.5, 69], [6, 1.3, 2, 70], [2, 0.8, 1.1, 71], [4, 1.4, 2, 72],
    [5, 0.6, 0.5, 73], [5, 0.6, 1.8, 74], [4, 0.7, 1.4, 75], [6, 0.5, 0.7, 76], [3, 1.5, 1.8, 77], [3, 1.4, 2, 78],
    [3, 2, 2.3, 79], [5, 1.5, 0.7, 80], [5, 2.2, 0.5, 81], [6, 1.2, 1.2, 82], [5, 0.8, 0.7, 83], [3, 0.5, 1.9, 84],
    [5, 1.4, 0.7, 85], [6, 0.7, 0.7, 86], [6, 1.2, 2, 87], [3, 1.7, 1.1, 88], [5, 1.6, 2.1, 89], [3, 1.3, 1.7, 90],
    [4, 1.5, 1.7, 91], [3, 1.5, 1.9, 92], [3, 0.6, 1.9, 93], [5, 1.8, 0.5, 94], [3, 1.8, 0.7, 95], [4, 1.7, 1.4, 96],
    [4, 1.5, 0.5, 97], [2, 2.1, 1.8, 98], [2, 0.7, 1.1, 99], [6, 1.2, 1.3, 100]
]   #contient toutes les données importantes de chaque objet dans le format suivant : [longueur, largeur, hauteur, numero]

def offlineDim2():
    start = time.time()
    res=[]
    resulat=[]
    utilise=[0 for y in range(len(tableau))]#on créer un tableau de la taille de tableau rempli de 0 pour vérifier si l'objet est déja placé ou non
    temp=()
    temp=tableau.copy()
    dim=0
    for i in range(len(temp)):#ici on ajoute une colonne a notre tableau temp créer juste avant ou l'on stock la surface occupé par l'objet en position 4
        temp[i].append(round(temp[i][0]*temp[i][1],3))
    temp.sort(key=lambda x: x[-1], reverse=True)#on trie temp par la suface dans l'ordre décroissant

    for i in range(len(temp)):#on va parcourir temp
        if utilise[i]==1:#on vérfie si l'objet est déja placé, si c'est le cas, on passe à l'objet suivant
            i+=1
        else:
            maxTempl=[]
            maxTempl.append(temp[i][0])#on place le premier objet de l'itération dans notre wagon
            maxTempL=[]
            maxTempL.append(temp[i][1])#on place le premier objet de l'itération dans notre wagon
            Ltot=sum(maxTempL)
            utilise[i]=1#on marque l'objet comme placé
            res.append(temp[i][3])#on ajoute l'objet a notre liste de résultat temporaire
            dim+=temp[i][0]*temp[i][1]
            for j in range(i,len(temp)):#on va parcourir la liste temp à partir de l'objet suivant celui que l'on vient de placer jusqu'a la fin
                if utilise[j]==1:#on verifie que cet objet n'est pas placé
                    j+=1
                else:
                    for k in range(len(maxTempl)):#on va parcourir l'ensemble des objet déja placé dans le wagon
                        if maxTempl[k]+temp[j][0] <= lmax and maxTempL[k] >= temp[j][1]:#si l'objet rentre dans le wagon, dans la meme longueur qu'un objet déja placé
                            maxTempl[k] = maxTempl[k] + temp[j][0]#on modifie la longueur utilisé
                            maxTempL[k]=max(maxTempL[k], temp[j][1])#ne sert pas mais peut servir si on veut optimiser le code
                            Ltot = sum(maxTempL)
                            res.append(temp[j][3])#on ajoute l'objet a notre liste de résultat temporaire
                            utilise[j] = 1
                            dim+=temp[j][0]*temp[j][1]
                        elif temp[j][1]+Ltot<=Lmax:#si l'objet rentre dans le wagon, sur une nouvelle largeur, sur une nouvelle longueur
                            maxTempl.append(temp[j][0])#on créer la nouvelle longueur et on rentre sa longueur
                            maxTempL.append(temp[j][1])#on rajoute dans le nouvelle longueur et on rentre sa largeur
                            Ltot = sum(maxTempL)#on met a jour la largeur total des objet dans le wagon
                            res.append(temp[j][3])#on ajoute l'objet a notre liste de résultat temporaire
                            utilise[j] = 1
                            dim+=temp[j][0]*temp[j][1]#on calcul la nouvelle surface utilisé

        if len(res)>0:#on met notre résultat temporaire dans notre résultat final si ce dernier n'est pas vide
            resulat.append(res.copy())
            res.clear()
    print("La dimension non occupée est de ",round((len(resulat)*(lmax*Lmax))-dim,3),"m²")#on affiche la dimension non occupé
    end = time.time()
    print(round(end-start,3),'secondes')#on affiche le temps utilisé pour la fonction
    return resulat#on renvoie le résultat

print(offlineDim2())
print(len(offlineDim2()))





def offlineDim1():
    start = time.time()#on prend le temps de départ
    res=[]
    resulat=[]
    utilise=[0 for y in range(len(tableau))]#on créer un tableau de la taille de tableau rempli de 0 pour vérifier si l'objet est déja placé ou non
    dim=0
    dernier=0
    for i in range(len(tableau)):#on va parcourir l'ensemble des objets de notre tableau
        rajoute=False
        if utilise[i]==1:#si l'objet est déja placé, on passe à l'objet suivant
            i+=1
        else:
            maxTemp=tableau[i][0]#on rentre le premier objet dans le wagon, on stock sa longueur
            maxTemp2=tableau[i][0]
            utilise[i]=1#on marque l'objet comme placé
            res.append(i+1)#on met l'objet dans notre liste de résultat temporaire
            index=0
            fin=False
            j = 0
            ite=0
            dim+=tableau[i][0]
            while fin == False:#va nous permettre de parcourir l'ensemble des objets et de faire plusieurs fois le tours si besoin
                if utilise[j] == 1:#si l'objet est déja placé, on passe à l'objet suivant
                    ite+=1
                elif maxTemp2+ tableau[j][0] <= lmax:#si l'objet peut renter directement dans le wagon, on le met dedans
                    maxTemp2 = maxTemp2 + tableau[j][0]
                    #res.append(tableau[j][0])
                    res.append(j+1)
                    utilise[j]=1
                    ite=0
                    dim+=tableau[j][0]
                    dernier=tableau[j][0]
                elif maxTemp + tableau[j][0] <= lmax and maxTemp + tableau[j][0] > maxTemp2 and maxTemp2 + tableau[j][0] <= lmax:
                    #on vérifie si mettre cet objet est plus avantageux que l'objet mis en dernier dans le wagon
                    if rajoute == False:#si cet le second objet que l'on met dans le wagon, on le met juste
                        maxTemp2 = maxTemp2 + tableau[j][0]
                        res.append(j+1)#on ajoute le numero de l'objet dans notre liste de résultat temporaire
                        rajoute = True#on précise que maintenant on n'est plus au deuxieme objet rajouté
                        index = j
                        ite=0#remet le compteur d'itération à 0
                        dim+=tableau[j][0]#on met à jour la surface utilisé
                        dernier=tableau[j][0]#on met à jour le dernier objet mis dans le wagon
                    else:#sinon on retire le dernier objet mis dans le wagon et on met celui ci à la place
                        dim=dim-dernier#on retire la surface de l'objet mis en dernier
                        res.pop()#on retire le dernier objet mis dans le résultat temporaire
                        maxTemp2 = maxTemp2 + tableau[j][0]
                        res.append(j+1)#on met le nouvel objet dans le wagon
                        index = j
                        dim+=tableau[j][0]
                        ite=0
                j += 1
                if j==len(tableau):#on remet j à 0 si il dépasse la taille de tableau
                    j=0
                if ite==len(tableau):#si on a fait un tour complet de tableau sans rien rajouter on stop
                    fin=True
            utilise[index]=1#on marque le dernier objet ajouté comme placé
            resulat.append(res.copy())#on copie notre liste de résultat temporaire dans notre résultat final
            res.clear()#on supprime notre liste de résultat temporaire

    print("La dimension non occupée est de ",round((lmax*len(resulat))-dim,3),"m")#on affiche notre dimension non occupée
    end = time.time()
    print(round(end-start,3),'secondes')#on affiche le temps utilisé pour la fonction
    return resulat

print("offlineDm1 : ",offlineDim1())
print(len(offlineDim1()))




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