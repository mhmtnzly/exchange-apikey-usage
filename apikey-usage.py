import requests
import pandas as pd
url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=fe52a9a86d4fc451ee3a6bbe86e0db89"
response=requests.get(url)
response=response.json()['rates']
response=pd.json_normalize(response).T
response.columns=['Rates']
print(response.head())
response.to_csv('exchange_rates_1.csv')