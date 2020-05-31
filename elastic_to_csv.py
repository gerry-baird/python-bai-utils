from elasticsearch import Elasticsearch, helpers, exceptions
from elasticsearch_dsl import Search
import pandas as pd
import sys
import json

host = "<yourhostname>"
port = 443
auth = '<your userid>:<your password>'

# declare an instance of the Elasticsearch library
client = Elasticsearch([{'host': host, 'port': port, 'http_auth': auth}],
                       use_ssl=True,
                       verify_certs=False,
                       ssl_show_warn=False 
                       )

try:
    # use the JSON library's dump() method for indentation
    info = json.dumps(client.info(), indent=4)

    # pass client object to info() method
    print("Elasticsearch client info():", info)

except exceptions.ConnectionError as err:

    # print ConnectionError for Elasticsearch
    print("\nElasticsearch info() ERROR:", err)
    print("\nThe client host:", host, "is invalid or cluster is not running")

    # change the client's value to 'None' if ConnectionError
    client = None

if client == None:
    sys.exit()

s = Search(using=client, index='incidents').query("match", category="Leak")
response = s.execute()

results_df = pd.DataFrame((d.to_dict() for d in s.scan()))

print(results_df)

results_df.to_csv('output.csv')
