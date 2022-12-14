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

#filter out no-power-data points and no-commissioning-date-data points
gdfTWP_with_closest_gridpoint = gdfTWP_with_closest_gridpoint[gdfTWP_with_closest_gridpoint["Total power"]!="#ND"]
#gdfTWP_with_closest_gridpoint = gdfTWP_with_closest_gridpoint[gdfTWP_with_closest_gridpoint["Commissioning date"]!="#ND"]

#sum of total power for each gridpoint (at present, considering all windfarms)
gdfTWP_gruped_by_closest_gridpoint = gdfTWP_with_closest_gridpoint.groupby(['gridpoint_index'])["Total power"].sum()

#region computation taking commisioning dates into account

#simplificated dataFrame leaving only columns of interest
simplified_df = gdfTWP_with_closest_gridpoint.drop("geometry",axis=1)
simplified_df = simplified_df[["gridpoint_index","Commissioning date","Area","Total power"]]

#group by gridpoint and commissioning date, cumulative sum
simplified_df_gruped_by_closest_gridpoint_and_comdate = simplified_df.groupby(['gridpoint_index','Commissioning date']).sum().groupby(level=0).cumsum()
#endregion

