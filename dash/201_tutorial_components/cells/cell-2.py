# callback "decorator", reference components to be used
@app.callback(
    # output first
    dash.dependencies.Output('output-id', 'output-prop-to-modify'),
    # inputs second, always passed as list (even if only 1 input)
    [dash.dependencies.Input('input-id', 'input-prop-to-use')]  
)
# define function
def transform_output(input_prop):
    # do some stuff, or not

    # return the value/object you want assigned to `output-prop-to-modify`
    return input_prop