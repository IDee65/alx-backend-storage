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


if __name__ == "__main__":
    main()
