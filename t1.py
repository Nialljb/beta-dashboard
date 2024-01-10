import dash
from dash import dcc
from dash import html
import pandas as pd
from sqlalchemy import create_engine

# Create a database engine
engine = create_engine('testData.csv')

# Read data from the relational database
df = pd.read_sql_query('SELECT * FROM table_name', engine)

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children='''
        Data visualization using Dash
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['PID'], 'y': df['TICV'], 'type': 'bar', 'name': 'Column 1'},
                {'x': df['PID'], 'y': df['wm_vol'], 'type': 'bar', 'name': 'Column 2'},
            ],
            'layout': {
                'title': 'Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
