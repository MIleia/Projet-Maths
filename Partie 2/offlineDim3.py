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



def offlineDim3(tableau, lmax, Lmax, Hmax):
    # Conversion des dimensions en unités de 0.1 mètre
    nb_cases_l = int(lmax * 10)
    nb_cases_L = int(Lmax * 10)
    nb_cases_H = int(Hmax * 10)

    # Trier les objets par volume décroissant
    tableau.sort(key=lambda x: x[0] * x[1] * x[2], reverse=True)

    # Liste des wagons (chacun représenté par une matrice 3D de cases disponibles)
    wagons = []

    # Initialisation du premier wagon
    espace_disponible = [[[0] * nb_cases_H for _ in range(nb_cases_L)] for _ in range(nb_cases_l)]
    wagons.append(espace_disponible)

    # Traitement des objets
    for i, obj in enumerate(tableau):
        obj_l, obj_L, obj_H = int(obj[0] * 10), int(obj[1] * 10), int(obj[2] * 10)
        placee = False

        # Parcourir tous les wagons pour trouver une place pour l'objet
        for wagon in wagons:
            for l in range(nb_cases_l):
                for L in range(nb_cases_L):
                    for h in range(nb_cases_H):
                        # Vérifier si l'objet peut être placé à la position (l, L, h) dans le wagon
                        if l + obj_l <= nb_cases_l and L + obj_L <= nb_cases_L and h + obj_H <= nb_cases_H:
                            peut_placer = True
                            for i1 in range(obj_l):
                                for j1 in range(obj_L):
                                    for k1 in range(obj_H):
                                        if wagon[l + i1][L + j1][h + k1] != 0:
                                            peut_placer = False
                                            break
                                    if not peut_placer:
                                        break
                                if not peut_placer:
                                    break

                            if peut_placer:
                                # Placer l'objet dans le wagon
                                for i1 in range(obj_l):
                                    for j1 in range(obj_L):
                                        for k1 in range(obj_H):
                                            wagon[l + i1][L + j1][h + k1] = i + 1
                                placee = True
                                break
                    if placee:
                        break
                if placee:
                    break
            if placee:
                break

        # Si l'objet n'a pas été placé, créer un nouveau wagon et y placer l'objet
        if not placee:
            nouveau_wagon = [[[0] * nb_cases_H for _ in range(nb_cases_L)] for _ in range(nb_cases_l)]
            for i1 in range(obj_l):
                for j1 in range(obj_L):
                    for k1 in range(obj_H):
                        nouveau_wagon[i1][j1][k1] = i + 1
            wagons.append(nouveau_wagon)

    # Calcul de la dimension non occupée
    dim = len(wagons) * lmax * Lmax * Hmax
    for obj in tableau:
        dim = dim - obj[0] * obj[1] * obj[2]
    print("Dimension non occupée :", round(dim, 3), "m³")

    return wagons

start = time.time()
wagons = offlineDim3(tableau, lmax, Lmax, Hmax)
end = time.time()
print("Nombre de wagons : ", len(wagons))
print("Temps d'exécution : ", round(end - start, 3), "s")


