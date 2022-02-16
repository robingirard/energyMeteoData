from pkg_resources import resource_filename

# We define the paths for the various data folders

data_path = {'gis': resource_filename('buildingdata', 'data/gis'),
             'census': resource_filename('buildingdata', 'data/census'),
             'energy': resource_filename('buildingdata', 'data/energy'),
             'diagnosis': resource_filename('buildingdata', 'data/diagnosis'),
             'meteo': resource_filename('buildingdata', 'data/meteo'),
             'administrative_boundaries': resource_filename('buildingdata', 'data/administrative_boundaries')}


#### same but with pathlib
from pathlib import Path

My_data_path = Path().absolute() /'buildingdata' / 'data'


data_path_pathlib ={
    'base' : My_data_path,
    'diagnosis' : My_data_path / 'diagnosis',
    'energy': My_data_path / 'energy',
    'census': My_data_path / 'census',
    'gis': My_data_path / 'gis',
    'meteo': My_data_path / 'meteo',
    'administrative_boundaries' : My_data_path / 'administrative_boundaries',
    'IGN' : My_data_path / 'gis',
}

def set_display():
    None
### trying to find a local config
import importlib
local_config = importlib.util.find_spec("local_config")
found = local_config is not None

set_display()