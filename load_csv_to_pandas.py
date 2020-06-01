import pandas as pd
import json

raw_data = pd.read_csv('output.csv')

raw_data['data'] = raw_data['data'].str.replace("\'", "\"")


json_df = pd.concat([pd.json_normalize(json.loads(js)) for js in raw_data['data']])

print(json_df.head())

