import pandas as pd
import numpy as np

import plotly.express as px

from dash import Dash, html

# Datos
battles = pd.read_csv('Data/battles.csv')

# Limpieza de los datos 
battles['battle_type'].fillna('Unknown', inplace=True)
battles['attacker_king'].fillna('Unknown', inplace=True)

battles['attacker_size'].fillna(battles['attacker_size'].mean(), inplace=True)
battles['defender_size'].fillna(battles['defender_size'].mean(), inplace=True)

# Construcción de variables
battles['total_warriors'] = battles['attacker_size'] + battles['defender_size']

# Gráfica 
def figura():
    fig = px.scatter(
        battles[battles['name'] != 'Battle of Castle Black'], 
        x='attacker_size', 
        y='defender_size', 
        color='region',
        size='total_warriors',
        hover_data=['name', 'battle_type']
    )

    return fig