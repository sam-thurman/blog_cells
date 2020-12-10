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