def list_all(mongo_collection):
    """
    Lists all documents in mongo_collection
    """
    return mongo_collection.find({})
