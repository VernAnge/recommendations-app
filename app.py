import os
from dash import dcc, html, Dash
from dash.dependencies import Input, Output, State
import pandas as pd

if not os.path.exists('cleaned_data.csv'):
    print("Cleaned data file does not exist. Please run clean.py to generate it.")
    exit()

# Load cleaned data and products
df = pd.read_csv('cleaned_data.csv')
with open('recommended_products.txt') as f:
    recommended_products = f.read().splitlines()

# Init app
app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Store(id='login-state', storage_type='session'),
    dcc.Store(id='login-error', storage_type='session')
])

# Login page
login_layout = html.Div(className='centered', children=[
    html.Div(className='login-box', children=[
        html.H2('Login'),
        dcc.Input(id='user-id', type='text', placeholder='Enter User ID', className='login-input'),
        html.Button('Login', id='login-button', className='login-button'),
        html.Div(id='login-output', className='login-output')
    ])
])

# Main page
main_layout = html.Div([
    html.H2('Product Recommendations'),
    html.Div(id='recommendations'),
    html.H3('All Products'),
    html.Div([html.Div(product, className='product') for product in recommended_products], className='product-grid')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname'),
     Input('login-state', 'data'),
     Input('login-error', 'data')]
)
def display_page(pathname, login_state, login_error):
    if pathname == '/' or pathname == '/login':
        if login_error:
            login_layout.children[0].children[-1] = html.Div('Invalid User ID', style={'color': 'red'})
        else:
            login_layout.children[0].children[-1] = html.Div('')
        return login_layout
    elif pathname == '/main' and login_state == 'logged_in':
        return main_layout
    else:
        return login_layout

@app.callback(
    [Output('login-state', 'data'),
     Output('login-error', 'data'),
     Output('url', 'pathname')],
    [Input('login-button', 'n_clicks')],
    [State('user-id', 'value')],
    prevent_initial_call=True
)
def check_login(n_clicks, user_id):
    if n_clicks:
        if user_id and user_id in df['idcol'].astype(str).values:
            return 'logged_in', None, '/main'
        else:
            return None, 'error', Dash.no_update
    return Dash.no_update, Dash.no_update, Dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)