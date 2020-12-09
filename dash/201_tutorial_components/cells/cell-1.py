app.layout = html.Div(children=[

    html.H1(children='My Dash App'),

    dcc.Input(
        id='input-field',
        type='text'
    )
])