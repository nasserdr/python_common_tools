#!/usr/bin/env python3
"""
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    q = {'topics': {'$elemMatch': {'$eq': topic}}}
    mongo_collection.find(q)
