#!/usr/bin/env python3
"""
returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
    mongo_collection.update({'averageScore': {$avg: 'score'}})
    mongo_collection.find({'_id':1, 'averageScore': 1}).sort('averageScore')
