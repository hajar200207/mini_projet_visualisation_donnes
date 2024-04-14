import matplotlib.pyplot as plt
# Données
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 10, 12]

plt.bar(categories, values, edgecolor='black', alpha=0.7)
plt.title("Diagramme à Barres Simple")
plt.xlabel("Catégories")
plt.ylabel("Valeurs")
plt.grid(True, axis='y')  # Ajout d'une grille sur l'axe
plt.show()
