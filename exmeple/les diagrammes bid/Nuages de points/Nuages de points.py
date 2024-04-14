import matplotlib.pyplot as plt

# Données
x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 18, 20]

# Création du nuage de points
plt.scatter(x, y, color='blue', marker='o', label='Points')

# Ajout de labels et titre
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Nuage de Points')

# Affichage de la légende
plt.legend()

# Affichage du graphique
plt.show()
