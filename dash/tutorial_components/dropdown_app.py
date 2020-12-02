import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# import an external stylesheet, will be a CSS file
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# set up the reference to our Dash Application and link to external style
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# create some data to plot
df = pd.DataFrame({
    "Fruit":["Apple", "Orange", "Banana", "Orange", "Peach", "Apple", "Peach", "Banana"],
    "Amount":[3, 6, 2, 4, 6, 5, 7, 2],
    "Store":["Bob's Cornerstore", "Jenny's Convenience", "Jenny's Convenience", "Bob's Cornerstore", "Bob's Cornerstore", "Jenny's Convenience", "Jenny's Convenience", "Bob's Cornerstore"]
})

# create bar plot from our newly created data
# see https://plotly.com/python/px-arguments/ for more options
fig = px.bar(df, x="Fruit", y="Amount", color="Store", barmode="group")

# LAYOUT, will hold all of our application "structure"
app.layout = html.Div(children=[
    html.H1(children='My First Dash App'),

    html.Div(children='''
        Dash: A web-app framework for Python.
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