import matplotlib.pyplot as plt
# Données
sizes = [20, 30, 25, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # Eclatement de la première part
# Création du diagramme circulaire
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%',shadow=True, startangle=90)
# Assurer que le diagramme est un cercle
plt.axis('equal')
# Ajouter un titre
plt.title("Diagramme Circulaire")
# Afficher le diagramme
plt.show()
