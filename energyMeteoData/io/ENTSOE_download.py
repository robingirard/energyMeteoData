from entsoe import EntsoePandasClient
import pandas as pd

PROXY = {"http":"http://10.42.32.29:8080","https":"https://10.42.32.29:8080"}
TOKEN = 'afe838d5-438d-4b17-966f-e47ddfca5882'
client = EntsoePandasClient(api_key = TOKEN, proxies = PROXY, retry_delay = 60, retry_count = 10)

start = pd.Timestamp('20170101', tz='Europe/Brussels')
end = pd.Timestamp('20201231', tz='Europe/Brussels')
country_code = 'BE'  # Belgium
#country_code_from = 'FR'  # France
#country_code_to = 'DE_LU' # Germany-Luxembourg
#type_marketagreement_type = 'A01'
#contract_marketagreement_type = "A01"

client.query_load(country_code, start=start,end=end)
client.query_generation_per_plant(country_code, start=start,end=end, psr_type=None)