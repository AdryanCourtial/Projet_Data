import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input, State
from graph.film_graph import update_film_graph
from graph.comparison_graph import update_main_graph

df = pd.read_csv('data/DATA_ESSAiE2.csv', delimiter=';')

app = Dash(__name__)

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H1(children='Analyse des données', className='text-center mb-4'),
        html.Div([
            dcc.Dropdown(
                options=[{'label': film, 'value': film} for film in df['Film']],
                value=[df['Film'][0]],
                multi=True,
                id='film-dropdown',
                className='form-control'
            ),
            html.Button('Update Film Graph', id='update-film-button', className='btn btn-primary mt-2')
        ], className='form-group'),
        dcc.Graph(id='film-graph-content')
    ], className='container mt-5'),
    html.Div([
        dcc.Graph(id='comparison-graph')
    ], className='container mt-5')
])

# Callback pour mettre à jour le graphique de film
@app.callback(
    Output('film-graph-content', 'figure'),
    [Input('update-film-button', 'n_clicks')],
    [State('film-dropdown', 'value')]
)
def update_film(n_clicks, selected_films):
    return update_film_graph(n_clicks, selected_films, df)

# Callback pour mettre à jour le graphique de comparaison
@app.callback(
    Output('comparison-graph', 'figure'),
    [Input('film-graph-content', 'hoverData')]
)
def update_comparison(hover_data):
    return update_main_graph(hover_data, df)


if __name__ == '__main__':
    app.run_server(debug=True)
