import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

import dash 
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets) 

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    dcc.Link('Navegar a /', href='/1'),
    html.Br(),
    dcc.Link('Navegar a /page-2', href='/2'),

    html.Div(id='page-content')
])

@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')]
)

def display_page(pathname):
    return html.Div([
        html.H2(
            f'Estas en la pagina: {pathname[1]}'
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)