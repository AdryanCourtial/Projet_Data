from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd

# Chargement des données depuis le fichier CSV
df = pd.read_csv('data/DATA_ESSAiE2.csv', delimiter=';')

# Création de l'application Dash
app = Dash(__name__)

# Styles CSS
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Définition de la mise en page de l'application
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
        dcc.Graph(id='graph-content')
    ], className='container mt-5')
])

# Définition de la fonction de mise à jour du graphique en fonction des films sélectionnés
@app.callback(
    Output('film-graph-content', 'figure'),
    [Input('update-film-button', 'n_clicks')],
    [State('film-dropdown', 'value')]
)
def update_film_graph(n_clicks, selected_films):
    filtered_df = df[df['Film'].isin(selected_films)]
    fig = px.bar(filtered_df, x='Year', y='Box office gross Worldwide', color='Film', barmode='group', title='Box office gross Worldwide for selected films')
    return fig

# Définition de la fonction de mise à jour du graphique principal
@app.callback(
    Output('graph-content', 'figure'),
    [Input('film-graph-content', 'hoverData')]
)
def update_main_graph(hover_data):
    if hover_data and 'points' in hover_data[0]:
        year = hover_data[0]['points'][0]['x']
        filtered_df = df[df['Year'] == year]
        fig = px.scatter(filtered_df, x='Budget', y='Box office gross Worldwide', color='Film', title=f'Box office gross Worldwide vs. Budget in {year}')
        return fig
    else:
        return px.scatter(df, x='Budget', y='Box office gross Worldwide', color='Film', title='Box office gross Worldwide vs. Budget')

# Exécution de l'application
if __name__ == '__main__':
    app.run_server(debug=True)
