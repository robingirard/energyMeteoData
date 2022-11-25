from entsoe import EntsoePandasClient
import pandas as pd

#PROXY = {"http":"http://10.42.32.29:8080","https":"https://10.42.32.29:8080"}
TOKEN = 'b0dcb78f-e4d0-4016-9bd2-d3c4f80e0fd9'
client = EntsoePandasClient(api_key = TOKEN, retry_delay = 60, retry_count = 10)

start = pd.Timestamp('20150101', tz='Europe/Brussels') #20140101
end = pd.Timestamp('20220101', tz='Europe/Brussels') #20220101
country_code = 'FR'  # France
# #country_code_from = 'FR'  # France
#country_code_to = 'DE_LU' # Germany-Luxembourg
#type_marketagreement_type = 'A01'
#contract_marketagreement_type = "A01"

client.query_load(country_code, start=start,end=end)
client.query_generation_per_plant(country_code, start=start,end=end, psr_type=None)

xml_string = client.query_load(country_code, start, end)
with open('outfile_load.xml', 'w') as f:
    f.write(xml_string)

xml_string = client.query_load(country_code, start, end)
with open('outfile_generation_per_plant.xml', 'w') as f:
    f.write(xml_string)
