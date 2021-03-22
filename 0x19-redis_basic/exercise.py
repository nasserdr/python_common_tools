#!/usr/bin/env python3
"""
Create a Cache class
"""
import redis
import random
import uuid

class Cache:
    """
    The class Cache
    """
    def __init__(self):
        """
        Initialize the method init
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
