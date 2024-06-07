# importer la fonction onlineDim1 du fichier onlineDim1.py
from onlineDim1 import onlineDim1
from offlineDim1 import offlineDim1
from onlineDim2 import onlineDim2
from offlineDim2 import offlineDim2
from onlineDim3 import onlineDim3
from offlineDim3 import offlineDim3

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


# Appel de la fonction onlineDim1
print("\n\n----- onlineDim1 -----\n")
start = time.time()
wagons = onlineDim1()
end = time.time()
print("Conteneurs : ", wagons[1], "\n")
print("Nombre de wagons : ", wagons[0])
print("Temps d'exécution : ", round(end - start, 3), "s")


# Appel de la fonction offlineDim1
print("\n\n----- offlineDim1 -----\n")
print("offlineDm1 : ",offlineDim1())


# Appel de la fonction onlineDim2
print("\n\n----- onlineDim2 -----\n")
start = time.time()
wagons = onlineDim2(tableau, lmax, Lmax)
end = time.time()
print("Nombre de wagons : ", len(wagons))
print("Temps d'exécution : ", round(end - start, 3), "s")


# Appel de la fonction offlineDim2
print("\n\n----- offlineDim2 -----\n")
print(offlineDim2())


# Appel de la fonction onlineDim3
print("\n\n----- onlineDim3 -----\n")
start = time.time()
wagons = onlineDim3(tableau, lmax, Lmax, Hmax)
end = time.time()
print("Nombre de wagons : ", len(wagons))
print("Temps d'exécution : ", round(end - start, 3), "s")


# Appel de la fonction offlineDim3
print("\n\n----- offlineDim3 -----\n")
start = time.time()
wagons = offlineDim3(tableau, lmax, Lmax, Hmax)
end = time.time()
print("Nombre de wagons : ", len(wagons))
print("Temps d'exécution : ", round(end - start, 3), "s")