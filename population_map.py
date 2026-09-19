from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure()

# Create axes
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Create map
m = Basemap(
    llcrnrlon=40.,
    llcrnrlat=20.,
    urcrnrlon=70.,
    urcrnrlat=45.,
    resolution='l',
    projection='merc',
    lat_0=32.,
    lon_0=55.,
    lat_ts=20.
)

# Draw map
m.drawcoastlines()
m.drawcountries()
m.fillcontinents()

# Cities coordinates
tehran_lat = 35.4120
tehran_lon = 51.2323

tabriz_lat = 38.426
tabriz_lon = 46.1746

isfahan_lat = 32.3841
isfahan_lon = 51.4003

shiraz_lat = 29.5918
shiraz_lon = 52.5837

# Population
tehran_population = 9039000
tabriz_population = 1643960
isfahan_population = 2109654
shiraz_population = 1869001

# Scatter
m.scatter(
    [tehran_lon, tabriz_lon, isfahan_lon, shiraz_lon],
    [tehran_lat, tabriz_lat, isfahan_lat, shiraz_lat],
    s=[
        tehran_population / 10000,
        tabriz_population / 10000,
        isfahan_population / 10000,
        shiraz_population / 10000
    ],
    color='blue',
    alpha=0.7,
    latlon=True
)

plt.title("Population of Major Cities in Iran")

plt.show()
