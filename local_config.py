#you can change this file adding data_path_pathlib elements required for your work and put the file either in the project folder or
#if you want it to be shared by all project, in your /Users/[username]/ folder.
import pandas as pd
from pathlib import Path
import socket

def My_local_config():
    print('Local config of Santiago')

    pd.options.display.width = 0
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    if (socket.gethostname()=='Santiagos-MacBook-Pro.local'):
        My_data_path = Path().absolute() /'..' / 'input'

    data_path_pathlib ={
        'base' : My_data_path,
        'ECMWF' : Path("/Users") /"sant"/"Documents"/"MINES PARIS"/"2A"/"T2"/"Recherche Simulation de Production éolienne"/"Github"/"Data"/ "Données ECMWF nc",
        'Europe' : Path("/Users") /"sant"/"Documents"/"MINES PARIS"/"2A"/"T2"/"Recherche Simulation de Production éolienne"/"Github"/"Data"/"Europe",

        #'France' : Path("/Users") /"robin.girard"/"Documents"/"Code"/"Data"/"Maps"/"France"
        #"renewable.ninja"
    }

    return data_path_pathlib
