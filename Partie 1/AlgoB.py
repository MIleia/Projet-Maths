import time

# Définition des objets
objects = [
    ("Pompe", 0.2, 1.5),
    ("Démonte-pneus", 0.1, 1.5),
    ("Gourde", 1.0, 2),
    ("Chambre à air", 0.2, 0.5),
    ("Clé de 15", 0.3, 1.0),
    ("Multi-tool", 0.2, 1.7),
    ("Pince multiprise", 0.4, 0.8),
    ("Couteau suisse", 0.2, 1.5),
    ("Compresses", 0.1, 0.4),
    ("Désinfectant", 0.2, 0.6),
    ("Veste de pluie", 0.4, 1.0),
    ("Pantalon de pluie", 0.4, 0.75),
    ("Crème solaire", 0.4, 1.75),
    ("Carte IGN", 0.1, 0.2),
    ("Batterie Portable", 0.5, 0.4),
    ("Téléphone mobile", 0.4, 2.0),
    ("Lampes", 0.3, 1.8),
    ("Arrache Manivelle", 0.4, 0.0),
    ("Bouchon valve chromé bleu", 0.01, 0.1),
    ("Maillon rapide", 0.05, 1.4),
    ("Barre de céréales", 0.4, 0.8),
    ("Fruits", 0.6, 1.3),
    ("Rustines", 0.05, 1.5)
]


def algoB(objects, capacite):
    start = time.time()
    n = len(objects)

    utilPoids=[]
    i=0
    for i in range(len(objects)):
        utilPoids.append(objects[i][2] / objects[i][1])

    poids=0
    utilite=0
    sacFinal=[]
    i=0
    nbrObjets=0
    while (poids<capacite) and (nbrObjets<n):
        maxUtilPoids=0
        for i in range(n-nbrObjets):
            if utilPoids[i]>maxUtilPoids:
                maxUtilPoids=utilPoids[i]
                maxIndex=i
        if poids+objects[maxIndex][1]>capacite:
            objects.pop(maxIndex)
            utilPoids.pop(maxIndex)
            i = 0
            nbrObjets += 1
        else:
            sacFinal.append(objects[maxIndex])
            poids+=objects[maxIndex][1]
            utilite+=objects[maxIndex][2]
            objects.pop(maxIndex)
            utilPoids.pop(maxIndex)
            i=0
            nbrObjets+=1


    utiliteTot = 0
    poidsTot = 0
    for i in range(len(sacFinal)):
        utiliteTot = sacFinal[i][2] + utiliteTot
        poidsTot = sacFinal[i][1] + poidsTot
        print(sacFinal[i][0])
    print("Utilité totale : ", round(utiliteTot, 2))
    print("Poids total : ", round(poidsTot, 2))
    end = time.time()
    print("Temps d'exécution : ", end - start)
    return sacFinal



algoB(objects, 2)






