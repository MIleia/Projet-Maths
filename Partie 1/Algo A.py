

def exact(objects, capacity):
    n = len(objects)
    # Initialiser la matrice de programmation dynamique
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Remplir la matrice
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if objects[i - 1][1] * 100 <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - int(objects[i - 1][1] * 100)] + objects[i - 1][2])
            else:
                dp[i][w] = dp[i - 1][w]

    # Retrouver les objets sélectionnés
    selected_objects = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_objects.append(objects[i - 1])
            w -= int(objects[i - 1][1] * 100)
        i -= 1

    return selected_objects, dp[n][capacity]

# Appel de la fonction exact avec les objets et la capacité maximale
selected_objects, total_utility = exact(objects, int(0.6 * 100))

# Affichage des objets sélectionnés et l'utilité totale
print("Objets sélectionnés :")
for obj in selected_objects:
    print(obj[0])
print("Utilité totale :", total_utility)



# Définition des objets
objets = [
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


def exact(objects, capacity):
    n = len(objects)
    # Initialiser la matrice de programmation dynamique
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Remplir la matrice
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if objects[i - 1][1] * 100 <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - int(objects[i - 1][1] * 100)] + objects[i - 1][2])
            else:
                dp[i][w] = dp[i - 1][w]

    # Retrouver les objets sélectionnés
    selected_objects = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_objects.append(objects[i - 1])
            w -= int(objects[i - 1][1] * 100)
        i -= 1

    return selected_objects, dp[n][capacity]

# Appel de la fonction exact avec les objets et la capacité maximale
selected_objects, total_utility = exact(objects, int(0.6 * 100))

# Affichage des objets sélectionnés et l'utilité totale
print("Objets sélectionnés :")
for obj in selected_objects:
    print(obj[0])
print("Utilité totale :", total_utility)


