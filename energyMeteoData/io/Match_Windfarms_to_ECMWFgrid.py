#region importations
#import typing
import xarray as xr
#import fiona
import geopandas as gpd
import pandas as pd
from os import path
from pathlib import Path
import numpy as np
import sys
import matplotlib.pyplot as plt
import xarray as xr
#import rioxarray
from shapely.geometry import Point
#endregion

#region meteo data France
#fiter dsECMWF for France only
#France coordinates:
min_lon = -4.65
min_lat = 51.0
max_lon = 9.45
max_lat = 41.60 #source: https://latitudelongitude.org/fr/
dsECMWF_FR = dsECMWF.sel(latitude=slice(min_lat,max_lat), longitude=slice(min_lon,max_lon))
#endregion

#region extract ECMWF grid as GeoDataFrame (geometry = lat,lon)
ECMWFlong = dsECMWF_FR.longitude
ECMWFlat = dsECMWF_FR.latitude
ECMWFlongnp = ECMWFlong.to_numpy()
ECMWFlatnp = ECMWFlat.to_numpy()

polygons = []
for x in ECMWFlongnp:
    for y in ECMWFlatnp:
        polygons.append(Point(x,y))
ECMWFgrid = gpd.GeoDataFrame({'geometry':polygons})
#endregion

#region windfarms France
france_windfarms = gdfTWP[gdfTWP.Country=="France"]
france_windfarms.reset_index(drop=True,inplace=True)
#end region

#region plot France
fig1, ax = plt.subplots(figsize=(12, 6))

worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
francemap = worldmap[worldmap.name=="France"]
francemap.plot(color="lightgrey",ax=ax) #plot France contour

ECMWFgrid.plot(color="red", ax=ax,markersize=0.5,legend=True) #plot ECMWF gridpoints

france_windfarms.plot(color="blue",ax=ax,markersize=0.5,legend=True) #plot TWP windfarms
#endregion

#region match each windfarm to a point in the grid (the closest one)
gdfTWP_with_closest_gridpoint = gpd.sjoin_nearest(france_windfarms,ECMWFgrid)
gdfTWP_with_closest_gridpoint = gdfTWP_with_closest_gridpoint.rename(columns={'index_right':'gridpoint_index'})
#end region





