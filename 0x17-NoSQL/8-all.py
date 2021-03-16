def list_all(mongo_collection):
    """
    Lists all documents in mongo_collection
    """
    return list(mongo_collection.find({}))
