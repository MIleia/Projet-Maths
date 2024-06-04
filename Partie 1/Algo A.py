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


def exact_recursive(objects, capacite, index=0, current_subset=[], current_poids=0, current_utilite=0):
    global meilleure_utilite, meilleurs_objects

    if index == len(objects):
        if current_poids <= capacite and current_utilite > meilleure_utilite:
            meilleure_utilite = current_utilite
            meilleurs_objects = current_subset.copy()
        return

    # Inclure l'objet à l'index actuel
    next_poids = current_poids + int(objects[index][1] * 100)
    next_utilite = current_utilite + objects[index][2]

    if next_poids <= capacite:
        exact_recursive(objects, capacite, index + 1, current_subset + [objects[index]], next_poids, next_utilite)

    # Ne pas inclure l'objet à l'index actuel
    exact_recursive(objects, capacite, index + 1, current_subset, current_poids, current_utilite)


def exact(objects, capacite):
    global meilleure_utilite, meilleurs_objects
    meilleure_utilite = 0
    meilleurs_objects = []
    capacite = int(capacite * 100)  # Convertir la capacité en centièmes pour éviter les problèmes de flottants

    start = time.time()
    exact_recursive(objects, capacite)
    end = time.time()

    print("Temps : ", end - start)
    masse_restante = capacite - sum(objet[1] * 100 for objet in meilleurs_objects)
    masse_restante /= 100  # Convertir la masse restante en unités d'origine

    return meilleurs_objects, meilleure_utilite, masse_restante


# Appel de la fonction exact
selected_objects, total_utility, masse = exact(objects, 0.8)

# Affichage des objets sélectionnés ainsi que l'utilité totale et la masse restante
print("Objets sélectionnés :")
for obj in selected_objects:
    print(obj[0])
print("Utilité totale :", total_utility)
print("Masse restante :", masse)


