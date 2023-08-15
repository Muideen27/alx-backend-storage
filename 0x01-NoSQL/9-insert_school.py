#!/usr/bin/env python3
''' module for task 9 '''


def insert_school(mongo_collection, **kwargs):
    '''Python function that inserts a new document in a collection based on kwargs'''
    if mongo_collection is None:
        return None
    
    try:
        result = mongo_collection.insert_one(kwargs)
        return result.inserted_id
    except Exception as e:
        print("An error occurred:", str(e))
        return None

