#!/usr/bin/env python3
""" insert school """
from typing import Dict, Any


def insert_school(mongo_collection, **kwargs) -> str:
    """ insert school

    Args:
        mongo_collection (object): mongodb collection

    Returns:
        str: id of new document
    """
    new_school: Dict[Any, Any] = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
