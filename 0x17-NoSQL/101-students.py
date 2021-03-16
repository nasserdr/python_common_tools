#!/usr/bin/env python3
"""
returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
    return mongo_collection.find('students').sort("averageScore")
