import dash
import pandas as pd
from dash import Dash, html
import dash_bootstrap_components as dbc
from component.nav import get_navbar
pd.options.mode.chained_assignment = None  # Disable the warning

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    use_pages=True
)

server = app.server

app.layout = html.Div(children=[
    html.Div(
        get_navbar(),
        style= {"margin": "-20px -20px 20px -20px"}
    ),
    dash.page_container
    
], style= {"margin": "20px 20px 20px 20px"})


if __name__ == '__main__':
    app.run_server(debug=True)
