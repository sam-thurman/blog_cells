import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = px.data.gapminder()

app.layout = html.Div(children=[

    html.H1('Gapminder Visualizer'),

    dcc.Dropdown(
        id=
    )
])

if __name__ = '__main__':
    app.run_server(debug=True)