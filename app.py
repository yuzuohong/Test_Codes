# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


import pandas as pd

file = 'D:\\Book1.xlsx'

df = pd.read_excel(file,sheet_name='Sheet1',header=0,converters={'Movement Type':str, 'Entries':int})

external_stylesheets = ['https://codepen.io/chriddyp/pen/GYoxoq.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Goods Movement Postings'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['Movement Type'], 'y': df['Entries'], 'type': 'bar', 'name': 'Goods movement postings'},

            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
