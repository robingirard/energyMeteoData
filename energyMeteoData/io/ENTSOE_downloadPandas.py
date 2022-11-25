from entsoe import EntsoePandasClient
import pandas as pd

#PROXY = {"http":"http://10.42.32.29:8080","https":"https://10.42.32.29:8080"}
TOKEN = 'b0dcb78f-e4d0-4016-9bd2-d3c4f80e0fd9'
client = EntsoePandasClient(api_key = TOKEN)

start = pd.Timestamp('20150101', tz='Europe/Brussels') #20140101
end = pd.Timestamp('20220101', tz='Europe/Brussels') #20220101
country_code = 'FR'  # France
#country_code_from = 'FR'  # France
#country_code_to = 'DE_LU' # Germany-Luxembourg
#type_marketagreement_type = 'A01'
#contract_marketagreement_type = "A01"

ts = client.query_load(country_code, start=start, end=end)
ts.to_csv('outfile_load.csv')

ts2 = client.query_generation_per_plant(country_code, start=start,end=end, psr_type=None)
ts2.to_csv('outfile_generation_per_plant.csv')

# client.query_load_forecast(country_code, start=start,end=end)
# client.query_load_and_forecast(country_code, start=start, end=end)
# client.query_generation_forecast(country_code, start=start,end=end)
# client.query_wind_and_solar_forecast(country_code, start=start,end=end, psr_type=None)
# client.query_generation(country_code, start=start,end=end, psr_type=None)
# client.query_installed_generation_capacity(country_code, start=start,end=end, psr_type=None)
# client.query_installed_generation_capacity_per_unit(country_code, start=start,end=end, psr_type=None)
# client.query_imbalance_prices(country_code, start=start,end=end, psr_type=None)
# client.query_contracted_reserve_prices(country_code, start, end, type_marketagreement_type, psr_type=None)
# client.query_contracted_reserve_amount(country_code, start, end, type_marketagreement_type, psr_type=None)
# client.query_unavailability_of_generation_units(country_code, start=start,end=end, docstatus=None, periodstartupdate=None, periodendupdate=None)
# client.query_unavailability_of_production_units(country_code, start, end, docstatus=None, periodstartupdate=None, periodendupdate=None)
# client.query_unavailability_transmission(country_code_from, country_code_to, start, end, docstatus=None, periodstartupdate=None, periodendupdate=None)
# client.query_withdrawn_unavailability_of_generation_units(country_code, start, end)
# client.query_import(country_code, start, end)
# client.query_generation_import(country_code, start, end)
# client.query_procured_balancing_capacity(country_code, start, end, process_type, type_marketagreement_type=None)
