#Librerias 
from pydoc import classname
from turtle import width
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from components import card, navbar, carousel
from graphs import scatter_plot_1, scatter_plot_2, bar_plot_1, bar_plot_2, bar_plot_3

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
    html.Div(
        children=[
            dcc.Graph(
                id='example-graph',
                figure=scatter_plot_1(),
                style={
                    'height': '400px',
                    'width': '45%',
                    'border': '2px solid white',
                    'borderRadius': '10px',
                    'boxShadow': '0px 4px 10px 0px rgba(255,255,255,0.3)'

                }            
            ),
            dcc.Graph(
                id='example-graph2',
                figure=scatter_plot_2(),
                style={
                    'height': '400px',
                    'width': '45%',
                    'border': '2px solid white',
                    'borderRadius': '10px',
                    'boxShadow': '0px 4px 10px 0px rgba(255,255,255,0.3)'
                }
            ),
        ],
        style={
            'width': '100%', 
            'display':'flex',
            'justifyContent':'space-around',
        },
    ),
    html.Div(
        children=[
            dcc.Graph(
                id='bar-plot_1',
                figure=bar_plot_1(),
                style={
                    'height': '400px',
                    'width': '45%',
                    'border': '2px solid white',
                    'borderRadius': '10px',
                    'boxShadow': '0px 4px 10px 0px rgba(255,255,255,0.3)'

                }            
            ),
            dcc.Graph(
                id='bar-plot_3',
                figure=bar_plot_3(),
                style={
                    'height': '400px',
                    'width': '45%',
                    'border': '2px solid white',
                    'borderRadius': '10px',
                    'boxShadow': '0px 4px 10px 0px rgba(255,255,255,0.3)'

                }            
            ),
        ],
        style={
            'background': 'red',
            'height': 'auto',
            'width': '100%',
            'marginTop': '50px',    
            'display':'flex',
            'justifyContent':'space-around',
        }
    ),
    html.Div(
        children=[
            dcc.Graph(
                id='bar-plot_2',
                figure=bar_plot_2(),
                style={
                    'height': '400px',
                    'width': '80%',
                    'border': '2px solid white',
                    'borderRadius': '10px',
                    'boxShadow': '0px 4px 10px 0px rgba(255,255,255,0.3)',
                    'display':'flex',
                    'margin':'50px auto',

                }            
            ),
        ]
    )
])

# Ejecución del script
if __name__ == '__main__':
    app.run_server(debug=True)