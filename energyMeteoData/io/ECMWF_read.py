
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

if path.exists(Path.home() / "local_config.py"):
    sys.path.append(str(Path.home()))
    from local_config import My_local_config
    data_path_pathlib = My_local_config()
else:
    if path.exists("local_config.py"):
        from local_config import My_local_config
        data_path_pathlib = My_local_config()
    else:
        My_data_path = Path().absolute() / 'energyMeteoData' #/ 'data'
        data_path_pathlib = {'base': My_data_path,'ECMWF': My_data_path / "ECMWF"}
#endregion

#region function definition

def get_possible_codes(data_path_pathlib,
                zone_file = data_path_pathlib['Europe'] / 'europe.shp',
                zone_map_CODE_name="FIRST_FIPS"):
    zone_map = geopandas.read_file(zone_file)
    return zone_map[zone_map_CODE_name].unique()

def load_netcdf(data_path_pathlib,Variable,year,
                filePattern = "ioera5_(__Variable__)_(__year__).nc",
                zone_CODE = None,
                zone_file = data_path_pathlib['Europe'] / 'europe.shp',
                zone_map_CODE_name="FIRST_FIPS"):
    filename =filePattern.replace("(__Variable__)", Variable).replace("(__year__)", year)
    ds = xr.open_dataset(data_path_pathlib['ECMWF'] / filename, decode_coords="coordinates",decode_times=True) ### decode_coords ne semble pas fonctionner
    df = ds.to_dataframe()
    df_lolat = df.reset_index()[["longitude","latitude"]].drop_duplicates()
    gdf = geopandas.GeoDataFrame(df_lolat, geometry=geopandas.points_from_xy(df_lolat.longitude, df_lolat.latitude))

    if not zone_CODE == None :
        zone_map =  geopandas.read_file(zone_file)
        country_map_selected = zone_map.loc[zone_map[zone_map_CODE_name].isin(zone_CODE),:]
        good_grid_points = geopandas.sjoin(gdf,country_map_selected).set_index(["longitude" , "latitude"])[[zone_map_CODE_name]]
        df_with_good_grid_points=pd.merge(df.reset_index(),good_grid_points.reset_index(),on=["longitude","latitude"],how="inner").set_index(["longitude","latitude","time",zone_map_CODE_name])
    else :
        df_with_good_grid_points= df;

    return ds,df_with_good_grid_points
#endregion

### exemple avec deux zones d'europe
get_possible_codes(data_path_pathlib)
ds,MyWindData = load_netcdf(data_path_pathlib,Variable = "Wind",year = str(2019),zone_CODE = ["FR"])
#
# ### utilisation d'une autre carte, ici les régions de France
# get_possible_codes(data_path_pathlib,zone_file = data_path_pathlib['France'] / 'Regions.shp',
#                 zone_map_CODE_name="ADMIN_NAME")
#
# MyWindData = load_netcdf(data_path_pathlib,Variable = "Wind",year = str(2011),
#                          zone_file = data_path_pathlib['France'] / 'Regions.shp',
#                          zone_map_CODE_name="ADMIN_NAME",zone_CODE = ['Alsace', 'Aquitaine'])
