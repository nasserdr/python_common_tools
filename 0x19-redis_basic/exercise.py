#!/usr/bin/env python3
"""
Create a Cache class
"""
import redis
import random


class Cache:
    """
    The class Cache
    """
    def __init__(self):
        """
        Initialize the method init
        """
        _redis = redis.Redis()
        _redis.flushdb()

    def store(self, data):
        r = random.getrandbits(32)
        client = self._redis
        return(client.set({r:data}))
