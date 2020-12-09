import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

# import an external stylesheet, will be a CSS file
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# set up the reference to our Dash Application and link to external style
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# LAYOUT, will hold all of our application "structure"
app.layout = html.Div(children=[
    
    html.H1(children='My Dash App'),

    dcc.Input(
        id='input-field',
        type='text'
    ),

    html.H3(id='output-header')
])

if __name__ == '__main__':
    # open server and host app
    # tell Dash to refresh our browser every time we make a code change
    app.run_server(debug=True)