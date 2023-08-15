#!/usr/bin/env python3
''' module for task 8 '''


def list_all(mongo_collection):
    ''' function that lists all documents in a collection '''
    if mongo_collection is None:
        return []
    else:
        documents = list(mongo_collection.find())
        return documents

