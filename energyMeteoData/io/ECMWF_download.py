

#region imports and variable definitions
import cdsapi
import xarray as xr
Europe_area = [ 60, -10, 34, 30, ]
all_day_times = [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ]
all_mon_days = [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ]
all_year_mon=[
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ]
output_folder = "D:\\Meteorological_data\\ECMWF\\input\\ERA5\\Europe\\"
#endregion

#region Wind download
for year in range(2010,2021):
    print(year)
    #see https://cds.climate.copernicus.eu/api-how-to
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [
                '10m_u_component_of_wind','10m_v_component_of_wind'
            ],
            'year': str(year),
            'month': all_year_mon,
            'day': all_mon_days,
            'time': all_day_times,
            'area': Europe_area,
            "format": "netcdf"
        },
        output_folder+'era5_Wind_'+str(year)+'.nc')
#endregion

#region solar download
for year in range(2010,2021):
    print(year)
    #see https://cds.climate.copernicus.eu/api-how-to
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [
                 'surface_net_solar_radiation', 'surface_solar_radiation_downwards'
            ],
            'year': str(year),
            'month': all_year_mon,
            'day': all_mon_days,
            'time': all_day_times,
            'area': Europe_area,
            "format": "netcdf"
        },
        output_folder+'era5_Solar_'+str(year)+'.nc')
#endregion

#region temperature download
for year in range(2010,2021):
    print(year)
    #see https://cds.climate.copernicus.eu/api-how-to
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'netcdf',
            'variable': [
                 '2m_temperature'
            ],
            'year': str(year),
            'month': all_year_mon,
            'day': all_mon_days,
            'time': all_day_times,
            'area': Europe_area,
            "format": "netcdf"
        },
        output_folder+'era5_T2m_'+str(year)+'.nc')
#endregion

ds = xr.open_dataset('download.nc')
df = ds.to_dataframe()
df.columns=["Temperature"]





