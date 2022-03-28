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
        style={
            'color': colors['white'],
            'textAlign': 'center',
            'marginTop': '10px',
            'marginBottom': '5px'
        }
    ),
    html.Div(
        children='Dash: A web application framework for Python.',
        style={
            'textAlign': 'center',
            'marginBottom': '20px'
        }
    ),
    # carousel(),
    # html.Div(
        # children=[card('Hello everybody')],
        # className='p-3',
    # ),
    html.Div(
        children=[
            dcc.Graph(
                id='example-graph',
                figure=figura(),
                style={
                    'height': '400px',
                    'width': '45%'
                }            
            ),
            dcc.Graph(
                id='example-graph2',
                figure=figura(),
                style={
                    'height': '400px',
                    'width': '45%'
                }
            ),
        ],
        style={
            'width': '100%', 
            'display':'flex',
            'justify-content':'space-around',
        },
    )
])

# Ejecución del script
if __name__ == '__main__':
    app.run_server(debug=True)