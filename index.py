python
import pandas as pd
import matplotlib.pyplot as plt
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the SAIDI dataset
data = pd.read_csv('SAIDI.csv')

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Annual SAIDI Data Dashboard (2013-2025)"),
    html.Div([
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(year), 'value': year} for year in data['SAIDI_year'].unique()],
            placeholder="Select a year",
            multi=True
        )
    ]),
    dcc.Graph(id='saidi-graph'),
])

# Callback to update graph based on dropdown selection
@app.callback(
    Output('saidi-graph', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_graph(selected_years):
    if not selected_years:
        filtered_data = data
    else:
        filtered_data = data[data['SAIDI_year'].isin(selected_years)]

    fig = {
        'data': [
            {
                'x': filtered_data['SAIDI_year'],
                'y': filtered_data['SAIDI_value'],
                'type': 'bar',
                'name': 'SAIDI'
            }
        ],
        'layout': {
            'title': 'SAIDI Data Visualization',
            'xaxis': {'title': 'Year'},
            'yaxis': {'title': 'SAIDI (minutes per customer)'}
        }
    }
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
