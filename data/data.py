import matplotlib.pyplot as plt
import pandas as pd



def film_budget():
    df = pd.read_csv('dc_marvel_movie_performance.csv')

    df['Budget'] = df['Budget'].astype(str)

    fig, ax = plt.subplots()

    ax.plot(range(len(df)), df['Budget'])

    plt.xlabel('Film')
    plt.ylabel('Budget')
    plt.title('Budget des films DC et Marvel')

    plt.xticks(range(len(df)), df['Film'], rotation=90)

    plt.show()


if __name__ == "__main__":
    film_budget()