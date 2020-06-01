# Python Utilities
This is a collection of python scripts used for projects at work.

## Elastic to CSV
Connects to an Elasticsearch cluster and reads documents from an index and places them into a CSV file called output.csv. This might be useful if you wanted to take operational data held in elasticsearch and use it for ML purposes.

To use this script you'll need to pip install elasticsearch_dsl and pandas. The elasticsearch libraries you install must be compatible with you elasticsearch cluster. Here I'm running against elasticsearch 6 so I install the v6 library

```
sudo pip3 install elasticsearch-dsl==6
```

You will also need to add host, port and userID/pwd information in the placeholders on lines 7-9.

This example is specific to BAI and BAW process summaries but you can see I've changed the search to find all the completed process summry docs for a process called "Cash Allocation". I don't want the task activities so I've added a second search parameter to match type="process"

```
s = Search(using=client, index='process-summaries-completed-idx-ibm-bai-2020.01.10-000001') \
    .query("match", processApplicationName="Cash Allocation") \
    .query("match", type="process")
```

Here is some exampe output, the data column contains data from the tracking group.

![Example Output](https://github.com/gerry-baird/python-utils/blob/master/img/elastic_to_csv_example.jpg)
