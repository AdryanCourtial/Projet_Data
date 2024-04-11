# import matplotlib.pyplot as plt
# import pandas as pd



# def film_budget():
#     df = pd.read_csv('DATA_ESSAiE2.csv', sep=";")

#     df['Budget'] = df['Budget'].astype(str)

#     fig, ax = plt.subplots()

#     ax.plot(range(len(df)), df['Budget'])

#     plt.xlabel('Film')
#     plt.ylabel('Budget')
#     plt.title('Budget des films DC et Marvel')

#     plt.xticks(range(len(df)), df['Film'], rotation=90)

#     plt.show()


# if __name__ == "__main__":
#     film_budget()

# print(pd.read_csv('DATA_ESSAiE2.csv'))

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Créer une nouvelle figure
plt.figure(figsize=(10, 5))

# Créer une carte du monde avec Basemap
m = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')

# Dessiner les côtes, les frontières des pays et les méridiens/parallèles
m.drawcoastlines()
m.drawcountries()
m.drawparallels(range(-90,91,30), labels=[1,0,0,0]) # Latitude
m.drawmeridians(range(-180,181,60), labels=[0,0,0,1]) # Longitude

# Placer des marqueurs sur la carte pour répertorier des données
# Par exemple, placer un marqueur à Paris
lat, lon = 48.8566, 2.3522
x, y = m(lon, lat)
m.plot(x, y, 'ro', markersize=10, label='Paris')

# Placer un texte à côté du marqueur
plt.text(x, y, 'Paris', fontsize=12, ha='right')

# Ajouter une légende
plt.legend()

# Titre de la carte
plt.title('Carte du monde avec marqueurs')

# Afficher la carte
plt.show()
