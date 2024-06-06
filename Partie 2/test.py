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



def onlineDim2():
    conteneurs = []  # Liste de tuples représentant (longueur occupée, largeur occupée)

    for longueur, largeur, _ in tableau:
        placee = False
        for i in range(len(conteneurs)):
            l, L = conteneurs[i]
            # On regarde si la marchandise entre en largeur
            if L + largeur <= Lmax:
                if l + longueur <= lmax:
                    if longueur <= l:
                        conteneurs[i] = (l, L + largeur)
                        placee = True
                        break
                    else :
                        conteneurs[i] = (longueur, L + largeur)
                        placee = True
                        break
            else :
                if l + longueur <= lmax:
                    if largeur <= L:
                        conteneurs[i] = (l + longueur, largeur)
                        placee = True
                        break

        if placee == False:
            # Si la marchandise ne peut pas être ajoutée à un conteneur existant, on crée un nouveau conteneur
            conteneurs.append((longueur, largeur))

    dim = 0
    for l, L in conteneurs:
        dim += (lmax - l) * (Lmax - L)  # Calcul de la dimension non occupée

    print("Dimension non occupée :", round(dim, 3), "m²")
    return len(conteneurs), conteneurs


# Affichage des résultats
online_result_dim2 = onlineDim2()
print("Online Dimension 2: Nombre de conteneurs = ", online_result_dim2[0])
print("Conteneurs: ", online_result_dim2[1], "\n")






def onlineDim3():
    conteneurs = []  # Liste de tuples représentant (longueur occupée, largeur occupée)

    for longueur, largeur, hauteur in tableau:
        placee = False
        for i in range(len(conteneurs)):
            l, L, h = conteneurs[i]
            # On regarde si la marchandise entre en hauteur
            if h + hauteur <= Hmax:
                # On regarde si la marchandise entre en largeur
                if L + largeur <= Lmax:
                    # On regarde si la marchandise entre en longueur
                    if l + longueur <= lmax:
                        if longueur <= l:
                            conteneurs[i] = (l, L + largeur, h + hauteur)
                            placee = True
                            break
                        else :
                            conteneurs[i] = (longueur, L + largeur, h + hauteur)
                            placee = True
                            break
                else :
                    if l + longueur <= lmax:
                        if largeur <= L:
                            conteneurs[i] = (l + longueur, largeur, h + hauteur)
                            placee = True
                            break
            else :
                if L + largeur <= Lmax:
                    if l + longueur <= lmax:
                        if hauteur <= h:
                            conteneurs[i] = (l, L + largeur, hauteur)
                            placee = True
                            break
                    else :
                        conteneurs[i] = (longueur, L + largeur, hauteur)
                        placee = True
                        break

        if placee == False :
            # Si la marchandise ne peut pas être ajoutée à un conteneur existant, on crée un nouveau conteneur
            conteneurs.append((longueur, largeur, hauteur))

    dim = 0
    for l, L, h in conteneurs:
        dim += (lmax - l) * (Lmax - L) * (Hmax - h)  # Calcul de la dimension non occupée

    print("Dimension non occupée :", round(dim, 3), "m²")
    return len(conteneurs), conteneurs


# Affichage des résultats
online_result_dim3 = onlineDim3()
print("Online Dimension 2: Nombre de conteneurs = ", online_result_dim3[0])
print("Conteneurs: ", online_result_dim3[1], "\n")