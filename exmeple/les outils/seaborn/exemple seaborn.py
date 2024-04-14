import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Créer des DataFrames avec des données fictives
# DataFrame pour tips
tips_data = {
'total_bill': [25.12, 48.45, 30.50, 20.25, 60.34],
'tip': [3.50, 7.50, 5.00, 2.50, 10.00],
'sex': ['Female', 'Male', 'Female', 'Female', 'Male'],
'day': ['Sun', 'Sat', 'Fri', 'Sat', 'Sun']
}
tips_df = pd.DataFrame(tips_data)
# DataFrame pour iris
iris_df = sns.load_dataset("iris")
# Fonction pour afficher les graphiques
def display_plots():
    # Catplot avec DataFrame tips
    sns.catplot(x="day", y="total_bill", hue="sex", kind="bar", data=tips_df)
    plt.title("Catplot: Total Bill by Day and Sex")
    plt.show()
    # Regplot avec DataFrame tips
    sns.regplot(x="total_bill", y="tip", data=tips_df)
    plt.title("Regplot: Total Bill vs. Tip")
    plt.show()
    # Jointplot avec DataFrame iris
    sns.jointplot(x="sepal_length", y="sepal_width", data=iris_df, kind="hex")
    plt.suptitle("Jointplot: Sepal Length vs. Sepal Width")
    plt.show()
    # Boxplot avec DataFrame iris
    sns.boxplot(x="species", y="petal_length", data=iris_df)
    plt.title("Boxplot: Petal Length by Species")
    plt.show()
    # Pairplot avec DataFrame iris
    sns.pairplot(iris_df, hue="species")
    plt.suptitle("Pairplot: Pairwise Relationships by Species")
    plt.show()
    # Lmplot avec DataFrame tips
    sns.lmplot(x="total_bill", y="tip", hue="sex", data=tips_df)
    plt.title("Lmplot: Total Bill vs. Tip with Regression by Sex")
    plt.show()
# Appel de la fonction pour afficher les graphiques
display_plots()
