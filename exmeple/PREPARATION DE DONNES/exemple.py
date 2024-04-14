# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#collection
# Génération de données fictives pour les ventes
np.random.seed(0)
mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
produits = ['Produit A', 'Produit B', 'Produit C']
ventes = pd.DataFrame({
    'Mois': np.random.choice(mois, 100),
    'Produit': np.random.choice(produits, 100),
    'Quantité': np.random.randint(10, 100, 100),
    'Chiffre_d_affaires': np.random.randint(1000, 5000, 100)
})
# Affichage des 5 premières lignes des données
print("Premières lignes des données de vente :")
print(ventes.head())
print()
#Préparation des données :
# Calcul du chiffre d'affaires par unité de produit
ventes['CA_par_produit'] = ventes['Chiffre_d_affaires'] / ventes['Quantité']
 #Nettoyage des données :
# Suppression des lignes avec une quantité de vente négative
ventes = ventes[ventes['Quantité'] > 0]
#visualisation de donnes 
# Affichage des 5 premières lignes des données après nettoyage
print("Premières lignes des données après nettoyage :")
print(ventes.head())
print()
# Visualisation des ventes mensuelles par produit
plt.figure(figsize=(10, 6))
sns.barplot(data=ventes, x='Mois', y='Quantité', hue='Produit', palette='Set2')
plt.title('Ventes Mensuelles par Produit')
plt.xlabel('Mois')
plt.ylabel('Quantité Vendue')
plt.xticks(rotation=45)
plt.legend(title='Produit')
plt.show()