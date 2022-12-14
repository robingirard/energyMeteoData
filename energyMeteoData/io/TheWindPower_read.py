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

#region read ThwWindPower windfarms Excel
dfTWP = pd.read_excel(Path("/Users") /"sant"/"Documents"/"MINES PARIS"/"2A"/"T2"/"Recherche Simulation de Production éolienne"/"Github"/"Data"/"Données TheWindPower Excel"/"Windfarms_World_20221116.xls",sheet_name="Windfarms")
dfTWP.drop(0,inplace=True) #eliminates first row (it does not contain data)
df2TWP = dfTWP[dfTWP["Longitude"]!="#ND"] #eliminates entries without coordinates data
#endregion

#region homogenize commissioning-date data
df2TWP = df2TWP[df2TWP["Commissioning date"]!="#ND"] #eliminates entries without commissioning-date data
df2TWP['Commissioning date'] = pd.to_datetime(df2TWP['Commissioning date'])
df2TWP['Commissioning date'] = df2TWP['Commissioning date'].dt.strftime('%Y%/%m')
df2TWP['Commissioning date'] = pd.to_datetime(df2TWP["Commissioning date"])
#endregion

#region info DataFrame
print(dfTWP.head()) #OK
print(dfTWP.columns) #OK
print(dfTWP.info())
#endregion

#region DataFrame to GeoDataFrame
gdfTWP = geopandas.GeoDataFrame(df2TWP, geometry=geopandas.points_from_xy(df2TWP.Longitude, df2TWP.Latitude))
print(gdfTWP)
#endregion
