import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Création de données fictives
np.random.seed(42)
data = {
    'x_column': np.random.normal(0, 1, 100),
    'y_column': np.random.normal(1, 2, 100),
    'z_column': np.random.normal(-1, 1.5, 100),
    'w_column': np.random.normal(2, 1, 100)
}
df = pd.DataFrame(data)
# Utilisation de seaborn pour créer un scatterplot
sns.scatterplot(x='x_column', y='y_column', data=df)
plt.xlabel('Axe X')  # Ajouter un label pour l'axe X
plt.ylabel('Axe Y')  # Ajouter un label pour l'axe Y
plt.title('Scatterplot de x_column vs y_column')  # Ajouter un titre
plt.show()
