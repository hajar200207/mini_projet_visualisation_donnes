import numpy as np
import matplotlib.pyplot as plt

# Générer des données météorologiques hypothétiques pour chaque mois de l'année
mois = np.arange(1, 13)
temperature_max = np.random.randint(0, 30, size=12)
precipitations = np.random.randint(0, 100, size=12)

# Calculer les coordonnées polaires pour la spirale
theta = np.linspace(0, 2*np.pi, 1000)
r = 10 * np.sqrt(theta)  # J'ai ajouté un astérisque (*) pour la multiplication

# Créer la figure et les axes
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Tracer la spirale
ax.plot(theta, r, color='blue')

# Placer les points de données météorologiques sur la spirale
ax.scatter(2*np.pi*(mois-1)/12, temperature_max, color='red', label='Température Max')
ax.scatter(2*np.pi*(mois-1)/12, precipitations, color='green', label='Précipitations')

# Ajouter une légende
ax.legend()

# Afficher le graphique
plt.show()
