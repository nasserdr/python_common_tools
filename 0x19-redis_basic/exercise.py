#!/usr/bin/env python3
"""
Create a Cache class
"""
import redis
import uuid
from typing import Union, Optional, Callable


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

    def store(self, data: Union[str, bytes, int, float]):
        """
        takes data and store it with a key
        """
        key = uuid.uuid1()
        self._redis.set(str(key), str(data))
        return str(key)

    def get(self, key: str, fn: Optional[Callable]):
        self._redis.get(key)
