import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

csv_file = 'dc_marvel_movie_performance.csv'

df = pd.read_csv(csv_file)

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()