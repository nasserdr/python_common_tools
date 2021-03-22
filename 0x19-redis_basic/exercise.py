#!/usr/bin/env python3
"""
Create a Cache class
"""
import redis
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
        """
        takes data and store it with a key
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
