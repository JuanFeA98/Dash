import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

styles = ['.assets/styles.css']

app = dash.Dash(__name__, external_stylesheets=styles)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])  

index_page = html.Div([
    html.Header(
        children = [
            html.Img(id='logo', src='https://image.flaticon.com/icons/png/512/814/814513.png'),
            html.Div('Dashboard')
        ]
    ),
    dcc.Link('Go to page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to page 2', href='/page-2')     
])

page_1_layout = html.Div([
    html.H1('Hello page 1')
])


page_2_layout = html.Div([
    html.H1('Hello page 2')
])


def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return page_2_layout


if __name__ == '__main__':
    app.run_server(debug=True)
