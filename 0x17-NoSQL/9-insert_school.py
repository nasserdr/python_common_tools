#!/usr/bin/env python3
"""
insert a doc
"""

def insert_school(mongo_collection, **kwargs):
    """
    insert kwargs and return the inserted ID
    """
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
