# Python Utilities
This is a collection of python scripts used for projects at work.

## Elastic to CSV
Connects to an Elasticsearch cluster and reads documents from an index and places them into a CSV file called output.csv. This might be useful if you wanted to take operational data held in elasticsearch and use it for ML purposes.

To use this script you'll need to pip install elasticsearch_dsl and pandas. The elasticsearch libraries you install must be compatible with you elasticsearch cluster. Here I'm running against elasticsearch 6 so I install the v6 library

```
sudo pip3 install elasticsearch-dsl==6
```

You will also need to add host, port and userID/pwd information in the placeholders on lines 7-9.

