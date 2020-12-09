@app.callback(
    Output('output-header','children'),
    [Input('input-field','value')]
)
def update_header(prop):
    return prop