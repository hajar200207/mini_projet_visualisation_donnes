import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Créer un DataFrame avec des données fictives
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y1': [10, 15, 7, 20, 12],
    'y2': [5, 12, 9, 14, 8],
    'category': ['A', 'B', 'C', 'D', 'E']
})

# Fonction pour afficher les graphiques
def display_plots():
    # Figure de base
    
    fig1 = go.Figure()
    # Scatter plot

    fig2 = go.Figure(data=go.Scatter(x=df['x'], y=df['y1'], mode='markers', name='Scatter Plot'))
    # Bar plot
    fig3 = go.Figure(data=go.Bar(x=df['category'], y=df['y1'], name='Bar Plot'))
    # Pie chart
    fig4 =go.Figure(data=go.Pie(labels=df['category'], values=df['y1'], name='Pie Chart'))
    
    # Heatmap
    data = [
        go.Heatmap(
            z=[[10, 15, 7, 20, 12],
               [5, 12, 9, 14, 8]],
            x=['A', 'B', 'C', 'D', 'E'],
            y=['2019', '2020'],
            colorscale='Viridis'
        )
    ]
    fig5 = go.Figure(data=data)
    # Box plot
    fig6 = go.Figure(data=go.Box(y=df['y1'], name='Box Plot'))
    # Line plot with Plotly Express
    fig7 = px.line(df, x='x', y='y1', title='Line Plot with Plotly Express')
    # Scatter plot with Plotly Express
    fig8 = px.scatter(df, x='x', y='y1', color='category', title='Scatter Plot with Plotly Express')
    # Afficher les figures
    fig1.show();fig2.show();fig3.show();fig4.show()
    fig5.show();fig6.show();fig7.show();fig8.show()
# Appel de la fonction pour afficher les graphiques
display_plots()
