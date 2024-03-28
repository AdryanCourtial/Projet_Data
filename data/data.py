import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

columns = ["Film", "Budget"]


# csv_file = 'dc_marvel_movie_performance.csv'

df = pd.read_csv('dc_marvel_movie_performance.csv', usecols=columns)


print("Contents in csv file:", df)



plt.plot(df.Film, df.Budjet)

plt.show()