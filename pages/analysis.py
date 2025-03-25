import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

f = open('./data/about_the_data.md', 'r')
data = f.read()


layout = dcc.Markdown(data)
