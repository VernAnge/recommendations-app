"""
BI Dashboard Script

This script creates a Business Intelligence (BI) dashboard using Dash. The dashboard allows users to interactively explore data related to customer interactions and activity levels. It includes dropdown filters and visualizations for interaction types and customer activity distribution.

Modules:
    - pandas: Used for data manipulation and analysis.
    - dash: Used for creating the web application.
    - plotly.express: Used for creating interactive graphs.

Functions:
    - update_interaction_graph(interaction_type): Updates the bar graph based on the selected interaction type.
    - update_customer_activity_graph(interaction_type): Updates the pie chart showing customer activity distribution.

Usage:
    Run the script to start the Dash web server and access the dashboard through a web browser.

"""
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('cleaned_data.csv')

# Init
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1('BI Dashboard'),
    dcc.Dropdown(
        id='interaction-type-dropdown',
        options=[{'label': interaction, 'value': interaction} for interaction in df['interaction'].unique()],
        placeholder='Select an interaction type'
    ),
    dcc.Graph(id='interaction-graph'),
    html.H2('Customer Activity'),
    dcc.Graph(id='customer-activity-graph')
])

@app.callback(
    Output('interaction-graph', 'figure'),
    [Input('interaction-type-dropdown', 'value')]
)
def update_interaction_graph(interaction_type):
    """
    Updates the bar graph based on the selected interaction type.

    Parameters:
        interaction_type (str): The selected interaction type from the dropdown.

    Returns:
        fig (Figure): A Plotly bar graph showing the interactions for the selected type.
    """
    filtered_df = df[df['interaction'] == interaction_type]
    fig = px.bar(filtered_df, x='item_descrip', y='idcol', title=f'Interactions for {interaction_type}')
    return fig

@app.callback(
    Output('customer-activity-graph', 'figure'),
    [Input('interaction-type-dropdown', 'value')]
)
def update_customer_activity_graph(interaction_type):
    """
    Updates the pie chart showing customer activity distribution.

    Parameters:
        interaction_type (str): The selected interaction type from the dropdown (not used in this function).

    Returns:
        fig (Figure): A Plotly pie chart showing the distribution of customer activity.
    """
    activity_counts = df['active_ind'].value_counts()
    fig = px.pie(activity_counts, values=activity_counts, names=activity_counts.index, title='Customer Activity Distribution')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
