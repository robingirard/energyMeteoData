
#region importations
#import typing
import xarray as xr
#import fiona
import geopandas # mac had to use this https://github.com/conda-forge/shapely-feedstock/issues/53 DONE
#print(geopandas.__version__)
#import rioxarray # useless ?
import pandas as pd
from os import path
from pathlib import Path
import sys
import matplotlib.pyplot as plt
#endregion

dsECMWF = xr.open_dataset("/Users/sant/Documents/MINES PARIS/2A/T2/Recherche Simulation de Production éolienne/Github/Data/Données ECMWF nc/ioera5_Wind_2019.nc")
dfECMWF = dsECMWF.to_dataframe()
df_lolatECMWF = dfECMWF.reset_index()[["longitude","latitude"]].drop_duplicates()
gdfECMWF = geopandas.GeoDataFrame(df_lolatECMWF, geometry=geopandas.points_from_xy(df_lolatECMWF.longitude, df_lolatECMWF.latitude))

#To do: read all years
