import time
lmax = 11.583
Lmax = 2.294
Hmax = 2.569



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
    print("Le nombre de wagons utilisé est ",len(resulat))
    end = time.time()
    print(round(end-start,3),'secondes')#on affiche le temps utilisé pour la fonction
    return resulat

