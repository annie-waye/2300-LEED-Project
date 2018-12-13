from . import fetch as mfetch
from src.proj.usgbc import fetch as ufetch
from src.proj.usgbc import process as uproc
import cartopy.crs as ccrs
import cartopy.feature as cfeat
import cartopy.io.shapereader as cshp
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
import os
import pathlib as plib


def show():
    cwd = os.getcwd()
    root = plib.Path(cwd).parents[1]

    coords_path = os.path.join(root, 'data', 'raw', 'massachusetts_cities_coords.csv')
    coords = mfetch.get_data(coords_path)

    x = coords['Latitude'].values
    y = coords['Longitude'].values

    request = cimgt.OSM()
    fig, ax = plt.subplots(figsize=(10, 16),
                           subplot_kw=dict(projection=request.crs))

    ax.set_extent([-73.41, -69.93, 41.21, 42.92])
    ax.add_image(request, 8)

    county_shape = os.path.join(root, 'data', 'maps', 'county', 'countyl010g.shp')
    county_reader = cshp.Reader(county_shape)
    counties = list(county_reader.geometries())
    county_features = cfeat.ShapelyFeature(counties, ccrs.PlateCarree())
    ax.add_feature(county_features, facecolor='none', edgecolor='gray')
    ax.set_title('LEED Buildings in Massachusetts')

    plt.plot(x, y,
             color='red', linewidth=0, marker='o',
             transform=ccrs.Geodetic(), label='LEED-Certified Building'
             )

    ax.legend()

    plt.show()