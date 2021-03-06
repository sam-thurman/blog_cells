import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data = px.data.gapminder()

USA = data[data.country=='United States']

cols = ['lifeExp', 'pop', 'gdpPercap']

dropdown_options = [{'label':col,'value':col} for col in cols]

app.layout = html.Div(children=[

    html.H1('Gapminder Visualizer'),

    dcc.Graph(
        id='graph'
    ),

    dcc.Dropdown(
        id='dropdown',
        options=dropdown_options,
        value='pop'
    )
])


@app.callback(
    Output('graph','figure'),
    [Input('dropdown', 'value')]
)
def update_graph(prop):
    fig = px.line(
        USA,
        x='year',
        y=prop,
        title=f'United States {prop} over time'
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)