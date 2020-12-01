### Install Dash
```  
pip install dash
```
### Create file called `app.py` containing the following code
```
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

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
    app.run_server(debug=True)
```
- The `layout` is composed of a tree of "components" like `html.Div` and `dcc.Graph`.
- `dash_html_components` library has a component for every HTML tag. `html.H1(children='Hello Dash')` component generates a `<h1>Hello Dash</h1>` HTML element in your application.
- Not all components are pure HTML.  `dash_core_components` describe higher-level components that are interactive and are generated with JavaScript, HTML, and CSS through the React.js library.
- Each component is described entirely through keyword attributes. Dash is declarative: you will primarily describe your application through these attributes.
- The children property is special. By convention, it's always the first attribute which means that you can omit it: html.H1(children='Hello Dash') is the same as html.H1('Hello Dash'). Also, it can contain a string, a number, a single component, or a list of components.

### In the terminal, run our `app.py` script using the `python app.py`
You'll see the following output indicating our app is running:
```
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
```
### Copy and paste the URL (at top of output after `python app.py` command: "Dash is running on ____")provided into your browser to view our `app.py` dashboard