#!/usr/bin/env python3
""" filter school documents by topic """


def schools_by_topic(mongo_collection, topic):
    """ filter school documents by topic """
    return mongo_collection.find({"topics": topic})
