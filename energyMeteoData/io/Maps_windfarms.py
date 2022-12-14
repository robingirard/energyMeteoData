#region importations
#import typing
import xarray as xr
#import fiona
import geopandas
import pandas as pd
from os import path
from pathlib import Path
import numpy as np
import sys
import matplotlib.pyplot as plt
import xarray as xr
#endregion


#region Maps (world, Europe, France)

#region world
fig1, ax = plt.subplots(figsize=(12, 6))
worldmap = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
# Creating axes and plotting world map
worldmap.plot(color="lightgrey", ax=ax)
gdfTWP.plot(color="blue",ax=ax,markersize=0.5)
#endregion

#region Europe
fig2, ax = plt.subplots(figsize=(12, 6))
europemap = worldmap[worldmap.continent=="Europe"]
europemap.plot(color="lightgrey",ax=ax)
europe_windfarms = gdfTWP[gdfTWP.Continent=="Europe"]
europe_windfarms.plot(color="blue",ax=ax,markersize=0.5)
#endregion


#region France
fig3, ax = plt.subplots(figsize=(12, 6))
francemap = worldmap[worldmap.name=="France"]
francemap.plot(color="lightgrey",ax=ax)
france_windfarms = gdfTWP[gdfTWP.Country=="France"]
france_windfarms.plot(color="blue",ax=ax,markersize=0.5)
#endregion

#endregion

