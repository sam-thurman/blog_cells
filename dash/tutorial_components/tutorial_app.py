import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# export an external stylesheet, will be CSS code
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# set up the reference to our Dash Application and link external style
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Product": ["Case (128 cans) Beer", "Apples", "Oranges", "Bananas", "Lemons", "Oranges", "Bananas"],
    "Amount": [10, 12, 12, 10, 15, 13, 5],
    "Store": ["Paddy's Pub", "Bubbles' Shed n' Breakfast", "Bubbles' Shed n' Breakfast", "Paddy's Pub", "Paddy's Pub", "Paddy's Pub", "Bubbles' Shed n' Breakfast"]
})

fig = px.bar(df, x="Product", y="Amount", color="Store", barmode="group")

# Layout, will hold all of our application "structure"
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    # open server and host app
    # tell Dash to refresh our browser every time we make a code change
    app.run_server(debug=True)