import pandas as pd
from geopy.geocoders import Nominatim
import os
import pathlib as plib


def add_coords(coords, city, state):
    gloc = Nominatim(user_agent='my-application', timeout=3)
    loc = gloc.geocode(city + ' ' + state)
    if loc is None:
        coords[city] = None
    else:
        coords[city] = [loc.raw['lon'], loc.raw['lat']]
    pass


def get_coords(cities, state):
    coords = {}
    for city in cities:
        add_coords(coords, city, state)

    cts = list(coords.keys())
    vals = list(coords.values())
    lats = []
    lons = []
    for x in vals:
        if x is None:
            lats.append(None)
            lons.append(None)
        else:
            lats.append(x[0])
            lons.append(x[1])

    df = pd.DataFrame({'City': cts, 'Latitude': lats, 'Longitude': lons})
    df = df.dropna()
    df = df.reset_index(drop=True)

    root = plib.Path(os.getcwd()).parents[1]
    filename = os.path.join(root, 'data', 'raw',
                            state.lower() + '_cities_coords.csv')
    df.to_csv(filename, index=False)
    pass
