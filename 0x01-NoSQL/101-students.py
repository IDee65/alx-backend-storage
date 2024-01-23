#!/usr/bin/env python3
""" Python function that returns all students sorted by average score """


def top_students(mongo_collection):
    """ get the top students

    Args:
        mongo_collection (Collection): mongodb collection

    Returns:
        list: list of documents
    """
    # set the aggregrate pipeline, i.e arrays of stages
    pipeline = [
        # project stage
        {"$project": {"name": "$name",
                      "averageScore": {"$avg": "$topics.score"}}},
        # sort stage
        {"$sort": {"averageScore": -1}}


    ]
    result = list(mongo_collection.aggregate(pipeline))

    return result
