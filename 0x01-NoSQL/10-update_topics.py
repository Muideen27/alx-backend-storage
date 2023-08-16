#!/usr/bin/env python3
''' module for task 10 '''


def update_topics(mongo_collection, name, topics):
    '''Python function that changes all topics of a school document based on the name'''
    if mongo_collection is None:
        return
    
    try:
        mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    except Exception as e:
        print("An error occurred:", str(e))

