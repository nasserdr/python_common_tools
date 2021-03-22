Cache = __import__('exercise').Cache
r = Cache()
r.store("test")

cache = Cache()

TEST_CASES = {
    b'foo': None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    cache.get(key, fn=fn)
    #assert cache.get(key, fn=fn) == value
