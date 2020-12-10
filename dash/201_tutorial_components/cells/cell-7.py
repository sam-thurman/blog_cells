@app.callback(
    Output('graph','figure'),
    [Input('dropdown', 'value')]
)