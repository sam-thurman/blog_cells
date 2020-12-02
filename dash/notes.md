### What is dash

Dash is a (mostly) open-sourced dashboarding framework for building analytics-centric web applications in Python. Dash--built on top of Plotly.js, React.js and Flask--allows you to create and deploy high quality visuals and extremely customizable interfaces for displaying and exploring data.

### What makes up a Dash app

- Dash application code is composed of two parts
  - 1st - `layout`
    - describes the structure, what the application looks like
    - doesn't describe how the app should update
    - Dash provides Python classes for all of the visual components of the application
      - a core set of components lives in the `dash_core_components` and `dash_html_components` libraries, but you can build your own with Javascript and React
  - 2nd
    - describes interactivity of the application - how input elements should update output elements
    - for interactivity, use `@app.callback()` and dash decorators

```
@app.callback(
  dash.dependencies.Output('my-graph'),
  [dash.dependencies.Input('my-dropdown')]
)
def function(input_properties):
  ...
```

- first argument is output element(s), second argument is list of input elements

### Layout

- You'll notice `layout` is composed of a tree of "components" like `html.Div` and `dcc.Graph`
- Dash is _declarative_, meaning each component in Dash is described through keyword attribrutes, and every option that is configurable within a component is available as one of these keyword arguments.

### dash_html_components (imported `as html`)

- The `dash_html_components` library contains a component class for every HTML tag as well as keyword arguments for all of the HTML arguments.
- We use these components within `layout` to create the structutre of our applicaiton.
- While these components create and relate directly to real HTML components that will be rendered, there are a few syntactical differences between raw HTML and the components in `dash_html_components`.
- For example, these two lines of code would render the same thing on a web page

```
html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'}) # Dash code
<h1 style="text-align: center; color: #7FDBFF">Hello Dash</h1>           # HTML equivalent
```

- `style` property in HTML is a semicolon-sperated string. In Dash, you simply supply a dictionary
- keys in `style` dict are "camelCase" as oposed to "kebab-case"
- assign HTML `class` attribute as `className` in Dash
- children of the HTML tag is specified through the `children` argument - by convention, the `children` property is always the first attribute, which means that we can omit it

Asside from these differences, all other HTML attributes and tags act the same and are still available to you in Python through Dash

### dash_core_components (imported `as dcc`)

- includes a set of high-level components like dropdown menus, markdown text-blocks, graphs, and more.
- like the rest of dash, these comonents are highly declarative--meaning options are configurable through keyword arguments.
  - link to Dash Core Components documentation: https://dash.plotly.com/dash-core-components
- For rendering interactive data visualizations, we use the `Graph` component (will render using Plotly.js)
  - create a Plotly.py figure and feed it to the `figure` argument of `Graph`
    - link to Plotly.py documentation: https://plotly.com/python/
