import matplotlib.pyplot as plt 
import numpy as np
# Fonction Title()
def Title():
    plt.title('Titre du Graphique')
# Fonction bar()
def bar():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([10, 20, 15, 25, 30])
    plt.bar(x, y)
# Fonction Show()
def Show():
    plt.show()
# Fonction hist()
def hist():
    data = np.random.normal(0, 1, 1000)
    plt.hist(data, bins=30)
# Fonction Legend()
def Legend():
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x), label='Sinus')
    plt.plot(x, np.cos(x), label='Cosinus')
    plt.legend()
# Fonction Plot()
def Plot():
    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
# Fonction Label([])
def Label():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.xlabel('Axe des X')
    plt.ylabel('Axe des Y')
# Fonction scatter()
def scatter():
    x = np.random.rand(50)
    y = np.random.rand(50)
    plt.scatter(x, y)
# Appel de toutes les fonctions
Title(); bar();Show()
hist();Plot();Label()
scatter();Legend()
# Affichage de tout le graphique final
plt.show()