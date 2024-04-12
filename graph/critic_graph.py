
import pandas as pd
import plotly.express as px

def update_critic_graph(df):
    marvel_scores = df[df['Distributor'] == 'Marvel']['Rotten Tomatoes Critic Score'].mean()
    dc_scores = df[df['Distributor'] == 'DC']['Rotten Tomatoes Critic Score'].mean()
    difference = marvel_scores - dc_scores

    data = {'Distributor': ['Marvel', 'DC'], 'Score Difference': [difference, 0]}
    df_diff = pd.DataFrame(data)

    fig = px.bar(df_diff, x='Distributor', y='Score Difference', title='Difference in Critic Scores between Marvel and DC Films')
    return fig
