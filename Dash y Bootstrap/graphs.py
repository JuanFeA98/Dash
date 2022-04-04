import pandas as pd
import numpy as np

import plotly.express as px

from dash import Dash, html

# BATALLAS
# Datos
battles = pd.read_csv('Data/battles.csv')

# Limpieza de los datos 
battles['battle_type'].fillna('Unknown', inplace=True)
battles['attacker_king'].fillna('Unknown', inplace=True)

battles['attacker_size'].fillna(battles['attacker_size'].mean(), inplace=True)
battles['defender_size'].fillna(battles['defender_size'].mean(), inplace=True)

# Construcción de variables
battles['total_warriors'] = battles['attacker_size'] + battles['defender_size']

# MUERTES
# Datos
deaths = pd.read_csv('Data/character-deaths.csv')

# Construcción de variables
a = deaths.groupby('Death Year')[['Name']].count().reset_index()
b = deaths.groupby('Allegiances')[['Name']].count().reset_index()
c = deaths.groupby('Nobility')[['Name']].count().reset_index()

# GRÁFICAS
 
# Scatter plot 1 
def scatter_plot_1():
    fig = px.scatter(
        battles[battles['name'] != 'Battle of Castle Black'], 
        x='attacker_size', 
        y='defender_size', 
        color='region',
        size='total_warriors',
        hover_data=['name', 'battle_type']
    )

    fig.update_layout({
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'font_color': "white",
        'plot_bgcolor': 'rgba(0,0,0,0)',
    
    })

    return fig

# Scatter plot 2
def scatter_plot_2():
    fig = px.scatter(
        battles[battles['name'] != 'Battle of Castle Black'], 
        x='attacker_size', 
        y='defender_size', 
        color='attacker_king',
        size='total_warriors',
        hover_data=['name', 'battle_type']
    )

    fig.update_layout({
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'font_color': "white",
        'plot_bgcolor': 'rgba(0,0,0,0)',
    })

    return fig

# Bar plot 1
def bar_plot_1():
    fig = px.bar(a, x='Death Year', y='Name')
    return fig

# Bar plot 2
def bar_plot_2():
    fig = px.bar(b, x='Allegiances', y='Name')
    return fig

# Bar plot 3
def bar_plot_3():
    fig = px.bar(c, x='Nobility', y='Name')
    return fig