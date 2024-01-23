#!/usr/bin/env python3
""" scripts that prints nginx logs stats mongo db """
from pymongo import MongoClient


def main() -> None:
    """ Main funtion for the script algorithm
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    # print the number of documents in the collection
    print(f'{logs_collection.count_documents({})} logs')
    # print the Methods
    print('Methods:')
    # get the status
    status_count: int = logs_collection.count_documents({"method": "GET",
                                                         "path": "/status"})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # loop through the methods
    for method in methods:
        method_count: int = logs_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    # print the status check
    print(f'{status_count} status check')

    print("IPs:")

    # carry out aggregate on the collection
    # create the pipeline
    pipeline = [
        # group for accumulations
        {"$group": {
            "_id": "$ip", "count": {
                "$sum": 1
            }
        }
        },
        # sort
        {
            "$sort": {
                "count": -1
            }
        },
        # limit
        {"$limit": 10},
        # start a new project to pass to the next satge
        {
            # remove the _id column, rename _id as ip, include count column
            "$project": {"_id": 0, "ip": "$_id", "count": 1}
        }
    ]
    top_10_ips = logs_collection.aggregate(pipeline)
    # loop through the ip arrays
    for ip_obj in top_10_ips:
        count = ip_obj.get("count")
        ip = ip_obj.get("ip")
        print(f'\t{ip}: {count}')


if __name__ == "__main__":
    main()
