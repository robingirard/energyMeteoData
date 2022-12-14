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

#we start from simplified_df created in the weight_per_gridpoint script

#region define French regions
simplified_df.reset_index(inplace=True)

#endregion

