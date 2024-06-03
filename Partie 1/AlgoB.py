import time

# Définition des objets
objects = [
    ("Rustines", 0.05, 1.5),
    ("Maillon rapide", 0.05, 1.4),
    ("Démonte-pneus", 0.1, 1.5),
    ("Bouchon valve chromé bleu", 0.01, 0.1),
    ("Multi-tool", 0.2, 1.7),
    ("Pompe", 0.2, 1.5),
    ("Couteau suisse", 0.2, 1.5),
    ("Lampes", 0.3, 1.8),
    ("Téléphone mobile", 0.4, 2),
    ("Crème solaire", 0.4, 1.75),
    ("Compresses", 0.1, 0.4),
    ("Clé de 15", 0.3, 1),
    ("Désinfectant", 0.2, 0.6),
    ("Chambre à air", 0.2, 0.5),
    ("Veste de pluie", 0.4, 1),
    ("Fruits", 0.6, 1.3),
    ("Gourde", 1, 2),
    ("Pince multiprise", 0.4, 0.8),
    ("Carte IGN", 0.1, 0.2),
    ("Barre de céréales", 0.4, 0.8),
    ("Pantalon de pluie", 0.4, 0.75),
    ("Batterie Portable", 0.5, 0.4),
    ("Arrache Manivelle", 0.4, 0)
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

    end = time.time()
    print("Temps d'exécution : ", end-start)

    return sacFinal




temp=algoB(objects, 0.6)
utiliteTot=0
poidsTot=0
for i in range (len(temp)):
    utiliteTot=temp[i][2]+utiliteTot
    poidsTot=temp[i][1]+poidsTot
    print(temp[i][0])

print("Utilité totale : ", utiliteTot)
print("Poids total : ", round(poidsTot,2))



