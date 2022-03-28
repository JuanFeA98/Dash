#Librerias 
from pydoc import classname
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from components import card, navbar, carousel
from graphs import figura

# Inicializamos la app
app = Dash(external_stylesheets=[dbc.themes.DARKLY])

# Colores
colors = {
    'black' : '#1A1B25',
    'red' : '#F8C271E',
    'white' : '#EFE9E7',
    'background' : '#333333',
    'text' : '#FFFFFF'
}

# Establecemos el layout
app.layout = html.Div(children=[
    navbar(),
    html.H1(
        children='Hello Dash',
        className='text-center p-3',
        style={'color': colors['white']}
        ),
    html.Div(
        children='Dash: A web application framework for Python.',
        className='text-center p-1 text-light',
        ),
    # carousel(),
    html.Div(
        children=[card('Hello everybody')],
        className='p-3',
    ),
    dcc.Graph(
        id='example-graph',
        figure=figura()
    )
])

# Ejecución del script
if __name__ == '__main__':
    app.run_server(debug=True)