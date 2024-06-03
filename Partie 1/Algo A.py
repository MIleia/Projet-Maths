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


def exact(objects, capacite):
    n = len(objects)
    meilleure_utilite = 0
    meilleurs_objects = []

    # Convertir la capacité et les poids en entiers pour éviter les problèmes de précision des flottants
    capacite = capacite * 100

    # Parcours de toutes les combinaisons possibles
    for i in range(2**n):
        utilite = 0
        poids = 0
        objects_selectiones = []
        for j in range(n):
            if i & (1 << j):
                poids += objects[j][1] * 100
                utilite += objects[j][2]
                objects_selectiones.append(objects[j])

        # Comparaison entre la solution actuelle et la meilleure solution trouvée
        if poids <= capacite and utilite > meilleure_utilite:
            meilleure_utilite = utilite
            meilleurs_objects = objects_selectiones

    return meilleurs_objects, meilleure_utilite



# Appel de la fonction exact
selected_objects, total_utility = exact(objects, 0.6)

# Affichage des objets sélectionnés ainsi que l'utilité totale
print("Objets sélectionnés :")
for obj in selected_objects:
    print(obj[0])
print("Utilité totale :", total_utility)

