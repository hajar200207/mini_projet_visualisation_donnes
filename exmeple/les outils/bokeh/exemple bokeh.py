from bokeh.plotting import figure, show;import numpy as np;import time
from bokeh.models import ColumnDataSource, Title;from bokeh.io import push_notebook
# Couleurs disponibles
colors = ['red', 'green', 'green', 'orange', 'purple']
# Créer une source de données pour le cercle (initialement au point (0, 0))
source = ColumnDataSource(data=dict(x=[0], y=[0], color=[colors[0]]))  # Couleur initiale
# Créer une figure
p = figure(x_range=(-10, 10), y_range=(-10, 10))
circle = p.scatter(x='x', y='y', size=20, fill_color='color', source=source)
# Ajouter une légende à la figure
p.add_layout(Title(text="Animation de déplacement avec changement de couleur"), "above")
# Afficher la figure
show(p, notebook_handle=True)
# Fonction pour mettre à jour les données du cercle
def update_circle():
    # Générer de nouvelles données
    new_x = source.data['x'][-1] + np.random.choice([-1, 0, 1])
    new_y = source.data['y'][-1] + np.random.choice([-1, 0, 1])
    new_color = np.random.choice(colors)  # Choisir une couleur aléatoire parmi la liste
    # Mettre à jour les données du cercle
    source.stream({'x': [new_x], 'y': [new_y], 'color': [new_color]})
 # Fonction d'animation
def animate():
    while True:
        update_circle()
        push_notebook(handle=circle.data_source)  # Mettre à jour uniquement le cercle
        time.sleep(0.5)  # Pause pour ralentir l'animation
# Lancer l'animation
animate()
