#!/usr/bin/env python3
""" Update topics """


def update_topics(mongo_collection, name, topics) -> dict:
    """ update_topics.

    Args:
        mongo_collection (object): mongo_db collection
        name (str): school name to be updated
        topics (list[str]): topics to be updated

    Returns:
        dict: the updated school document
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
