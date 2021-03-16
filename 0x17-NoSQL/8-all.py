def list_all(mongo_collection):
    return mongo_collection.find({})
