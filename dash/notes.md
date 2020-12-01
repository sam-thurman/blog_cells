- Dash apps are composed of two parts - 1st - `layout` - describes what the application looks like - doesn't describe how the app should update - 2nd - describes interactivity of the application - how input elements should update output elements
  for interactivity, use `@app.react()` and dash decorators

```
@app.react('my-graph', ['my-dropdown'])
```

first argument is output element(s), second argument is list of input elements

- Dash provides Python classes for all of the visual components of the application
  - a core set of components lives in the `dash_core_components` and `dash_html_components` libraries, but you can build your own with Javascript and React

### About HTML in Dash

- The `dash_html_components` library contains a component class for every HTML tag as well as keyword arguments for all of the HTML arguments.
