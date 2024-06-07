import time


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



def onlineDim2(tableau, lmax, Lmax):
    # Conversion des dimensions en unités de 0.1 mètre
    nb_cases_l = int(lmax * 10)
    nb_cases_L = int(Lmax * 10)

    # Liste des wagons (chacun représenté par une matrice 2D de cases disponibles)
    wagons = []

    # Initialisation du premier wagon
    espace_disponible = [[0] * nb_cases_L for _ in range(nb_cases_l)]
    wagons.append(espace_disponible)

    # Traitement des objets, i est l'indice de l'objet, obj est l'objet
    for i, obj in enumerate(tableau):
        obj_l, obj_L = int(obj[0] * 10), int(obj[1] * 10)
        placee = False

        # Parcours de tous les wagons pour trouver une place pour l'objet
        for wagon in wagons:
            # Parcouris de toutes les cases du wagon en longueur
            for l in range(nb_cases_l):
                # Parcours de toutes les cases du wagon en largeur
                for L in range(nb_cases_L):
                    # Vérifier si l'objet peut être placé à la position (l, L) dans le wagon
                    if l + obj_l <= nb_cases_l and L + obj_L <= nb_cases_L:
                        # L'objet peut être placé si toutes les cases qu'il occupe sont disponibles
                        # la variable peut_placer passe donc à True si l'objet peut être placé
                        peut_placer = True
                        # Parcours de toutes les cases occupées par l'objet
                        # Parcours en longueur
                        for i1 in range(obj_l):
                            # Parcours en largeur
                            for j1 in range(obj_L):
                                # Verifier si la case est disponible
                                if wagon[l + i1][L + j1] != 0:
                                    # Si la case est occupée, la variable peut_placer passe à False
                                    peut_placer = False
                                    break
                            if peut_placer == False:
                                break
                        # Si l'objet peut être placé, on le placer dans le wagon
                        if peut_placer:
                            # Placement de l'objet dans le wagon
                            for i1 in range(obj_l):
                                # Mise à jour des cases du wagon en y mettant l'inidice de l'objet placé
                                for j1 in range(obj_L):
                                    wagon[l + i1][L + j1] = i
                            # L'objet a été placé (placee passe à True)
                            placee = True
                            break
                if placee == True:
                    break
            if placee == True:
                break

        # Si l'objet n'a pas été placé, création un nouveau wagon et y placer l'objet
        if placee == False :
            # Création d'un nouveau wagon
            nouveau_wagon = [[0] * nb_cases_L for _ in range(nb_cases_l)]
            # Mise à jour des cases du wagon en y mettant l'inidice de l'objet placé
            for i1 in range(obj_l):
                for j1 in range(obj_L):
                    nouveau_wagon[i1][j1] = i
            # Ajout du nouveau wagon à la liste des wagons
            wagons.append(nouveau_wagon)

    # Calcul de la dimension non occupée
    dim = len(wagons) * lmax * Lmax
    for obj in tableau :
        dim = dim - obj[0] * obj[1]
    print("Dimension non occupée :", round(dim, 3), "m²")

    return wagons


start = time.time()
wagons = onlineDim2(tableau, lmax, Lmax)
end = time.time()
print("Nombre de wagons : ", len(wagons))
print("Temps d'exécution : ", round(end - start, 3), "s")


