import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(data, bins=5, edgecolor='black', alpha=0.2)
plt.title("Histogramme Simple")
plt.xlabel("Valeurs")
plt.ylabel("Fréquence")
plt.grid(True)
plt.show()
