import time

#initialisation des dimensions max
lmax = 11.583
Lmax = 2.294
Hmax = 2.569
#dimension de chaque objet: longueur, largeur, hauteur
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



def onlineDim1():
    conteneurs = []
    #prend la longueur de l'objet à chaque itération
    for longueur, _, _ in tableau:
        ajoute = False
        #parcourt tous les wagons déjà créés
        for i in range(len(conteneurs)):
            #Si le wagon a de la place pour l'objet alors on l'ajoute
            if conteneurs[i] + longueur <= lmax:
                conteneurs[i] += longueur
                ajoute = True
                #une fois ajouté, plus besoin d'être dans la boucle
                break
        #Si l'objet est toujours disponible alos on crée un nouveau wagon
        if ajoute == False:
            conteneurs.append(longueur)

    dim = 0
    #on calcule la dimension non occupée en arrondissant au millième
    for i in range(len(conteneurs)):
        dim += lmax - conteneurs[i]
    print("Dimension non occupée :", round(dim, 3), "m")

    return len(conteneurs), conteneurs


