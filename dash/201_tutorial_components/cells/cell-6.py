import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# load gapminder data
data = px.data.gapminder()

# grab data for United States
USA = data[data.country=='United States']

#list of columns we want
cols = ['lifeExp', 'pop', 'gdpPercap']

# dash needs Dropdown 'options' to be in {'label': 'option name', 'value': option-value} format
dropdown_options = [{'label':col,'value':col} for col in cols]

app.layout = html.Div(children=[

    html.H1('Gapminder Visualizer'),

    dcc.Graph(
        id='graph'
    ),

    dcc.Dropdown(
        id='dropdown',
        options=dropdown_options, # options in list, properly formatted
        value='pop' # we can set a default value
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)